#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------------
# @Time    : 2025/9/26 17:38
# @Author  : WXY
# @File    : utils
# @PROJECT_NAME: youtubedown_gui
# @PRODUCT_NAME: PyCharm
# -------------------------------------------------------------------------------
from PySide6.QtWidgets import QMessageBox, QApplication
from PySide6.QtGui import QIcon
import os
import sys
from PySide6.QtCore import QSize, Qt, QFile, QIODevice
from LoggerManager import logger_manager
import psutil
import base64
import time
import requests
import socket

# 在文件开头添加版本号定义
VERSION = "V1.0.1"
AUTHOR = "WXY"
APPNAME = "PinZiMuGUI"
UNKNOWNCPU = "UNKNOWN_CPU"
UNKNOWNMOTHERBOARD = "UNKNOWN_MOTHERBOARD"
TOP_POSITION = 80.0
BOTTOM_POSITION = 99.0
COPYRIGHT = "© 2026 拼字幕 - 快速生成连续字幕长图"
# 客服微信图片 , 不能使用base64的图片, 打包工具对长字符串兼容不好, 虽然在debug可以运行, 但是一打包就挂了
# CUSTOMERSERVICE = """data:image/jpeg;base64,iVBORw0KGgoAAAA...ElFTkSuQmCC"""
# 客服微信图片结束
CUSTOMERSERVICE = "custom_coffee.jpg"

# 垂直滚动条样式
SCROLLBARSTYLE = """
        QScrollBar:vertical {
            background: rgba(255, 255, 255, 40);
            width: 12px;
            border-radius: 5px;
            margin: 0px;
            border: 1px solid rgba(255, 255, 255, 30);
        }

        QScrollBar::handle:vertical {
            background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 120), stop:1 rgba(255, 255, 255, 80));
            border: 1px solid rgba(255, 255, 255, 60);
            border-radius: 5px;
            min-height: 30px;
            margin: 2px;
        }

        QScrollBar::handle:vertical:hover {
            background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 150), stop:1 rgba(255, 255, 255, 110));
            border: 1px solid rgba(255, 255, 255, 80);
        }

        QScrollBar::handle:vertical:pressed {
            background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 100), stop:1 rgba(255, 255, 255, 60));
            border: 1px solid rgba(255, 255, 255, 100);
        }

        QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
            border: none;
            background: none;
            height: 0px;
        }

        QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
            background: rgba(255, 255, 255, 20);
        }

        QScrollBar:vertical:hover {
            background: rgba(255, 255, 255, 60);
            border: 1px solid rgba(255, 255, 255, 50);
        }
        """


# 完整的表格滚动条样式（包含水平和垂直滚动条）
TABLE_SCROLLBAR_STYLE = """
        /* 垂直滚动条 */
        QScrollBar:vertical {
            background: rgba(255, 255, 255, 40);
            width: 12px;
            border-radius: 5px;
            margin: 0px;
            border: 1px solid rgba(255, 255, 255, 30);
        }

        QScrollBar::handle:vertical {
            background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 120), stop:1 rgba(255, 255, 255, 80));
            border: 1px solid rgba(255, 255, 255, 60);
            border-radius: 5px;
            min-height: 30px;
            margin: 2px;
        }

        QScrollBar::handle:vertical:hover {
            background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 150), stop:1 rgba(255, 255, 255, 110));
            border: 1px solid rgba(255, 255, 255, 80);
        }

        QScrollBar::handle:vertical:pressed {
            background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 100), stop:1 rgba(255, 255, 255, 60));
            border: 1px solid rgba(255, 255, 255, 100);
        }

        QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
            border: none;
            background: none;
            height: 0px;
        }

        QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
            background: rgba(255, 255, 255, 20);
        }

        QScrollBar:vertical:hover {
            background: rgba(255, 255, 255, 60);
            border: 1px solid rgba(255, 255, 255, 50);
        }

        /* 水平滚动条 */
        QScrollBar:horizontal {
            background: rgba(255, 255, 255, 40);
            height: 12px;
            border-radius: 5px;
            margin: 0px;
            border: 1px solid rgba(255, 255, 255, 30);
        }

        QScrollBar::handle:horizontal {
            background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgba(255, 255, 255, 120), stop:1 rgba(255, 255, 255, 80));
            border: 1px solid rgba(255, 255, 255, 60);
            border-radius: 5px;
            min-width: 30px;
            margin: 2px;
        }

        QScrollBar::handle:horizontal:hover {
            background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgba(255, 255, 255, 150), stop:1 rgba(255, 255, 255, 110));
            border: 1px solid rgba(255, 255, 255, 80);
        }

        QScrollBar::handle:horizontal:pressed {
            background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgba(255, 255, 255, 100), stop:1 rgba(255, 255, 255, 60));
            border: 1px solid rgba(255, 255, 255, 100);
        }

        QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {
            border: none;
            background: none;
            width: 0px;
        }

        QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {
            background: rgba(255, 255, 255, 20);
        }

        QScrollBar:horizontal:hover {
            background: rgba(255, 255, 255, 60);
            border: 1px solid rgba(255, 255, 255, 50);
        }

        /* 滚动条交叉角落 */
        QScrollBar::corner {
            background: rgba(255, 255, 255, 40);
            border: 1px solid rgba(255, 255, 255, 30);
        }
        """


