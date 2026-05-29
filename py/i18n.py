#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------------
# @Time    : 2025/1/27
# @Author  : WXY
# @File    : i18n.py
# @PROJECT_NAME: youtubedown_gui
# @PRODUCT_NAME: PyCharm
# -------------------------------------------------------------------------------

import json
import os
import sys
from typing import Dict, Optional
from PySide6.QtCore import QObject, Signal
from SettingsManager import settings_manager
from LoggerManager import logger_manager


# 语言相关常量定义
LANGUAGE_DISPLAY_NAMES = {
    "zh_CN": "简体中文",
    "en_US": "English", 
    "ja_JP": "日本語"
}

# 显示名称到语言代码的映射
DISPLAY_TO_CODE_MAP = {
    "简体中文": "zh_CN",
    "English": "en_US",
    "日本語": "ja_JP"
}
# 语言显示顺序（用于UI中的下拉框等）
LANGUAGE_ORDER = ["zh_CN", "en_US", "ja_JP"]
# 语言代码到索引的映射
CODE_TO_INDEX_MAP = {
    "zh_CN": 0,
    "en_US": 1,
    "ja_JP": 2
}

# 索引到语言代码的映射
INDEX_TO_CODE_MAP = {
    0: "zh_CN",
    1: "en_US", 
    2: "ja_JP"
}



