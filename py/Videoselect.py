#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------------
# @Time    : 2026/5/26 14:47
# @Author  : WXY
# @File    : Videoselect.py
# @PROJECT_NAME: 20260525_pinzimu_gui
# @PRODUCT_NAME: PyCharm
# -------------------------------------------------------------------------------
import json
import os
import subprocess

import re
import shutil

from PySide6.QtCore import QUrl, QRect, Qt, QEvent, QPoint, QTimer, QThread, Signal
from PySide6.QtGui import QIcon, QPainter, QPen, QColor, QFont
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from PySide6.QtMultimediaWidgets import QVideoWidget
from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QFrame
from py_gui.videoselect_ui import Ui_fileselect
from py.utils import TOP_POSITION, BOTTOM_POSITION, setup_window_icon, COPYRIGHT, get_project_root, setup_window_title, get_max_video_frames
from py.video_geometry import (
    clamp_end_time,
    clamp_start_time,
    container_pct_to_video_pct,
    video_content_rect,
)


SUBTITLE_POSITION_COORDINATE_VERSION = 2


class Videoselect(QMainWindow):
    def __init__(self, video_path=None, main_window=None):
        super().__init__()
        self._overlay = None
        self._dragging = None
        self.media_player = None
        self.audio_output = None
        self.ui = Ui_fileselect()
        self.ui.setupUi(self)
        setup_window_icon(self)
        setup_window_title(self)
        self.video_path = video_path
        self.main_window = main_window
        self._project_dir = get_project_root()
        self.ffprobe_path = self._get_ffprobe_path()
        self.duration = 0
        self.start_time = 0
        self.end_time = 0
        self.is_playing = False
        self._is_muted = True
        self._top_position = TOP_POSITION
        self._bottom_position = BOTTOM_POSITION
        self._positions_need_migration = False
        self._init_paths()
        self._init_ui()
        self._setup_video_widget()
        self._load_video_info()
        self._init_media_player()
        self._load_positions()
        self._create_overlay()

    def _init_paths(self):
        self.play_icon_path = os.path.join(self._project_dir, "imgs", "play.png")
        self.pause_icon_path = os.path.join(self._project_dir, "imgs", "pause.png")
        self.mute_icon_path = os.path.join(self._project_dir, "imgs", "mute.png")
        self.sound_icon_path = os.path.join(self._project_dir, "imgs", "sound.png")

    def _init_ui(self):
        if os.path.exists(self.play_icon_path):
            self.ui.btnPlayPause.setIcon(QIcon(self.play_icon_path))
        if os.path.exists(self.mute_icon_path):
            self.ui.btnAudioPlayPause.setIcon(QIcon(self.mute_icon_path))
        self.ui.btnRestart.clicked.connect(self._back_to_main_window)
        self.ui.btnPlayPause.clicked.connect(self._toggle_play_pause)
        self.ui.btnAudioPlayPause.clicked.connect(self._toggle_mute)
        self.ui.btnSetStartCurrent.clicked.connect(self._set_start_from_current)
        self.ui.btnSetEndCurrent.clicked.connect(self._set_end_from_current)
        self.ui.sliderCurrentTime.valueChanged.connect(self._on_slider_moved)
        self.ui.sliderStartTime.valueChanged.connect(self._on_start_slider_moved)
        self.ui.sliderEndTime.valueChanged.connect(self._on_end_slider_moved)
        self.ui.btnStartExtract.clicked.connect(self._start_extract)
        self.ui.btnBackToMain.clicked.connect(self._back_to_main_window)

    def _get_ffprobe_path(self):
        ffprobe_path = os.path.join(self._project_dir, "utils", "ffmpeg", "ffprobe.exe")
        return ffprobe_path if os.path.exists(ffprobe_path) else None

    def _get_ffmpeg_path(self):
        ffmpeg_path = os.path.join(self._project_dir, "utils", "ffmpeg", "ffmpeg.exe")
        return ffmpeg_path if os.path.exists(ffmpeg_path) else None

    def _setup_video_widget(self):
        area = self.ui.videoAreaFrame
        layout = area.layout()
        if layout:
            while layout.count() > 0:
                layout.takeAt(0)
        else:
            layout = QVBoxLayout(area)
            layout.setContentsMargins(0, 0, 0, 0)
            layout.setSpacing(0)

        self.video_widget = QVideoWidget()
        self.video_widget.setAspectRatioMode(Qt.AspectRatioMode.KeepAspectRatio)
        self.video_widget.setStyleSheet("background-color: #000000; border: none;")
        layout.addWidget(self.video_widget)
        self.video_widget.videoSink().videoSizeChanged.connect(
            self._sync_overlay_geometry
        )

    def _load_video_info(self):
        if not self.video_path or not self.ffprobe_path:
            return
        try:
            result = subprocess.run(
                [
                    self.ffprobe_path,
                    "-v", "error",
                    "-select_streams", "v:0",
                    "-show_entries", "stream=nb_frames,duration,r_frame_rate:format=duration",
                    "-of", "json",
                    self.video_path,
                ],
                capture_output=True,
                text=True,
                encoding="utf-8",
                errors="ignore",
                creationflags=subprocess.CREATE_NO_WINDOW,
                check=True,
            )
            info = json.loads(result.stdout or "{}")
            self.duration = self._get_duration(info)
            self.end_time = self.duration
            frame_count = self._get_frame_count(info)
            fps = self._get_fps(info)
            self.ui.labelExtractSubtitle.setText(os.path.basename(self.video_path))
            self.ui.labelVideoInfo.setText(
                f"时长: {self._format_duration(self.duration)}  | 帧率: {fps}fps | 帧数: {frame_count if frame_count is not None else '--'}"
            )
            self._update_time_display()
            self._update_sliders_range()
        except Exception:
            self.ui.labelExtractSubtitle.setText("")
            self.ui.labelVideoInfo.setText("时长: --:--  | 帧率: --fps | 帧数: --")

    def _init_media_player(self):
        if not self.video_path:
            return
        self.audio_output = QAudioOutput(self)
        self.media_player = QMediaPlayer(self)
        self.media_player.setSource(QUrl.fromLocalFile(self.video_path))
        self.media_player.setVideoOutput(self.video_widget)
        self.media_player.setAudioOutput(self.audio_output)
        self.audio_output.setMuted(self._is_muted)
        self.media_player.positionChanged.connect(self._on_position_changed)
        self.media_player.durationChanged.connect(self._on_duration_changed)
        self.media_player.mediaStatusChanged.connect(self._on_media_status_changed)
        self.media_player.errorOccurred.connect(self._on_media_error)
        self.media_player.play()
        self.media_player.pause()

    def _on_media_error(self, error, error_string):
        pass

    def _toggle_play_pause(self):
        if not self.media_player:
            return
        if self.is_playing:
            self.media_player.pause()
            self.is_playing = False
            if os.path.exists(self.play_icon_path):
                self.ui.btnPlayPause.setIcon(QIcon(self.play_icon_path))
        else:
            self.media_player.play()
            self.is_playing = True
            if os.path.exists(self.pause_icon_path):
                self.ui.btnPlayPause.setIcon(QIcon(self.pause_icon_path))

    def _toggle_mute(self):
        if not self.audio_output:
            return
        self._is_muted = not self._is_muted
        self.audio_output.setMuted(self._is_muted)
        if self._is_muted:
            if os.path.exists(self.mute_icon_path):
                self.ui.btnAudioPlayPause.setIcon(QIcon(self.mute_icon_path))
        else:
            if os.path.exists(self.sound_icon_path):
                self.ui.btnAudioPlayPause.setIcon(QIcon(self.sound_icon_path))

    def _on_position_changed(self, position):
        if self.duration <= 0:
            return
        current_seconds = position / 1000.0
        self.ui.sliderCurrentTime.blockSignals(True)
        self.ui.sliderCurrentTime.setValue(int(current_seconds))
        self.ui.sliderCurrentTime.blockSignals(False)
        self._update_time_display(current_seconds)

    def _on_duration_changed(self, duration):
        self.duration = duration / 1000.0
        self.end_time = self.duration
        self._update_sliders_range()
        self._update_time_display()

    def _on_media_status_changed(self, status):
        if status == QMediaPlayer.MediaStatus.EndOfMedia:
            self.is_playing = False
            if os.path.exists(self.play_icon_path):
                self.ui.btnPlayPause.setIcon(QIcon(self.play_icon_path))
            self.media_player.setPosition(0)

    def _on_slider_moved(self, value):
        self._seek_preview(value)

    def _on_start_slider_moved(self, value):
        self._set_start_time(value, seek_preview=True)

    def _on_end_slider_moved(self, value):
        self._set_end_time(value, seek_preview=True)

    def _set_start_from_current(self):
        if self.media_player and self.duration > 0:
            current = self.media_player.position() / 1000.0
            self._set_start_time(current, seek_preview=True)

    def _set_end_from_current(self):
        if self.media_player and self.duration > 0:
            current = self.media_player.position() / 1000.0
            self._set_end_time(current, seek_preview=True)

    def _set_start_time(self, value, seek_preview=False):
        if self.duration <= 0:
            return
        self.start_time = clamp_start_time(value, self.end_time, self.duration)
        self.ui.sliderStartTime.blockSignals(True)
        self.ui.sliderStartTime.setValue(int(self.start_time))
        self.ui.sliderStartTime.blockSignals(False)
        self._update_range_display()
        if seek_preview:
            self._seek_preview(self.start_time)

    def _set_end_time(self, value, seek_preview=False):
        if self.duration <= 0:
            return
        self.end_time = clamp_end_time(value, self.start_time, self.duration)
        self.ui.sliderEndTime.blockSignals(True)
        self.ui.sliderEndTime.setValue(int(self.end_time))
        self.ui.sliderEndTime.blockSignals(False)
        self._update_range_display()
        if seek_preview:
            self._seek_preview(self.end_time)

    def _seek_preview(self, seconds):
        if not self.media_player or self.duration <= 0:
            return
        target_seconds = max(0.0, min(float(seconds), self.duration))
        target_ms = int(round(target_seconds * 1000))
        duration_ms = int(round(self.duration * 1000))
        target_ms = max(0, min(target_ms, duration_ms))
        self.media_player.setPosition(target_ms)

        self.ui.sliderCurrentTime.blockSignals(True)
        self.ui.sliderCurrentTime.setValue(target_ms // 1000)
        self.ui.sliderCurrentTime.blockSignals(False)
        self._update_time_display(target_ms / 1000.0)

    def _update_time_display(self, current=0):
        self.ui.labelCurrentTime.setText(
            f"{self._format_duration(current)} / {self._format_duration(self.duration)}"
        )

    def _update_sliders_range(self):
        max_val = max(1, int(self.duration))
        sliders = (
            self.ui.sliderCurrentTime,
            self.ui.sliderStartTime,
            self.ui.sliderEndTime,
        )
        for slider in sliders:
            slider.blockSignals(True)
            slider.setRange(0, max_val)
        self.ui.sliderStartTime.setValue(int(self.start_time))
        self.ui.sliderEndTime.setValue(int(self.end_time))
        for slider in sliders:
            slider.blockSignals(False)
        self._update_range_display()

    def _update_range_display(self):
        self.ui.labelStartTimeValue.setText(self._format_duration(self.start_time))
        self.ui.labelEndTimeValue.setText(self._format_duration(self.end_time))
        self.ui.labelSelectedDurationValue.setText(
            self._format_duration(max(0, self.end_time - self.start_time))
        )
        self.ui.labelEstimatedFramesValue.setText(f"{max(0, int(self.end_time - self.start_time))} 帧")

    def _get_duration(self, info):
        streams = info.get("streams") or []
        if streams:
            d = streams[0].get("duration")
            if d:
                return float(d)
        fmt = info.get("format") or {}
        d = fmt.get("duration")
        return float(d) if d else 0

    def _get_frame_count(self, info):
        streams = info.get("streams") or []
        if not streams:
            return None
        nb = streams[0].get("nb_frames")
        if not nb or nb == "N/A":
            return None
        return int(float(nb))

    def _get_fps(self, info):
        streams = info.get("streams") or []
        if not streams:
            return "--"
        fps_str = streams[0].get("r_frame_rate") or ""
        if "/" not in fps_str:
            return fps_str or "--"
        num, den = fps_str.split("/", 1)
        try:
            den_f = float(den)
            if den_f == 0:
                return "--"
            fps = float(num) / den_f
            return f"{fps:.2f}".rstrip("0").rstrip(".")
        except ValueError:
            return "--"

    def _format_duration(self, duration):
        total = int(round(duration))
        h = total // 3600
        m = (total % 3600) // 60
        s = total % 60
        if h > 0:
            return f"{h:02d}:{m:02d}:{s:02d}"
        return f"{m:02d}:{s:02d}"

    def _back_to_main_window(self):
        if self.media_player:
            self.media_player.stop()
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

    def get_positions(self):
        return (self._top_position, self._bottom_position)

    def _create_overlay(self):
        self._overlay = _SubtitleOverlay()
        self._overlay.set_positions(self._top_position, self._bottom_position)
        self._overlay.installEventFilter(self)

    def _sync_overlay_geometry(self):
        if not self._overlay or not self.video_widget.isVisible():
            return
        video_size = self.video_widget.videoSink().videoSize()
        video_rect = video_content_rect(self.video_widget.size(), video_size)

        if (
            self._positions_need_migration
            and video_size.width() > 0
            and video_size.height() > 0
        ):
            self._top_position = container_pct_to_video_pct(
                self._top_position, self.video_widget.height(), video_rect
            )
            self._bottom_position = container_pct_to_video_pct(
                self._bottom_position, self.video_widget.height(), video_rect
            )
            if self._bottom_position <= self._top_position + 5:
                self._top_position = TOP_POSITION
                self._bottom_position = BOTTOM_POSITION
            self._positions_need_migration = False
            self._overlay.set_positions(
                self._top_position, self._bottom_position
            )
            self._save_positions()

        global_pos = self.video_widget.mapToGlobal(video_rect.topLeft())
        self._overlay.setGeometry(
            global_pos.x(),
            global_pos.y(),
            video_rect.width(),
            video_rect.height(),
        )

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
# 处理窗口状态变化事件，当窗口最小化时隐藏 overlay，恢复时重新显示。
# 要不然会导致 overlay 钉在屏幕上
    def changeEvent(self, event):
        etype = event.type()
        if self._overlay and etype == QEvent.Type.WindowStateChange:
            if self.isMinimized():
                self._overlay.hide()
            else:
                self._sync_overlay_geometry()
                self._overlay.show()
                self._overlay.raise_()
        if self._overlay and etype == QEvent.Type.ActivationChange:
            if self.isActiveWindow():
                if not self.isMinimized():
                    self._sync_overlay_geometry()
                    self._overlay.show()
                    self._overlay.raise_()
            else:
                self._overlay.hide()
        super().changeEvent(event)

    def moveEvent(self, event):
        super().moveEvent(event)
        self._sync_overlay_geometry()

    def resizeEvent(self, event):
        super().resizeEvent(event)
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

    def _save_positions(self):
        from PySide6.QtCore import QSettings
        settings = QSettings("pinzimu", "pinzimu_gui")
        settings.setValue("subtitle_line_top", str(int(self._top_position)))
        settings.setValue("subtitle_line_bottom", str(int(self._bottom_position)))
        if not self._positions_need_migration:
            settings.setValue(
                "subtitle_line_coordinate_version",
                SUBTITLE_POSITION_COORDINATE_VERSION,
            )

    def _load_positions(self):
        from PySide6.QtCore import QSettings
        settings = QSettings("pinzimu", "pinzimu_gui")
        top_default = str(int(TOP_POSITION))
        bottom_default = str(int(BOTTOM_POSITION))
        saved_top = settings.value("subtitle_line_top", top_default)
        saved_bottom = settings.value("subtitle_line_bottom", bottom_default)
        has_saved_positions = settings.contains("subtitle_line_top") and settings.contains(
            "subtitle_line_bottom"
        )
        try:
            coordinate_version = int(
                settings.value("subtitle_line_coordinate_version", 1)
            )
        except (ValueError, TypeError):
            coordinate_version = 1
        self._positions_need_migration = (
            has_saved_positions
            and coordinate_version < SUBTITLE_POSITION_COORDINATE_VERSION
        )
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

    def _open_subtitleline(self):
        from py.Subtitleline import Subtitleline
        if self.media_player:
            self.media_player.stop()
        self.subtitleline_window = Subtitleline(
            main_window=self.main_window,
            video_path=self.video_path,
        )
        self.subtitleline_window.show()
        self.close()

    def _start_extract(self):
        ffmpeg_path = self._get_ffmpeg_path()
        if not ffmpeg_path:
            self.ui.labelProgressText.setText("错误: 未找到 ffmpeg")
            return
        if not self.video_path or not os.path.exists(self.video_path):
            self.ui.labelProgressText.setText("错误: 视频文件不存在")
            return

        self.ui.btnStartExtract.setEnabled(False)
        self.ui.labelProgressText.setText("正在提取中...")
        self.ui.progressExtract.setValue(0)

        range_seconds = max(0, self.end_time - self.start_time)
        if range_seconds <= 0:
            self.ui.labelProgressText.setText("错误: 时间范围无效")
            self.ui.btnStartExtract.setEnabled(True)
            return

        estimated_frames = int(range_seconds)
        max_frames = get_max_video_frames()
        if estimated_frames > max_frames:
            from PySide6.QtWidgets import QMessageBox
            QMessageBox.warning(
                self, "超出限制",
                f"当前预计提取 {estimated_frames} 帧，超过允许的最大 {max_frames} 帧。\n请重新选择提取范围。"
            )
            self.ui.labelProgressText.setText("错误: 帧数超出限制")
            self.ui.btnStartExtract.setEnabled(True)
            return

        freq_text = self.ui.comboFrequency.currentText()
        if freq_text == "全部帧":
            fps_str = None
        elif "s/帧" in freq_text:
            try:
                interval = float(freq_text.replace("s/帧", "").strip())
                fps_str = str(1.0 / interval) if interval > 0 else None
            except ValueError:
                fps_str = None
        else:
            fps_str = None

        output_dir = os.path.join(self._project_dir, "temp_frames")
        if os.path.exists(output_dir):
            shutil.rmtree(output_dir)
        os.makedirs(output_dir, exist_ok=True)

        cmd = [ffmpeg_path, "-y"]
        if self.start_time > 0:
            cmd.extend(["-ss", str(self.start_time)])
        cmd.extend(["-i", self.video_path])
        # 使用 -t (duration) 而不是 -to (absolute end time)
        # 这样可以确保提取的时长准确
        if self.end_time < self.duration:
            duration = self.end_time - self.start_time
            cmd.extend(["-t", str(duration)])
        if fps_str:
            cmd.extend(["-vf", f"fps={fps_str}"])
        cmd.extend(["-q:v", "2", os.path.join(output_dir, "frame_%04d.png")])

        # 调试日志: 打印实际的ffmpeg命令和参数
        print(f"[DEBUG] 频率文本: {freq_text}")
        print(f"[DEBUG] 计算的fps_str: {fps_str}")
        print(f"[DEBUG] 时间范围: start={self.start_time}, end={self.end_time}, duration={self.duration}")
        print(f"[DEBUG] 范围秒数: {range_seconds}")
        print(f"[DEBUG] FFmpeg命令: {' '.join(cmd)}")

        self._extract_worker = _ExtractWorker(cmd, output_dir, fps_str, range_seconds, self.duration)
        self._extract_worker.progress.connect(self._on_extract_progress)
        self._extract_worker.finished.connect(self._on_extract_finished)
        self._extract_worker.start()

    def _on_extract_progress(self, value):
        self.ui.progressExtract.setValue(value)

    def _on_extract_finished(self, frame_paths):
        self.ui.btnStartExtract.setEnabled(True)
        if not frame_paths:
            self.ui.labelProgressText.setText("提取完成: 0 张截图")
            return
        self.ui.progressExtract.setValue(100)
        self.ui.labelProgressText.setText(f"提取完成: {len(frame_paths)} 张截图")
        if self.media_player:
            self.media_player.pause()
        from py.Imagestitcher import Imagestitcher
        self.imagestitcher_window = Imagestitcher(
            frame_paths=frame_paths,
            subtitle_line_top=self._top_position,
            subtitle_line_bottom=self._bottom_position,
            main_window=self,
        )
        self.imagestitcher_window.show()
        self.hide()


class _ExtractWorker(QThread):
    progress = Signal(int)
    finished = Signal(list)

    def __init__(self, cmd, output_dir, fps_str, range_seconds, total_duration):
        super().__init__()
        self.cmd = cmd
        self.output_dir = output_dir
        self.fps_str = fps_str
        self.range_seconds = range_seconds
        self.total_duration = total_duration

    def run(self):
        try:
            self.progress.emit(0)
            process = subprocess.Popen(
                self.cmd,
                stderr=subprocess.PIPE,
                stdout=subprocess.DEVNULL,
                text=True,
                encoding="utf-8",
                errors="ignore",
                creationflags=subprocess.CREATE_NO_WINDOW,
            )
            frame_pattern = re.compile(r"frame=\s*(\d+)")
            total_frames = None
            last_progress = 0
            while True:
                line = process.stderr.readline()
                if not line and process.poll() is not None:
                    break
                match = frame_pattern.search(line)
                if match:
                    current_frame = int(match.group(1))
                    if total_frames is None:
                        if self.fps_str:
                            try:
                                total_frames = int(float(self.fps_str) * self.range_seconds)
                            except (ValueError, TypeError):
                                total_frames = max(1, int(self.range_seconds))
                        else:
                            total_frames = max(1, int(self.total_duration * 30))
                    if total_frames > 0:
                        pct = min(99, int(current_frame / total_frames * 100))
                        if pct > last_progress:
                            last_progress = pct
                            self.progress.emit(pct)
            process.wait()
            frame_paths = sorted(
                [
                    os.path.join(self.output_dir, f)
                    for f in os.listdir(self.output_dir)
                    if f.endswith(".png")
                ],
                key=lambda x: os.path.getmtime(x),
            )
            self.finished.emit(frame_paths)
        except Exception:
            frame_paths = sorted(
                [
                    os.path.join(self.output_dir, f)
                    for f in os.listdir(self.output_dir)
                    if f.endswith(".png")
                ],
                key=lambda x: os.path.getmtime(x),
            )
            self.finished.emit(frame_paths)


class _SubtitleOverlay(QFrame):
    """独立顶级窗口，透明背景，手动跟随 videoAreaFrame 位置。"""

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
        """上边缘和下边缘的设计"""
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