# QMESSAGEBOXSTYLE = """
#         QMessageBox {
#             background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #667eea, stop:1 #764ba2);
#             border-radius: 5px;
#             color: white;
#         }
#         QMessageBox QLabel {
#             color: white;
#             font-size: 14px;
#             padding: 10px;
#         }
#         QMessageBox QPushButton {
#             background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgba(255, 255, 255, 80), stop:1 rgba(255, 255, 255, 60));
#             border: 1px solid rgba(255, 255, 255, 100);
#             border-radius: 5px;
#             color: white;
#             font-weight: bold;
#             padding: 8px 16px;
#             min-width: 80px;
#         }
#         QMessageBox QPushButton:hover {
#             background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgba(255, 255, 255, 100), stop:1 rgba(255, 255, 255, 80));
#             border: 1px solid rgba(255, 255, 255, 150);
#         }
#         QMessageBox QPushButton:pressed {
#             background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgba(255, 255, 255, 60), stop:1 rgba(255, 255, 255, 40));
#         }
#     """


QMESSAGEBOXSTYLE = """
        QMessageBox {
            background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #f7f7f7, stop:1 #f7f7f7);
            border-radius: 5px;
            color: rgb(0, 0, 0);
        }
        QMessageBox QLabel {
            color: rgb(0, 0, 0);
            font-size: 14px;
            padding: 10px;
        }
        QMessageBox QPushButton {
            background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgba(255, 255, 255, 80), stop:1 rgba(255, 255, 255, 60));
            border: 1px solid rgba(138, 138, 138, 0.761);
            border-radius: 5px;
            color: rgb(0, 0, 0);
            font-weight: bold;
            padding: 8px 16px;
            min-width: 80px;
        }
        QMessageBox QPushButton:hover {
            background: rgba(196, 196, 196, 0.761);
            border: 1px solid rgba(138, 138, 138, 0.761);
        }
        QMessageBox QPushButton:pressed {
            background: rgba(163, 0, 252, 0.58);
        }
    """




# 应用程序标题常量
APP_TITLE = "拼字幕 - "+VERSION

# 禁用控件样式
DISABLED_CONTROL_STYLE = """
    QPushButton:disabled {
        color: #888888;
        background: rgba(200, 200, 200, 50);
        border: 1px solid rgba(150, 150, 150, 50);
    }
    QRadioButton:disabled {
        color: #888888;
    }
    QCheckBox:disabled {
        color: #888888;
    }
    QLineEdit:disabled {
        color: #888888;
        background: rgba(200, 200, 200, 30);
        border: 1px solid rgba(150, 150, 150, 50);
    }
"""


