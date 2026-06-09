#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------------
# @Time    : 2026/5/27 14:47
# @Author  : WXY
# @File    : Subtitleline.py
# @PRODUCT_NAME: PyCharm
# -------------------------------------------------------------------------------
import os

from PySide6.QtCore import QEvent, QPoint, QRect, QUrl, QTimer, Qt
from PySide6.QtGui import QPainter, QPen, QColor, QFont, QPixmap, QIcon
from PySide6.QtWidgets import (
    QMainWindow, QFrame, QVBoxLayout, QGraphicsScene, QGraphicsPixmapItem,
    QGraphicsView,
)
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from PySide6.QtMultimediaWidgets import QVideoWidget
from py_gui.subtitleline_ui import Ui_MainWindow
from py.utils import TOP_POSITION, BOTTOM_POSITION, setup_window_icon, COPYRIGHT, get_project_root, setup_window_title


class _SubtitleOverlay(QFrame):
    """独立顶级窗口，透明背景，手动跟随 previewArea 位置。
    使用 Qt.Tool + WA_TranslucentBackground 让它浮在所有窗口上方。
    """

    def __init__(self, parent=None):
        super().__init__(
            parent,
            Qt.WindowType.Tool | Qt.WindowType.FramelessWindowHint | Qt.WindowType.WindowStaysOnTopHint,
        )
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground, True)
        self.setAttribute(Qt.WidgetAttribute.WA_TransparentForMouseEvents, False)
        self.setMouseTracking(True)
        self._top_position = TOP_POSITION
        self._bottom_position = BOTTOM_POSITION

    def set_positions(self, top_pct, bottom_pct):
        self._top_position = top_pct
        self._bottom_position = bottom_pct
        self.update()

    def get_positions(self):
        return (self._top_position, self._bottom_position)

    def paintEvent(self, event):
        w = self.width()
        h = self.height()
        if w <= 0 or h <= 0:
            return
        painter = QPainter(self)
        if not painter.isActive():
            return
        painter.setRenderHint(QPainter.Antialiasing)
        
        # 【调试】先画一个红色半透明背景，确认 overlay 是否显示
        painter.fillRect(0, 0, w, h, QColor(255, 0, 0, 100))
        
        top_y = int(h * self._top_position / 100.0)
        bottom_y = int(h * self._bottom_position / 100.0)
        highlight_rect = QRect(0, top_y, w, max(0, bottom_y - top_y))
        painter.fillRect(highlight_rect, QColor(124, 59, 237, 30))
        painter.setPen(QPen(QColor("#7C3BED"), 2))
        painter.drawLine(0, top_y, w, top_y)
        painter.drawLine(0, bottom_y, w, bottom_y)
        self._draw_handle(painter, w // 2, top_y, True, self._top_position)
        self._draw_handle(painter, w // 2, bottom_y, False, self._bottom_position)

    def _draw_handle(self, painter, x, y, is_top, pct_value):
        label_w = 130
        label_h = 20
        label_y = y - label_h // 2
        label_y = max(0, min(self.height() - label_h, label_y))
        label_x = max(0, (self.width() - label_w) // 2)
        painter.fillRect(label_x, label_y, label_w, label_h, QColor("#7C3BED"))
        font = QFont("Microsoft YaHei", 9, QFont.Normal)
        painter.setFont(font)
        painter.setPen(Qt.white)
        pct_str = f"{int(pct_value)}%"
        text = f"{'上' if is_top else '下'}边缘 {pct_str}"
        painter.drawText(label_x + 8, label_y + label_h - 5, text)


class Subtitleline(QMainWindow):
    def __init__(self, main_window=None, image_path=None, video_path=None):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        setup_window_icon(self)
        setup_window_title(self)
        self.main_window = main_window
        self.image_path = image_path
        self.video_path = video_path
        self._project_dir = get_project_root()
        self._top_position = TOP_POSITION
        self._bottom_position = BOTTOM_POSITION
        self._is_video_mode = bool(video_path)
        self._is_playing = False
        self._duration = 0
        self._media_player = None
        self._audio_output = None
        self._dragging = None
        self._overlay = None
        self._init_paths()
        self._init_ui()
        self._load_positions()
        self._setup_preview()

    def _init_paths(self):
        self.play_icon_path = os.path.join(self._project_dir, "imgs", "play.png")
        self.pause_icon_path = os.path.join(self._project_dir, "imgs", "pause.png")

    def _init_ui(self):
        self.ui.btnRestart.clicked.connect(self._back_to_main_window)
        self.ui.btnResetDefault.clicked.connect(self._reset_to_default)
        self.ui.btnBack.clicked.connect(self._back_to_main_window)
        self.ui.btnContinue.clicked.connect(self._on_continue)
        self.ui.btnPlayPause.clicked.connect(self._toggle_play_pause)
        self.ui.sliderVideoProgress.sliderMoved.connect(self._on_slider_moved)
        self._update_play_button_icon()
        if not self._is_video_mode:
            self.ui.btnPlayPause.setVisible(False)
            self.ui.sliderVideoProgress.setVisible(False)
            self.ui.labelVideoTime.setVisible(False)

    def _setup_preview(self):
        if self._is_video_mode and self.video_path:
            self._setup_video_preview()
        elif self.image_path and os.path.exists(self.image_path):
            self._setup_image_preview()
        self._create_overlay()
        self.ui.overlayPanel.hide()

    def _setup_video_preview(self):
        self._video_widget = QVideoWidget()
        self._video_widget.setStyleSheet("background-color: #000000; border: none;")
        layout = self.ui.videoContainer.layout()
        if layout is None:
            layout = QVBoxLayout(self.ui.videoContainer)
            layout.setContentsMargins(0, 0, 0, 0)
            layout.setSpacing(0)
        layout.addWidget(self._video_widget)
        self._audio_output = QAudioOutput(self)
        self._media_player = QMediaPlayer(self)
        self._media_player.setVideoOutput(self._video_widget)
        self._media_player.setAudioOutput(self._audio_output)
        self._audio_output.setMuted(False)
        self._media_player.setSource(QUrl.fromLocalFile(self.video_path))
        self._media_player.positionChanged.connect(self._on_position_changed)
        self._media_player.durationChanged.connect(self._on_duration_changed)
        self._media_player.play()
        self._media_player.pause()

    def _setup_image_preview(self):
        pixmap = QPixmap(self.image_path)
        if pixmap.isNull():
            return
        scaled = pixmap.scaled(
            self.ui.previewArea.size(),
            Qt.KeepAspectRatio,
            Qt.SmoothTransformation,
        )
        self._pixmap_item = QGraphicsPixmapItem(scaled)
        scene = QGraphicsScene(self)
        scene.addItem(self._pixmap_item)
        self._graphics_view = _PreviewGraphicsView(self.ui.videoContainer)
        self._graphics_view.setScene(scene)
        self._graphics_view.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self._graphics_view.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        layout = QVBoxLayout(self.ui.videoContainer)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        layout.addWidget(self._graphics_view)
        self._scene = scene
        self._update_pixmap_position()

    def _create_overlay(self):
        self._overlay = _SubtitleOverlay()
        self._overlay.set_positions(self._top_position, self._bottom_position)
        self._overlay.installEventFilter(self)
        # 不在此处 show，等 showEvent 触发后再同步坐标并显示

    def _sync_overlay_geometry(self):
        if not self._overlay or not self.ui.previewArea.isVisible():
            return
        global_pos = self.ui.previewArea.mapToGlobal(QPoint(0, 0))
        w = self.ui.previewArea.width()
        h = self.ui.previewArea.height()
        print(f"[Overlay Sync] previewArea global_pos=({global_pos.x()}, {global_pos.y()}), size=({w}x{h})")
        self._overlay.setGeometry(
            global_pos.x(),
            global_pos.y(),
            w,
            h
        )

    def _update_pixmap_position(self):
        if not hasattr(self, "_graphics_view") or not self._pixmap_item:
            return
        area = self.ui.previewArea
        pix = self._pixmap_item.pixmap()
        if pix.isNull():
            return
        avail_w = area.width()
        avail_h = area.height()
        if avail_w <= 0 or avail_h <= 0:
            return
        scaled = pix.scaled(avail_w, avail_h, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self._pixmap_item.setPixmap(scaled)
        x = (avail_w - scaled.width()) // 2
        y = (avail_h - scaled.height()) // 2
        self._pixmap_item.setOffset(x, y)
        self._scene.setSceneRect(0, 0, avail_w, avail_h)

    def showEvent(self, event):
        super().showEvent(event)
        if self._overlay:
            QTimer.singleShot(0, self._show_overlay_delayed)
            QTimer.singleShot(100, self._show_overlay_delayed)

    def _show_overlay_delayed(self):
        if self._overlay:
            self._sync_overlay_geometry()
            self._overlay.show()
            self._overlay.raise_()

    def moveEvent(self, event):
        super().moveEvent(event)
        self._sync_overlay_geometry()

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self._update_pixmap_position()
        self._sync_overlay_geometry()

    def closeEvent(self, event):
        if self._overlay:
            self._overlay.hide()
            self._overlay.deleteLater()
            self._overlay = None
        super().closeEvent(event)

    def eventFilter(self, watched, event):
        if watched == self._overlay:
            et = event.type()
            if et == QEvent.Type.MouseMove:
                self._on_overlay_mouse_move(event.pos())
                return True
            elif et == QEvent.Type.MouseButtonPress:
                self._on_overlay_mouse_press(event.pos())
                return True
            elif et == QEvent.Type.MouseButtonRelease:
                self._on_overlay_mouse_release()
                return True
        return super().eventFilter(watched, event)

    def _get_pct_from_y(self, y):
        if not self._overlay:
            return 0.0
        h = self._overlay.height()
        if h <= 0:
            return 0.0
        return max(0.0, min(100.0, y / h * 100.0))

    def _on_overlay_mouse_move(self, pos):
        if not self._overlay:
            return
        if self._dragging:
            pct = self._get_pct_from_y(pos.y())
            if self._dragging == "top":
                if pct >= self._bottom_position - 5:
                    pct = self._bottom_position - 5
                self._top_position = max(0.0, pct)
            else:
                if pct <= self._top_position + 5:
                    pct = self._top_position + 5
                self._bottom_position = min(100.0, pct)
            self._overlay.set_positions(self._top_position, self._bottom_position)
            self._save_positions()
            self._update_info_label()
        else:
            near_top = abs(pos.y() - int(self._overlay.height() * self._top_position / 100.0)) <= 10
            near_bottom = abs(pos.y() - int(self._overlay.height() * self._bottom_position / 100.0)) <= 10
            if near_top or near_bottom:
                self._overlay.setCursor(Qt.SizeVerCursor)
            else:
                self._overlay.unsetCursor()

    def _on_overlay_mouse_press(self, pos):
        if not self._overlay:
            return
        top_y = int(self._overlay.height() * self._top_position / 100.0)
        bottom_y = int(self._overlay.height() * self._bottom_position / 100.0)
        if abs(pos.y() - top_y) <= 10:
            self._dragging = "top"
            self._overlay.setCursor(Qt.SizeVerCursor)
        elif abs(pos.y() - bottom_y) <= 10:
            self._dragging = "bottom"
            self._overlay.setCursor(Qt.SizeVerCursor)

    def _on_overlay_mouse_release(self):
        self._dragging = None
        if self._overlay:
            self._overlay.unsetCursor()

    def _update_info_label(self):
        height_pct = max(0, int(self._bottom_position - self._top_position))
        self.ui.labelAreaHeight.setText(
            f"字幕区域高度：{height_pct}% · 位置已自动保存"
        )

    def _save_positions(self):
        from PySide6.QtCore import QSettings
        settings = QSettings("pinzimu", "pinzimu_gui")
        settings.setValue("subtitle_line_top", str(int(self._top_position)))
        settings.setValue("subtitle_line_bottom", str(int(self._bottom_position)))

    def _load_positions(self):
        from PySide6.QtCore import QSettings
        settings = QSettings("pinzimu", "pinzimu_gui")
        top_default = str(int(TOP_POSITION))
        bottom_default = str(int(BOTTOM_POSITION))
        saved_top = settings.value("subtitle_line_top", top_default)
        saved_bottom = settings.value("subtitle_line_bottom", bottom_default)
        try:
            self._top_position = float(saved_top)
            self._bottom_position = float(saved_bottom)
        except (ValueError, TypeError):
            self._top_position = TOP_POSITION
            self._bottom_position = BOTTOM_POSITION
        self._top_position = max(0.0, min(100.0, self._top_position))
        self._bottom_position = max(0.0, min(100.0, self._bottom_position))
        if self._bottom_position <= self._top_position + 5:
            self._top_position = TOP_POSITION
            self._bottom_position = BOTTOM_POSITION
        self._update_info_label()

    def _reset_to_default(self):
        self._top_position = TOP_POSITION
        self._bottom_position = BOTTOM_POSITION
        if self._overlay:
            self._overlay.set_positions(self._top_position, self._bottom_position)
        self._save_positions()
        self._update_info_label()

    def _back_to_main_window(self):
        if self._media_player:
            self._media_player.stop()
        if self._overlay:
            self._overlay.hide()
            self._overlay.deleteLater()
            self._overlay = None
        self.hide()
        if self.main_window is not None:
            self.main_window.show()
            self.main_window.raise_()
            self.main_window.activateWindow()
        self.deleteLater()

    def _on_continue(self):
        pass

    def _update_play_button_icon(self):
        if self._is_playing and os.path.exists(self.pause_icon_path):
            self.ui.btnPlayPause.setIcon(QIcon(self.pause_icon_path))
        elif os.path.exists(self.play_icon_path):
            self.ui.btnPlayPause.setIcon(QIcon(self.play_icon_path))

    def _toggle_play_pause(self):
        if not self._media_player:
            return
        if self._is_playing:
            self._media_player.pause()
            self._is_playing = False
        else:
            self._media_player.play()
            self._is_playing = True
        self._update_play_button_icon()

    def _on_position_changed(self, position):
        if self._duration <= 0:
            return
        current_seconds = position / 1000.0
        self.ui.sliderVideoProgress.blockSignals(True)
        self.ui.sliderVideoProgress.setValue(int(current_seconds))
        self.ui.sliderVideoProgress.blockSignals(False)
        self.ui.labelVideoTime.setText(
            f"{self._format_time(current_seconds)} / {self._format_time(self._duration)}"
        )

    def _on_duration_changed(self, duration):
        self._duration = duration / 1000.0
        self.ui.sliderVideoProgress.setRange(0, max(1, int(self._duration)))
        self.ui.labelVideoTime.setText(
            f"0:00 / {self._format_time(self._duration)}"
        )

    def _on_slider_moved(self, value):
        if self._media_player:
            self._media_player.setPosition(value * 1000)

    def _format_time(self, seconds):
        total = int(round(seconds))
        m = total // 60
        s = total % 60
        return f"{m}:{s:02d}"

    def get_positions(self):
        return (self._top_position, self._bottom_position)


class _PreviewGraphicsView(QGraphicsView):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAttribute(Qt.WA_TransparentForMouseEvents, True)
        self.setStyleSheet("background: transparent; border: none;")
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
