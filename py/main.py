#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------------
# @Time    : 2025/9/26 17:37
# @Author  : WXY
# @File    : main.py
# @PROJECT_NAME: youtubedown_gui
# @PRODUCT_NAME: PyCharm
# -------------------------------------------------------------------------------
import sys
import os
import atexit
import shutil

# 添加项目目录到Python路径 - 必须在导入自定义模块之前
current_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.dirname(current_dir)
for path in (project_dir, current_dir):
    if path not in sys.path:
        sys.path.insert(0, path)

# ✅ 在打包环境下释放locales目录 - 必须在其他模块导入之前
if getattr(sys, 'frozen', False):
    try:
        import runtime_extract
        print("✅ locales目录释放脚本已执行")
    except ImportError as e:
        print(f"⚠️ 无法导入runtime_extract: {e}")
    except Exception as e:
        print(f"❌ 释放locales目录失败: {e}")

# 现在导入PySide6和自定义模块
from PySide6.QtCore import QEvent, QSettings
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
from py.Splashcreen import SplashScreen
from py_gui.mainwindow_ui import Ui_MainWindow
from py.GlobalExceptionHandler import GlobalExceptionHandler
from py.SingleInstanceManager import SingleInstanceManager
from py.LoggerManager import logger_manager
from py.Videoselect import Videoselect
from py.Imageselect import Imageselect
from py.Projectinfo import ProjectInfoWindow
from py.Settings import SettingsWindow
from utils import show_error, APPNAME, setup_window_icon, COPYRIGHT, get_project_root, setup_window_title, get_max_image_count
# from py_gui import resource_rc


class MainWindow(QMainWindow):
    IMAGE_MODE_STYLE = """#imageModeFrame {
    background-color: #F5F0FF;
    border: 2px solid #7C3BED;
    border-radius: 8px;
}
#imageModeIconBg {
    background-color: #DDD0FF;
    border-radius: 22px;
}
#imageModeTitle {
    color: #7C3BED;
    font-size: 14px;
}
#imageModeSubTitle {
    color: #4B5563;
    font-size: 12px;
}"""

    IMAGE_MODE_UNSELECTED_STYLE = """#imageModeFrame {
    background-color: #F3F4F6;
    border: 1px solid #F3F4F6;
    border-radius: 8px;
}
#imageModeIconBg {
    background-color: transparent;
    border: none;
}
#imageModeTitle {
    color: #4B5563;
    font-size: 14px;
}
#imageModeSubTitle {
    color: #4B5563;
    font-size: 12px;
}"""

    VIDEO_MODE_STYLE = """#videoModeFrame {
    background-color: #F3F4F6;
    border: 1px solid #F3F4F6;
    border-radius: 8px;
}
#videoModeIconBg {
    background-color: transparent;
    border: none;
}
#videoModeTitle {
    color: #4B5563;
    font-size: 14px;
}
#videoModeSubTitle {
    color: #4B5563;
    font-size: 12px;
}"""

    VIDEO_MODE_SELECTED_STYLE = """#videoModeFrame {
    background-color: #F5F0FF;
    border: 2px solid #7C3BED;
    border-radius: 8px;
}
#videoModeIconBg {
    background-color: #DDD0FF;
    border-radius: 22px;
}
#videoModeTitle {
    color: #7C3BED;
    font-size: 14px;
}
#videoModeSubTitle {
    color: #4B5563;
    font-size: 12px;
}"""

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        setup_window_icon(self)
        setup_window_title(self)
        self.current_mode = "image"
        self.video_select_window = None
        self.image_select_window = None
        self._settings = QSettings("pinzimu", "pinzimu_gui")
        self._settings_window = None
        self._fix_image_paths()
        self._bind_events()
        self._apply_saved_settings()
    
    def eventFilter(self, watched, event):
        if event.type() == QEvent.Type.MouseButtonPress:
            if watched == self.ui.videoModeFrame:
                self._select_video_file()
                return True
            if watched == self.ui.imageModeFrame:
                self._select_image_file()
                return True
        return super().eventFilter(watched, event)

    def _bind_events(self):
        self.ui.videoModeFrame.installEventFilter(self)
        self.ui.imageModeFrame.installEventFilter(self)
        self.ui.btnSelectFile.clicked.connect(self._select_file_by_current_mode)
        self.ui.btnProjectInfo.clicked.connect(self._show_project_info)
        self.ui.btnSettings.clicked.connect(self._show_settings)

    def _select_file_by_current_mode(self):
        if self.current_mode == "video":
            self._select_video_file()
        else:
            self._select_image_file()

    def _show_project_info(self):
        self._project_info_window = ProjectInfoWindow(self)
        self._project_info_window.show()

    def _show_settings(self):
        self._settings_window = SettingsWindow(self)
        self._settings_window.show()

    def _apply_saved_settings(self):
        max_image = get_max_image_count()
        self.ui.imageModeSubTitle.setText(f"最多{max_image}张")

    def _select_image_mode(self):
        self.current_mode = "image"
        self.ui.imageModeFrame.setStyleSheet(self.IMAGE_MODE_STYLE)
        self.ui.videoModeFrame.setStyleSheet(self.VIDEO_MODE_STYLE)
        self.ui.labelUploadTitle.setText("上传图片文件")
        self.ui.labelUploadSubtitle.setText("选择多张图片，系统将按顺序拼接成字幕长图")
        self.ui.btnSelectFile.setText("选择图片")
        self.ui.labelFormats.setText("支持格式：JPG、PNG、GIF、WEBP")

    def _select_video_mode(self):
        self.current_mode = "video"
        self.ui.imageModeFrame.setStyleSheet(self.IMAGE_MODE_UNSELECTED_STYLE)
        self.ui.videoModeFrame.setStyleSheet(self.VIDEO_MODE_SELECTED_STYLE)
        self.ui.labelUploadTitle.setText("上传视频文件")
        self.ui.labelUploadSubtitle.setText("视频文件只能选择一个")
        self.ui.btnSelectFile.setText("选择视频")
        self.ui.labelFormats.setText("支持格式：mp4、mov、mkv、avi、wmv、webm")

    def _select_image_file(self):
        self._select_image_mode()
        last_dir = self._settings.value("last_image_dir", "")
        if not last_dir or not os.path.exists(last_dir):
            last_dir = ""
        file_paths, _ = QFileDialog.getOpenFileNames(
            self,
            "选择图片文件",
            last_dir,
            "图片文件 (*.jpg *.jpeg *.png *.gif *.webp)"
        )
        if file_paths:
            max_count = get_max_image_count()
            if len(file_paths) > max_count:
                from PySide6.QtWidgets import QMessageBox
                QMessageBox.warning(self, "超出限制", f"最多支持{max_count}张图片，已截取前{max_count}张")
                file_paths = file_paths[:max_count]
            self._settings.setValue("last_image_dir", os.path.dirname(file_paths[0]))
            self.image_select_window = Imageselect(file_paths, self)
            self.hide()
            self.image_select_window.show()

    def _select_video_file(self):
        self._select_video_mode()
        last_dir = self._settings.value("last_video_dir", "")
        if not last_dir or not os.path.exists(last_dir):
            last_dir = ""
        video_path, _ = QFileDialog.getOpenFileName(
            self,
            "选择视频文件",
            last_dir,
            "视频文件 (*.mp4 *.mov *.mkv *.avi *.wmv *.webm)"
        )
        if video_path:
            self._settings.setValue("last_video_dir", os.path.dirname(video_path))
            self.video_select_window = Videoselect(video_path, self)
            self.hide()
            self.video_select_window.show()
    
    def _fix_image_paths(self):
        """修复图片路径问题 - 将相对路径转换为绝对路径"""
        project_dir = get_project_root()
        image_png_path = os.path.join(project_dir, "imgs", "image.png")
        video_png_path = os.path.join(project_dir, "imgs", "video.png")
        
        # 为标签设置正确的图片
        from PySide6.QtGui import QPixmap
        if os.path.exists(image_png_path):
            self.ui.imageModeIconLabel.setPixmap(QPixmap(image_png_path))
        if os.path.exists(video_png_path):
            self.ui.videoModeIconLabel.setPixmap(QPixmap(video_png_path))