def get_setting(key, default=None):
    """从注册表读取配置项"""
    from PySide6.QtCore import QSettings
    settings = QSettings("pinzimu", "pinzimu_gui")
    return settings.value(f"settings/{key}", default)


def set_setting(key, value):
    """写入配置项到注册表"""
    from PySide6.QtCore import QSettings
    settings = QSettings("pinzimu", "pinzimu_gui")
    settings.setValue(f"settings/{key}", value)


def get_logging_enabled():
    """获取日志记录开关，默认开启"""
    val = get_setting("enable_logging", True)
    if isinstance(val, str):
        val = val.lower() in ("true", "1", "yes")
    return bool(val)


def set_logging_enabled(enabled):
    """设置日志记录开关"""
    set_setting("enable_logging", enabled)


def get_max_image_count():
    """获取最大图片数量，默认50"""
    try:
        return int(get_setting("max_image_count", 50))
    except (ValueError, TypeError):
        return 50


def set_max_image_count(count):
    """设置最大图片数量"""
    set_setting("max_image_count", int(count))


def get_max_video_frames():
    """获取最大视频帧数量，默认200"""
    try:
        return int(get_setting("max_video_frames", 200))
    except (ValueError, TypeError):
        return 200


def set_max_video_frames(count):
    """设置最大视频帧数量"""
    set_setting("max_video_frames", int(count))


def get_last_save_dir():
    """获取上次保存图片的目录"""
    val = get_setting("last_save_dir", "")
    if val and os.path.exists(val):
        return val
    return ""


def set_last_save_dir(dir_path):
    """保存图片的目录"""
    set_setting("last_save_dir", dir_path)


def setup_window_icon(window, icon_path="imgs/favicon.ico"):
    """为窗口设置图标"""
    icon = QIcon()
    icon_full_path = get_resource_path(icon_path)
    if os.path.exists(icon_full_path):
        icon.addFile(icon_full_path, QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        window.setWindowIcon(icon)
    else:
        print(f"Warning: Icon file not found: {icon_full_path}")

def setup_window_title(window, subtitle=""):
    """
    为窗口设置统一的标题

    Args:
        window: 窗口对象
        subtitle: 子标题（可选），如果提供则显示为 "拼字幕 - V1.0.1 - 子标题"
    """
    if subtitle:
        title = f"{APP_TITLE} - {subtitle}"
    else:
        title = APP_TITLE

    window.setWindowTitle(title)
    logger_manager.debug(f"设置窗口标题: {title}", "utils")

def get_bundled_resource_path(resource_name):
    """获取打包资源的路径（兼容开发和打包环境）, 支持在多个位置查找 FFmpeg"""
    if getattr(sys, 'frozen', False):
        # 打包后的exe环境
        base_path = sys._MEIPASS

        # 首先在根目录查找
        root_path = os.path.join(base_path, resource_name)
        if os.path.exists(root_path):
            return root_path

        # 然后在 py 子目录查找
        py_path = os.path.join(base_path, 'py', resource_name)
        if os.path.exists(py_path):
            return py_path

        # 最后返回根目录路径（即使不存在）
        return root_path
    else:
        # 开发环境
        base_path = os.path.dirname(os.path.abspath(__file__))
        return os.path.join(base_path, resource_name)

def setup_ffmpeg():
    """设置 ffmpeg 路径"""
    ffmpeg_path = get_bundled_resource_path('ffmpeg.exe')
    if os.path.exists(ffmpeg_path):
        os.environ["FFMPEG_BINARY"] = ffmpeg_path
        return ffmpeg_path
    else:
        # 如果找不到打包的 ffmpeg，尝试使用系统 PATH 中的
        import shutil
        system_ffmpeg = shutil.which('ffmpeg')
        if system_ffmpeg:
            os.environ["FFMPEG_BINARY"] = system_ffmpeg
            return system_ffmpeg
    return None

# def setup_ffprobe():
#     """设置 ffprobe 路径"""
#     ffprobe_path = get_bundled_resource_path('ffprobe.exe')
#     if os.path.exists(ffprobe_path):
#         return ffprobe_path
#     return None

def get_resource_path(filename):
    """获取资源文件路径，兼容打包后的exe"""
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, filename)
    else:
        project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        return os.path.join(project_root, filename)


