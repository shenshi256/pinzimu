#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------------
# @Time    : 2026/5/29 15:17
# @Author  : WXY
# @File    : Settings.py
# @PROJECT_NAME: 20260525_pinzimu_gui
# @PRODUCT_NAME: PyCharm
# -------------------------------------------------------------------------------
from PySide6.QtGui import QIntValidator
from PySide6.QtWidgets import QMainWindow
from py_gui.settings_ui import Ui_SettingsWindow
from utils import (setup_window_icon, setup_window_title,
                   get_logging_enabled, set_logging_enabled,
                   get_max_image_count, set_max_image_count,
                   get_max_video_frames, set_max_video_frames,
                   show_info, show_error)

MIN_VALUE = 1
MAX_VALUE = 999999


class SettingsWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_SettingsWindow()
        self.ui.setupUi(self)
        setup_window_icon(self)
        setup_window_title(self, "设置")
        self._valid_image_count = 50
        self._valid_video_frames = 200

        validator = QIntValidator(MIN_VALUE, MAX_VALUE)
        self.ui.editImageCount.setValidator(validator)
        self.ui.editVideoFrames.setValidator(validator)

        self.ui.editImageCount.editingFinished.connect(self._on_image_count_finished)
        self.ui.editVideoFrames.editingFinished.connect(self._on_video_frames_finished)

        self._load_settings()
        self.ui.btnSave.clicked.connect(self._on_save)

    def _load_settings(self):
        logging_enabled = get_logging_enabled()
        self.ui.radioLogYes.setChecked(logging_enabled)
        self.ui.radioLogNo.setChecked(not logging_enabled)

        max_image = get_max_image_count()
        self._valid_image_count = max_image
        self.ui.editImageCount.setText(str(max_image))

        max_frames = get_max_video_frames()
        self._valid_video_frames = max_frames
        self.ui.editVideoFrames.setText(str(max_frames))

    def _validate_int_field(self, line_edit, field_name, fallback_value):
        text = line_edit.text().strip()
        if not text:
            show_error(self, "输入错误", f"{field_name}不能为空")
            line_edit.setText(str(fallback_value))
            line_edit.setFocus()
            return False
        try:
            value = int(text)
        except ValueError:
            show_error(self, "输入错误", f"{field_name}必须为整数")
            line_edit.setText(str(fallback_value))
            line_edit.setFocus()
            return False
        if value < MIN_VALUE or value > MAX_VALUE:
            show_error(self, "输入错误", f"{field_name}范围为 {MIN_VALUE} - {MAX_VALUE}")
            line_edit.setText(str(fallback_value))
            line_edit.setFocus()
            return False
        return value

    def _on_image_count_finished(self):
        result = self._validate_int_field(
            self.ui.editImageCount, "图片数量", self._valid_image_count
        )
        if result is not False:
            self._valid_image_count = result

    def _on_video_frames_finished(self):
        result = self._validate_int_field(
            self.ui.editVideoFrames, "视频帧数量", self._valid_video_frames
        )
        if result is not False:
            self._valid_video_frames = result

    def _on_save(self):
        image_result = self._validate_int_field(
            self.ui.editImageCount, "图片数量", self._valid_image_count
        )
        if image_result is False:
            return

        video_result = self._validate_int_field(
            self.ui.editVideoFrames, "视频帧数量", self._valid_video_frames
        )
        if video_result is False:
            return

        set_logging_enabled(self.ui.radioLogYes.isChecked())
        set_max_image_count(image_result)
        set_max_video_frames(video_result)
        show_info(self, "保存成功", "设置已保存，部分配置将在下次启动程序时生效。")
        self.close()
