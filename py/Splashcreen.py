#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------------
# @Time    : 2025/9/26 17:36
# @Author  : WXY
# @File    : Splashcreen
# @PROJECT_NAME: youtubedown_gui
# @PRODUCT_NAME: PyCharm
# -------------------------------------------------------------------------------
import sys
import os
from PySide6.QtWidgets import QMainWindow, QApplication
from PySide6.QtCore import QTimer, Qt, Signal
from PySide6.QtGui import QPixmap, QPainter, QPainterPath, QRegion
from py_gui.splashscreen_ui import Ui_splashscreen

# 尝试导入资源文件，如果失败则跳过
try:
    from py_gui import resouce_rc
except ImportError:
    pass

from utils import setup_label_icon, VERSION, setup_high_dpi_support, setup_window_title,setup_window_icon
from SettingsManager import settings_manager
from datetime import datetime, timedelta
from LoggerManager import logger_manager


class SplashScreen(QMainWindow):
    finished = Signal()

    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.WindowStaysOnTopHint)

        self.ui = Ui_splashscreen()
        self.ui.setupUi(self)

        self.ui.closeButton.clicked.connect(QApplication.quit)

        self._drag_pos = None

        try:
            setup_window_icon(self)
        except Exception as e:
            logger_manager.warning(f"设置窗口图标失败: {e}", "splash_screen")

        try:
            setup_window_title(self)
        except Exception as e:
            logger_manager.warning(f"设置窗口标题失败: {e}", "splash_screen")

        self.set_rounded_corners()
        self.setup_safe_texts()
        self.setup_logo()

        self.progress_value = 0
        self.progress_messages = [
            (20, "加载配置中..."),
            (50, "初始化模块中..."),
            (80, "准备界面中..."),
            (100, "启动完成")
        ]

        self.progress_timer = QTimer(self)
        self.progress_timer.timeout.connect(self.advance_progress)

        self.timer = QTimer(self)
        self.timer.setSingleShot(True)
        self.timer.timeout.connect(self.finish_splash)

        logger_manager.info("启动界面初始化完成", "splash_screen")

    def showEvent(self, event):
        """窗口显示事件"""
        super().showEvent(event)
        self.set_rounded_corners()
        # 这里取一个随机数, 从10 - 20 之间随机取一个随机整数
        # 然后赋值给 start(10)
        import random

        num = random.randint(10, 20)
        self.progress_timer.start(num) # 进度条的进度, 10ms触发一次的话, 大概就是1.3 - 2s左右加载完

    def resizeEvent(self, event):
        """窗口大小改变事件"""
        super().resizeEvent(event)
        self.set_rounded_corners()

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self._drag_pos = event.globalPosition().toPoint() - self.frameGeometry().topLeft()
            event.accept()

    def mouseMoveEvent(self, event):
        if self._drag_pos is not None and event.buttons() == Qt.MouseButton.LeftButton:
            self.move(event.globalPosition().toPoint() - self._drag_pos)
            event.accept()

    def set_rounded_corners(self):
        """设置圆角"""
        if not self.isVisible():
            return
        try:
            radius = 15
            path = QPainterPath()
            path.addRoundedRect(self.rect(), radius, radius)
            region = QRegion(path.toFillPolygon().toPolygon())
            self.setMask(region)
        except Exception as e:
            logger_manager.error(f"设置圆角失败: {e}", "splash_screen")

    def get_logo_path(self):
        """获取Logo图片的正确路径"""
        try:
            # 在打包环境下
            if getattr(sys, 'frozen', False):
                # 从 _MEIPASS 获取
                logo_path = os.path.join(sys._MEIPASS, 'imgs', 'logo.png')
                if os.path.exists(logo_path):
                    return logo_path
            else:
                # 开发环境下的多个可能路径
                current_dir = os.path.dirname(os.path.abspath(__file__))
                possible_paths = [
                    os.path.join(os.path.dirname(current_dir), 'imgs', 'logo.png'),  # ../imgs/logo.png
                    os.path.join(current_dir, 'imgs', 'logo.png'),  # ./imgs/logo.png
                    "imgs/logo.png",  # 相对路径
                ]
                
                for path in possible_paths:
                    if os.path.exists(path):
                        return path
            
            return None
        except Exception as e:
            logger_manager.error(f"获取Logo路径失败: {e}", "splash_screen")
            return None

    def setup_safe_texts(self):
        """设置安全的文本内容"""
        try:
            self.ui.subTitleLabel.setText("正在准备字幕长图引擎...")
            self.ui.statusLabel.setText("初始化组件中 · 请稍候")
            self.ui.loadingProgressBar.setValue(0)
        except Exception as e:
            logger_manager.error(f"设置安全文本失败: {e}", "splash_screen")

    def create_rounded_pixmap(self, pixmap, size):
        """创建圆角图片"""
        try:
            # 创建一个透明的图片
            rounded_pixmap = QPixmap(size)
            rounded_pixmap.fill(Qt.GlobalColor.transparent)

            # 创建画家
            painter = QPainter(rounded_pixmap)
            painter.setRenderHint(QPainter.RenderHint.Antialiasing)

            # 创建圆角路径
            path = QPainterPath()
            path.addRoundedRect(0, 0, size.width(), size.height(), 5, 5)

            # 设置裁剪路径
            painter.setClipPath(path)

            # 绘制缩放后的图片
            scaled_pixmap = pixmap.scaled(size, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
            painter.drawPixmap(0, 0, scaled_pixmap)

            painter.end()
            return rounded_pixmap

        except Exception as e:
            logger_manager.error(f"创建圆角图片失败: {e}", "splash_screen")
            return pixmap

    def setup_logo(self):
        """设置Logo图片"""
        try:
            # 首先尝试从Qt资源系统加载
            try:
                pixmap = QPixmap(":/img/logo.png")
                if not pixmap.isNull():
                    # 创建圆角图片
                    rounded_pixmap = self.create_rounded_pixmap(pixmap, self.ui.logoLabel.size())
                    self.ui.logoLabel.setPixmap(rounded_pixmap)
                    self.ui.logoLabel.setStyleSheet("border-radius: 5px;")
                    return
            except Exception:
                pass

            # 如果资源加载失败，尝试加载本地文件
            logo_path = self.get_logo_path()
            if logo_path and os.path.exists(logo_path):
                pixmap = QPixmap(logo_path)
                if not pixmap.isNull():
                    # 创建圆角图片
                    rounded_pixmap = self.create_rounded_pixmap(pixmap, self.ui.logoLabel.size())
                    self.ui.logoLabel.setPixmap(rounded_pixmap)
                    self.ui.logoLabel.setStyleSheet("border-radius: 5px;")
                    logger_manager.info(f"Logo从本地路径加载成功: {logo_path}", "splash_screen")
                    return

            # 如果都失败了，使用emoji作为备用
            logger_manager.warning("Logo图片加载失败，使用默认图标", "splash_screen")
            self.ui.logoLabel.setText("🎬")
            self.ui.logoLabel.setStyleSheet("""
                QLabel {
                    color: white;
                    font-size: 32px;
                    border-radius: 5px;
                }
            """)

        except Exception as e:
            logger_manager.error(f"设置Logo失败: {e}", "splash_screen")
            # 最终备用方案
            self.ui.logoLabel.setText("🎬")
            self.ui.logoLabel.setStyleSheet("""
                QLabel {
                    color: white;
                    font-size: 32px;
                    border-radius: 5px;
                }
            """)

    def advance_progress(self):
        try:
            if self.progress_value >= 100:
                self.progress_timer.stop()
                self.on_loading_finished()
                return

            self.progress_value += 1
            self.ui.loadingProgressBar.setValue(self.progress_value)

            current_text = "初始化组件中 · 请稍候"
            for threshold, message in self.progress_messages:
                if self.progress_value <= threshold:
                    current_text = message
                    break
            self.ui.statusLabel.setText(current_text)

        except Exception as e:
            logger_manager.error(f"推进进度失败: {e}", "splash_screen")

    def on_loading_finished(self):
        """加载完成"""
        try:
            self.ui.statusLabel.setText("启动完成")
            self.timer.start(300)
        except Exception as e:
            logger_manager.error(f"加载完成处理失败: {e}", "splash_screen")

    def finish_splash(self):
        try:
            self.timer.stop()
            self.finished.emit()
        except Exception as e:
            logger_manager.error(f"结束启动页失败: {e}", "splash_screen")


def main():
    """主函数"""
    # ✅ 在创建QApplication之前设置高DPI支持
    setup_high_dpi_support()
    
    app = QApplication(sys.argv)

    # 设置应用程序信息
    app.setApplicationName("拼字幕")
    app.setApplicationVersion(VERSION)

    try:
        splash = SplashScreen()
        splash.show()

        # 运行应用程序
        sys.exit(app.exec())

    except Exception as e:
        logger_manager.error(f"启动界面运行错误: {e}", "splash_screen")
        print(f"❌ 启动界面运行错误: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()