def get_project_root():
    """获取项目根目录，兼容开发和打包环境"""
    if hasattr(sys, '_MEIPASS'):
        return sys._MEIPASS
    else:
        return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def show_message_with_icon(parent, icon_type, title, message, icon_path="imgs/favicon.ico"):
    """显示带图标的消息框"""
    msg_box = QMessageBox(parent)
    # 设置当前的弹窗窗口始终保持在最顶层
    msg_box.setWindowFlags(msg_box.windowFlags() | Qt.WindowType.WindowStaysOnTopHint)

    # 添加自定义样式
    msg_box.setStyleSheet(QMESSAGEBOXSTYLE)

    # 设置窗口图标
    icon_full_path = get_resource_path(icon_path)
    if os.path.exists(icon_full_path):
        msg_box.setWindowIcon(QIcon(icon_full_path))

    msg_box.setIcon(icon_type)
    msg_box.setWindowTitle(title)
    msg_box.setText(message)
    return msg_box.exec()

def show_info(parent, title, message, icon_path="imgs/favicon.ico"):
    """显示信息提示框"""
    return show_message_with_icon(parent, QMessageBox.Icon.Information, title, message, icon_path)

def show_warning(parent, title, message, icon_path="imgs/favicon.ico"):
    """显示警告提示框"""
    return show_message_with_icon(parent, QMessageBox.Icon.Warning, title, message, icon_path)

def show_error(parent, title, message, icon_path="imgs/favicon.ico"):
    """显示错误提示框"""
    return show_message_with_icon(parent, QMessageBox.Icon.Critical, title, message, icon_path)

def show_question(parent, title, message, icon_path="imgs/favicon.ico"):
    """显示询问对话框"""
    return show_message_with_icon(parent, QMessageBox.Icon.Question, title, message, icon_path)

def show_confirm_exit(parent, title="确认退出", message="正在处理，确定要退出吗？", icon_path="imgs/favicon.ico"):
    """显示确认退出对话框
    # 基本使用
    reply = show_confirm_exit(self)

    # 自定义消息
    reply = show_confirm_exit(self, "退出确认", "确定要关闭应用程序吗？")

    # 判断用户选择
    if reply == QMessageBox.StandardButton.Yes:
        # 用户选择退出
        pass

    """
    msg_box = QMessageBox(parent)
    # 设置当前的弹窗窗口始终保持在最顶层
    msg_box.setWindowFlags(msg_box.windowFlags() | Qt.WindowType.WindowStaysOnTopHint)

    # 添加自定义样式
    msg_box.setStyleSheet(QMESSAGEBOXSTYLE)

    # 设置窗口图标
    icon_full_path = get_resource_path(icon_path)
    if os.path.exists(icon_full_path):
        msg_box.setWindowIcon(QIcon(icon_full_path))

    msg_box.setIcon(QMessageBox.Icon.Question)
    msg_box.setWindowTitle(title)
    msg_box.setText(message)
    msg_box.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
    msg_box.setDefaultButton(QMessageBox.StandardButton.No)

    return msg_box.exec()

# 确认对话框, 这个会比上一个更加通用
def show_confirm(parent, title, message, icon_path="imgs/favicon.ico"):
    """显示确认对话框（Yes/No）

    Args:
        parent: 父窗口
        title: 对话框标题
        message: 对话框消息
        icon_path: 图标路径

    Returns:
        QMessageBox.StandardButton.Yes 或 QMessageBox.StandardButton.No

    Example:
        reply = show_confirm(self, "确认操作", "确定要执行此操作吗？")
        if reply == QMessageBox.StandardButton.Yes:
            # 用户确认
            pass
    """
    msg_box = QMessageBox(parent)
    # 设置当前的弹窗窗口始终保持在最顶层
    msg_box.setWindowFlags(msg_box.windowFlags() | Qt.WindowType.WindowStaysOnTopHint)

    # 添加自定义样式
    msg_box.setStyleSheet(QMESSAGEBOXSTYLE)

    # 设置窗口图标
    icon_full_path = get_resource_path(icon_path)
    if os.path.exists(icon_full_path):
        msg_box.setWindowIcon(QIcon(icon_full_path))

    msg_box.setIcon(QMessageBox.Icon.Question)
    msg_box.setWindowTitle(title)
    msg_box.setText(message)
    msg_box.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
    msg_box.setDefaultButton(QMessageBox.StandardButton.No)

    return msg_box.exec()