def _clean_temp_frames():
    """清理 temp_frames 临时目录"""
    try:
        temp_dir = os.path.join(get_project_root(), "temp_frames")
        if os.path.exists(temp_dir):
            shutil.rmtree(temp_dir)
            logger_manager.info("清理临时文件目录: temp_frames", "main")
    except Exception as e:
        logger_manager.warning(f"清理临时文件目录失败: {e}", "main")


def main():
    """主函数"""
    try:
        # 创建应用程序实例
        app = QApplication(sys.argv)

        # 清理上次运行残留的临时帧文件（防止非正常退出导致残留）
        _clean_temp_frames()
        atexit.register(_clean_temp_frames)
        
        # 设置应用程序属性 - 在创建任何窗口之前设置
        app.setQuitOnLastWindowClosed(True)
        
        # 设置中文语言环境 - 必须在 QApplication 创建后立即设置
        from PySide6.QtCore import QLocale, QTranslator, QLibraryInfo

        locale = QLocale(QLocale.Language.Chinese, QLocale.Country.China)
        QLocale.setDefault(locale)

        translator = QTranslator()
        qt_translations_path = QLibraryInfo.path(QLibraryInfo.LibraryPath.TranslationsPath)
        if translator.load(locale, "qtbase", "_", qt_translations_path):
            app.installTranslator(translator)
        else:
            if translator.load(locale, "qt", "_", qt_translations_path):
                app.installTranslator(translator)

        # 初始化单例管理器
        instance_manager = SingleInstanceManager(APPNAME)
        if instance_manager.is_running():
            show_error(None,"提示", "应用程序已运行。")
            return 0

        # 启动单例服务器
        if not instance_manager.start_server():
            show_error(None,"提示", "无法启动单例服务器")
            return 1

        # 设置全局异常处理器
        exception_handler = GlobalExceptionHandler()
        sys.excepthook = exception_handler.handle_exception

        # 初始化日志管理器
        logger_manager.info("应用程序启动", "main")

        from utils import get_logging_enabled
        if not get_logging_enabled():
            logger_manager.setup_file_logging(enable_debug=False)
            logger_manager.info("日志记录已禁用", "main")

        # 创建主窗口（先不显示）
        main_window = MainWindow()

        # 创建并显示启动界面
        splash = SplashScreen()

        # 连接单例管理器的信号到启动界面的置顶方法
#        instance_manager.show_window_signal.connect(splash.bring_to_front)

        def on_splash_finished():
            main_window.show()
            main_window.raise_()
            main_window.activateWindow()
            splash.close()

        splash.finished.connect(on_splash_finished)

        splash.show()

        # 运行应用程序
        result = app.exec()

        logger_manager.info("应用程序退出", "main")
        return result

    except Exception as e:
        print(f"应用程序启动失败: {e}")
        import traceback
        traceback.print_exc()
        return 1

if __name__ == "__main__":
    sys.exit(main())