class I18nManager(QObject):
    """国际化管理器"""

    # 语言切换信号
    language_changed = Signal(str)

    def __init__(self):
        super().__init__()
        self.current_language = "zh_CN"  # 默认中文
        self.translations: Dict[str, Dict[str, str]] = {}
        self.supported_languages =LANGUAGE_DISPLAY_NAMES.copy()  
        # 获取locales目录路径
        self.locales_dir = self._get_locales_dir()

        # 加载所有语言文件
        self._load_all_translations()

        # 从设置中加载用户选择的语言
        self._load_language_from_settings()

    def _get_locales_dir(self) -> str:
        """获取locales目录的绝对路径"""
        if getattr(sys, 'frozen', False):
            # 打包后的exe环境
            base_dir = os.path.dirname(sys.executable)
        else:
            # 开发环境
            base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

        return os.path.join(base_dir, "locales")

    def _load_all_translations(self):
        """加载所有语言翻译文件"""
        for lang_code in self.supported_languages.keys():
            self._load_translation(lang_code)

    def _load_translation(self, lang_code: str):
        """加载指定语言的翻译文件"""
        file_path = os.path.join(self.locales_dir, f"{lang_code}.json")

        try:
            if os.path.exists(file_path):
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read().strip()
                    if content:  # 文件不为空
                        self.translations[lang_code] = json.loads(content)
                    else:  # 文件为空，初始化为空字典
                        self.translations[lang_code] = {}
            else:
                # 文件不存在，创建空的翻译字典
                self.translations[lang_code] = {}
                logger_manager.warning(f"语言文件不存在: {file_path}", "i18n")

        except json.JSONDecodeError as e:
            logger_manager.error(f"解析语言文件失败 {file_path}: {e}", "i18n")
            self.translations[lang_code] = {}
        except Exception as e:
            logger_manager.error(f"加载语言文件失败 {file_path}: {e}", "i18n")
            self.translations[lang_code] = {}

    def _load_language_from_settings(self):
        """从设置中加载用户选择的语言"""
        try:
            saved_language = settings_manager.get_setting("language", "zh_CN")
            if saved_language in self.supported_languages:
                self.current_language = saved_language
            else:
                logger_manager.warning(f"不支持的语言设置: {saved_language}，使用默认语言", "i18n")
        except Exception as e:
            logger_manager.error(f"加载语言设置失败: {e}", "i18n")

    def set_language(self, lang_code: str):
        """设置当前语言"""
        if lang_code not in self.supported_languages:
            logger_manager.error(f"不支持的语言代码: {lang_code}", "i18n")
            return False

        if self.current_language != lang_code:
            self.current_language = lang_code

            # 保存到设置
            try:
                settings_manager.set_setting("language", lang_code)
                logger_manager.info(f"语言已切换到: {self.supported_languages[lang_code]}", "i18n")

                # 发出语言切换信号
                self.language_changed.emit(lang_code)
                return True
            except Exception as e:
                logger_manager.error(f"保存语言设置失败: {e}", "i18n")
                return False

        return True

    def get_current_language(self) -> str:
        """获取当前语言代码"""
        return self.current_language

    def get_supported_languages(self) -> Dict[str, str]:
        """获取支持的语言列表"""
        return self.supported_languages.copy()

    # 这个版本不支持点号分隔的嵌套键访问
    def translate_no_dot(self, key: str, default: Optional[str] = None) -> str:
        """翻译文本"""
        # 如果没有提供默认值，使用key作为默认值
        if default is None:
            default = key

        # 获取当前语言的翻译
        current_translations = self.translations.get(self.current_language, {})

        # 查找翻译
        if key in current_translations:
            return current_translations[key]

        # 如果当前语言没有翻译，尝试使用中文作为后备
        if self.current_language != "zh_CN":
            zh_translations = self.translations.get("zh_CN", {})
            if key in zh_translations:
                return zh_translations[key]

        # 都没有找到，返回默认值
        return default

    def translate(self, key: str, default: Optional[str] = None) -> str:
        """翻译文本，支持点号分隔的嵌套键访问"""
        # 如果没有提供默认值，使用key作为默认值
        if default is None:
            default = key

        # 获取当前语言的翻译
        current_translations = self.translations.get(self.current_language, {})

        # 支持点号分隔的嵌套键访问
        def get_nested_value(data: dict, key_path: str):
            """从嵌套字典中获取值，支持点号分隔的路径"""
            keys = key_path.split('.')
            current = data

            for k in keys:
                if isinstance(current, dict) and k in current:
                    current = current[k]
                else:
                    return None
            return current

        # 查找翻译
        result = get_nested_value(current_translations, key)
        if result is not None and isinstance(result, str):
            return result

        # 如果当前语言没有翻译，尝试使用中文作为后备
        if self.current_language != "zh_CN":
            zh_translations = self.translations.get("zh_CN", {})
            result = get_nested_value(zh_translations, key)
            if result is not None and isinstance(result, str):
                return result

        # 都没有找到，返回默认值
        return default

    def add_translation(self, lang_code: str, key: str, value: str):
        """添加翻译条目"""
        if lang_code not in self.supported_languages:
            logger_manager.error(f"不支持的语言代码: {lang_code}", "i18n")
            return False

        if lang_code not in self.translations:
            self.translations[lang_code] = {}

        self.translations[lang_code][key] = value
        return True

    def save_translations(self, lang_code: str):
        """保存翻译到文件"""
        if lang_code not in self.supported_languages:
            logger_manager.error(f"不支持的语言代码: {lang_code}", "i18n")
            return False

        file_path = os.path.join(self.locales_dir, f"{lang_code}.json")

        try:
            # 确保目录存在
            os.makedirs(self.locales_dir, exist_ok=True)

            # 保存翻译
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(
                    self.translations.get(lang_code, {}),
                    f,
                    ensure_ascii=False,
                    indent=2
                )

            logger_manager.info(f"翻译文件已保存: {file_path}", "i18n")
            return True

        except Exception as e:
            logger_manager.error(f"保存翻译文件失败 {file_path}: {e}", "i18n")
            return False

    def reload_translations(self):
        """重新加载所有翻译文件"""
        self.translations.clear()
        self._load_all_translations()
        logger_manager.info("翻译文件已重新加载", "i18n")


# 创建全局实例
i18n_manager = I18nManager()


# 提供便捷的翻译函数, i18n提供的简便函数, 这是一个约定

def _(key: str, default: Optional[str] = None) -> str:
    """便捷的翻译函数
        # 使用 _ 函数 - 简洁明了
title = _("app_title")
button_text = _("buttons.start_download")

# 如果不用 _，代码会很冗长
title = i18n_manager.translate("app_title")
button_text = i18n_manager.translate("buttons.start_download")
    """
    return i18n_manager.translate(key, default)


def tr(key: str, default: Optional[str] = None) -> str:
    """翻译函数的别名"""
    return i18n_manager.translate(key, default)