# 添加内存监控函数
def log_memory_usage(stage_name):
    try:
        process = psutil.Process(os.getpid())
        memory_info = process.memory_info()
        system_memory = psutil.virtual_memory()
        logger_manager.info(
            f"📊 [{stage_name}] 进程内存: {memory_info.rss // (1024 * 1024)}MB, "
            f"系统内存使用: {system_memory.percent}%, "
            f"可用: {system_memory.available // (1024 * 1024)}MB",
            "transcriber"
        )
    except Exception as e:
        logger_manager.info(f"📊 [{stage_name}] 无法获取内存信息: {e}", "transcriber")

# 添加 CPU 监控函数
def log_cpu_usage(stage_name):
    try:
        process = psutil.Process(os.getpid())
        # 获取进程 CPU 使用率（需要间隔时间计算）
        process_cpu = process.cpu_percent(interval=0.1)
        # 获取系统整体 CPU 使用率
        system_cpu = psutil.cpu_percent(interval=0.1)
        # 获取 CPU 核心数
        cpu_count = psutil.cpu_count()
        # 获取 CPU 频率信息
        cpu_freq = psutil.cpu_freq()

        freq_info = ""
        if cpu_freq:
            freq_info = f", 频率: {cpu_freq.current:.0f}MHz"

        logger_manager.info(
            f"🖥️ [{stage_name}] 进程CPU: {process_cpu:.1f}%, "
            f"系统CPU: {system_cpu:.1f}%, "
            f"核心数: {cpu_count}{freq_info}",
            "transcriber"
        )
    except Exception as e:
        logger_manager.info(f"🖥️ [{stage_name}] 无法获取CPU信息: {e}", "transcriber")


# 添加综合系统监控函数
def log_system_usage(stage_name):
    """综合监控内存和CPU使用情况"""
    try:
        process = psutil.Process(os.getpid())

        # 内存信息
        memory_info = process.memory_info()
        system_memory = psutil.virtual_memory()

        # CPU信息
        process_cpu = process.cpu_percent(interval=0.1)
        system_cpu = psutil.cpu_percent(interval=0.1)

        logger_manager.info(
            f"📊 [{stage_name}] 进程: 内存{memory_info.rss // (1024 * 1024)}MB, CPU{process_cpu:.1f}% | "
            f"系统: 内存{system_memory.percent:.1f}%, CPU{system_cpu:.1f}%",
            "transcriber"
        )
    except Exception as e:
        logger_manager.info(f"📊 [{stage_name}] 无法获取系统信息: {e}", "transcriber")


# 这个是专门用来给UI线程使用的格式化的内容
def get_system_monitor_info():
    """获取系统监控信息，返回格式化的字典"""
    try:
        process = psutil.Process(os.getpid())

        # 获取进程内存信息
        memory_info = process.memory_info()
        process_memory_mb = memory_info.rss // (1024 * 1024)
        process_memory_gb = process_memory_mb / 1024

        # 获取系统内存信息
        system_memory = psutil.virtual_memory()

        # 获取CPU信息
        process_cpu = process.cpu_percent(interval=0.1)
        system_cpu = psutil.cpu_percent(interval=0.1)

        # 格式化内存显示
        if process_memory_gb >= 1.0:
            memory_text = f"{process_memory_gb:.1f}G"
        else:
            memory_text = f"{process_memory_mb}M"

        return {
            'process_memory_text': memory_text,
            'process_cpu': process_cpu,
            'system_memory_percent': system_memory.percent,
            'system_cpu': system_cpu,
            'process_memory_mb': process_memory_mb,
            'system_memory_available_mb': system_memory.available // (1024 * 1024)
        }
    except Exception as e:
        return {'error': str(e)}


def get_image_base64(image_path=None):
    """将图片转换为base64格式"""
    if image_path is None:
        image_path = CUSTOMERSERVICE
    image_full_path = get_resource_path(image_path)
    try:
        if os.path.exists(image_full_path):
            with open(image_full_path, "rb") as img_file:
                img_data = img_file.read()
                img_base64 = base64.b64encode(img_data).decode('utf-8')
                service_img = f"data:image/jpeg;base64,{img_base64}"
    except Exception as e:
        print(f"加载客服图片失败: {e}")
        service_img = ""
    return service_img

# def get_customer_service_image_base64( ):
#     """从Qt资源中获取客服图片并转换为Base64"""
#     try:
#         # 从Qt资源系统读取图片
#         file = QFile(":/img/customer_service.png")
#         if file.open(QIODevice.ReadOnly):
#             image_data = file.readAll()
#             file.close()
#             # 转换为Base64
#             base64_data = base64.b64encode(image_data.data()).decode('utf-8')
#             return f"data:image/png;base64,{base64_data}"
#         else:
#             return ""
#     except Exception as e:
#         print(f"加载客服图片失败: {e}")
#         return ""

# 时间格式化函数
def format_timestamp(seconds):
    """格式化时间戳为HH:MM:SS,mmm"""
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    secs = int(seconds % 60)
    millis = int((seconds - int(seconds)) * 1000)
    return f"{hours:02}:{minutes:02}:{secs:02},{millis:03}"

def format_timestamp_seconds( seconds):
    """格式化时间戳为HH:MM:SS"""
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    secs = int(seconds % 60)
    return f"{hours:02}:{minutes:02}:{secs:02}"

def setup_label_icon(label, icon_path="imgs/favicon.ico"):
    """为QLabel设置图标"""
    from PySide6.QtGui import QPixmap
    icon_full_path = get_resource_path(icon_path)
    if os.path.exists(icon_full_path):
        pixmap = QPixmap(icon_full_path)
        # 根据Label大小调整图片
        if not label.size().isEmpty():
            # KeepAspectRatio = 1, SmoothTransformation = 1  使用这两个也可以
            scaled_pixmap = pixmap.scaled(label.size(), Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
            label.setPixmap(scaled_pixmap)
        else:
            label.setPixmap(pixmap)
    else:
        print(f"Warning: Icon file not found: {icon_full_path}")

def get_network_speed():
    """获取网络速度信息"""
    try:
        # 获取网络IO统计信息
        net_io_1 = psutil.net_io_counters()
        time.sleep(1)  # 等待1秒
        net_io_2 = psutil.net_io_counters()
        
        # 计算1秒内的数据传输量
        bytes_sent = net_io_2.bytes_sent - net_io_1.bytes_sent
        bytes_recv = net_io_2.bytes_recv - net_io_1.bytes_recv
        
        # 转换为更易读的单位
        def format_bytes(bytes_value):
            """将字节转换为易读格式"""
            if bytes_value < 1024:
                return f"{bytes_value} B/s"
            elif bytes_value < 1024 * 1024:
                return f"{bytes_value / 1024:.1f} KB/s"
            elif bytes_value < 1024 * 1024 * 1024:
                return f"{bytes_value / (1024 * 1024):.1f} MB/s"
            else:
                return f"{bytes_value / (1024 * 1024 * 1024):.1f} GB/s"
        
        return {
            'upload_speed': format_bytes(bytes_sent),
            'download_speed': format_bytes(bytes_recv),
            'upload_bytes_per_sec': bytes_sent,
            'download_bytes_per_sec': bytes_recv
        }
    except Exception as e:
        return {'error': str(e)}

def get_system_monitor_info_with_network():
    """获取包含网速的完整系统监控信息"""
    try:
        # 获取基础系统信息
        system_info = get_system_monitor_info()
        
        # 获取网速信息
        network_info = get_network_speed()
        
        # 合并信息
        if 'error' not in system_info and 'error' not in network_info:
            system_info.update(network_info)
        elif 'error' in network_info:
            # 如果网速获取失败，添加默认值
            system_info.update({
                'upload_speed': '0 B/s',
                'download_speed': '0 B/s',
                'upload_bytes_per_sec': 0,
                'download_bytes_per_sec': 0,
                'network_error': network_info['error']
            })
        
        return system_info
    except Exception as e:
        return {'error': str(e)}

# 设置高DPI支持，必须在创建QApplication之前调用
def setup_high_dpi_support():
    """设置高DPI支持，必须在创建QApplication之前调用"""
    try:
        # 启用高DPI缩放支持 (Qt 5.6+)
        QApplication.setAttribute(Qt.ApplicationAttribute.AA_EnableHighDpiScaling, True)

        # 启用高DPI像素图支持 (Qt 5.14+)
        QApplication.setAttribute(Qt.ApplicationAttribute.AA_UseHighDpiPixmaps, True)

        # 禁用窗口上下文帮助按钮 (检查属性是否存在)
        try:
            if hasattr(Qt.ApplicationAttribute, 'AA_DisableWindowContextHelpButton'):
                QApplication.setAttribute(Qt.ApplicationAttribute.AA_DisableWindowContextHelpButton, True)
        except AttributeError:
            # 如果属性不存在，忽略这个设置
            pass

        # 设置高DPI缩放因子舍入策略 (Qt 5.14+)
        try:
            if hasattr(Qt, 'HighDpiScaleFactorRoundingPolicy'):
                QApplication.setHighDpiScaleFactorRoundingPolicy(
                    Qt.HighDpiScaleFactorRoundingPolicy.PassThrough
                )
        except AttributeError:
            # 如果Qt版本较老，忽略这些设置
            pass

        print("✅ 高DPI支持设置完成")
        return True

    except Exception as e:
        print(f"⚠️ 高DPI支持设置失败: {e}")
        return False



def draw_subtitle_lines(painter, width, height, top_position, bottom_position):
    """绘制字幕上下边线（公共函数，供各 overlay 的 paintEvent 调用）

    Args:
        painter: QPainter 实例
        width: 绘制区域宽度
        height: 绘制区域高度
        top_position: 上边线百分比 (0-100)
        bottom_position: 下边线百分比 (0-100)
    """
    if width <= 0 or height <= 0:
        return
    from PySide6.QtCore import QRect
    from PySide6.QtGui import QColor, QPen, QFont
    top_y = int(height * top_position / 100.0)
    bottom_y = int(height * bottom_position / 100.0)
    highlight_rect = QRect(0, top_y, width, max(0, bottom_y - top_y))
    painter.fillRect(highlight_rect, QColor(124, 59, 237, 30))
    painter.setPen(QPen(QColor("#7C3BED"), 2))
    painter.drawLine(0, top_y, width, top_y)
    painter.drawLine(0, bottom_y, width, bottom_y)
    draw_subtitle_handle(painter, width // 2, top_y, True, top_position)
    draw_subtitle_handle(painter, width // 2, bottom_y, False, bottom_position)


def draw_subtitle_handle(painter, x, y, is_top, pct_value):
    """绘制字幕线手柄标签"""
    from PySide6.QtCore import Qt
    from PySide6.QtGui import QColor, QFont
    label_w = 130
    label_h = 20
    label_y = max(0, min(y - label_h // 2, painter.device().height() - label_h))
    label_x = max(0, (painter.device().width() - label_w) // 2)
    painter.fillRect(label_x, label_y, label_w, label_h, QColor("#7C3BED"))
    font = QFont("Microsoft YaHei", 9, QFont.Normal)
    painter.setFont(font)
    painter.setPen(QColor("#FFFFFF"))
    pct_str = f"{int(pct_value)}%"
    text = f"{'上' if is_top else '下'}边缘 {pct_str}"
    painter.drawText(label_x + 8, label_y + label_h - 5, text)



