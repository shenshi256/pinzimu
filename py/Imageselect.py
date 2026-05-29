#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------------
# @Time    : 2026/5/28 17:10
# @Author  : WXY
# @File    : Imageselect.py
# @PROJECT_NAME: 20260525_pinzimu_gui
# @PRODUCT_NAME: PyCharm
# -------------------------------------------------------------------------------
import os

from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QPixmap, QPainter, QIntValidator
from PySide6.QtWidgets import QMainWindow, QLabel, QFrame, QMessageBox

from py_gui.imageselect_ui import Ui_ImageSelect
from py.utils import setup_window_icon, draw_subtitle_lines, TOP_POSITION, BOTTOM_POSITION, show_confirm, COPYRIGHT, get_project_root, setup_window_title, get_max_image_count
from py.ImageDialog import stitch_and_show_dialog


class _ImageOverlay(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAttribute(Qt.WidgetAttribute.WA_TransparentForMouseEvents, False)
        self.setMouseTracking(True)
        self._top_position = TOP_POSITION
        self._bottom_position = BOTTOM_POSITION
        self._dragging = None
        self._on_positions_changed = None

    def set_positions(self, top_pct, bottom_pct):
        self._top_position = top_pct
        self._bottom_position = bottom_pct
        self.update()

    def get_positions(self):
        return (self._top_position, self._bottom_position)

    def set_on_positions_changed(self, callback):
        self._on_positions_changed = callback

    def paintEvent(self, event):
        painter = QPainter(self)
        if not painter.isActive():
            return
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        draw_subtitle_lines(
            painter, self.width(), self.height(),
            self._top_position, self._bottom_position,
        )

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            top_y = int(self.height() * self._top_position / 100.0)
            bottom_y = int(self.height() * self._bottom_position / 100.0)
            if abs(event.position().y() - top_y) <= 10:
                self._dragging = "top"
                self.setCursor(Qt.CursorShape.SizeVerCursor)
            elif abs(event.position().y() - bottom_y) <= 10:
                self._dragging = "bottom"
                self.setCursor(Qt.CursorShape.SizeVerCursor)

    def mouseMoveEvent(self, event):
        if self._dragging:
            pct = max(0.0, min(100.0, event.position().y() / self.height() * 100.0))
            if self._dragging == "top":
                if pct >= self._bottom_position - 5:
                    pct = self._bottom_position - 5
                self._top_position = max(0.0, pct)
            else:
                if pct <= self._top_position + 5:
                    pct = self._top_position + 5
                self._bottom_position = min(100.0, pct)
            self.update()
        else:
            top_y = int(self.height() * self._top_position / 100.0)
            bottom_y = int(self.height() * self._bottom_position / 100.0)
            near_top = abs(event.position().y() - top_y) <= 10
            near_bottom = abs(event.position().y() - bottom_y) <= 10
            if near_top or near_bottom:
                self.setCursor(Qt.CursorShape.SizeVerCursor)
            else:
                self.unsetCursor()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton and self._dragging:
            self._dragging = None
            self.unsetCursor()
            if self._on_positions_changed:
                self._on_positions_changed(self._top_position, self._bottom_position)


class Imageselect(QMainWindow):
    def __init__(self, image_paths, main_window=None):
        super().__init__()
        self.ui = Ui_ImageSelect()
        self.ui.setupUi(self)
        setup_window_icon(self)
        setup_window_title(self)
        self.ui.labelFooter.setText(COPYRIGHT)
        self.main_window = main_window
        self.image_paths = list(image_paths)
        self._current_index = 0
        self._project_dir = get_project_root()
        self._preview_label = None
        self._overlay = None
        self._positions = {}
        self._init_positions()
        self._init_ui()
        self._setup_preview()
        self._update_navigation()

    def _init_positions(self):
        for i in range(len(self.image_paths)):
            self._positions[i] = (TOP_POSITION, BOTTOM_POSITION)

    def _init_ui(self):
        self.ui.btnRestart.clicked.connect(self._back_to_main_window)
        self.ui.btnPrevImage.clicked.connect(self._prev_image)
        self.ui.btnNextImage.clicked.connect(self._next_image)
        self.ui.btnAddImages.clicked.connect(self._add_images)
        self.ui.btnResetDefault.clicked.connect(self._reset_current)
        self.ui.btnResetAll.clicked.connect(self._reset_all)
        self.ui.btnSyncAll.clicked.connect(self._sync_all)
        self.ui.btnGenerate.clicked.connect(self._on_generate)
        self._setup_goto_validator()
        self.ui.btnGoToPage.clicked.connect(self._go_to_page)
        self._update_image_count_label()

    def _setup_preview(self):
        self._preview_label = QLabel()
        self._preview_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self._preview_label.setStyleSheet("background-color: transparent; border: none;")
        layout = self.ui.previewArea.layout()
        if layout is not None:
            layout.addWidget(self._preview_label)

        self._overlay = _ImageOverlay(self.ui.previewArea)
        self._overlay.setStyleSheet("background: transparent;")
        self._overlay.set_on_positions_changed(self._on_overlay_positions_changed)
        self._overlay.raise_()

        self._preview_label.setMinimumSize(1, 1)
        QTimer.singleShot(50, self._show_current_image)

    def _on_overlay_positions_changed(self, top_pct, bottom_pct):
        if 0 <= self._current_index < len(self.image_paths):
            self._positions[self._current_index] = (top_pct, bottom_pct)
            self._update_info_label()

    def _show_current_image(self):
        if not self.image_paths or self._current_index < 0:
            return
        if self._current_index >= len(self.image_paths):
            self._current_index = len(self.image_paths) - 1
        path = self.image_paths[self._current_index]
        if not os.path.exists(path):
            return
        pixmap = QPixmap(path)
        if pixmap.isNull():
            return
        available_size = self.ui.previewArea.size()
        if available_size.width() > 10 and available_size.height() > 10:
            scaled = pixmap.scaled(
                available_size,
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation,
            )
            self._preview_label.setPixmap(scaled)
        else:
            self._preview_label.setPixmap(pixmap)

        top_pct, bottom_pct = self._positions.get(
            self._current_index, (TOP_POSITION, BOTTOM_POSITION)
        )
        self._overlay.set_positions(top_pct, bottom_pct)
        self._update_info_label()

    def _update_info_label(self):
        top, bottom = self._positions.get(
            self._current_index, (TOP_POSITION, BOTTOM_POSITION)
        )
        height_pct = max(0, int(bottom - top))
        self.ui.labelInfoDetail.setText(
            f"字幕区域高度：{height_pct}% · 每张图片独立保存"
        )

    def _update_navigation(self):
        total = len(self.image_paths)
        self.ui.labelImageCounter.setText(f"第 {self._current_index + 1} / {total} 张")
        self.ui.btnPrevImage.setEnabled(self._current_index > 0)
        self.ui.btnNextImage.setEnabled(self._current_index < total - 1)
        self._update_image_count_label()
        self._update_goto_field()

    def _setup_goto_validator(self):
        total = len(self.image_paths)
        validator = QIntValidator(1, max(1, total))
        self.ui.editGoToPage.setValidator(validator)

    def _update_goto_field(self):
        total = len(self.image_paths)
        self.ui.editGoToPage.setText(str(self._current_index + 1))
        validator = self.ui.editGoToPage.validator()
        if isinstance(validator, QIntValidator):
            validator.setTop(max(1, total))

    def _update_image_count_label(self):
        count = len(self.image_paths)
        max_count = get_max_image_count()
        self.ui.labelImageCount.setText(f"当前已有 {count} 张图片")
        self.ui.labelImageAddHint.setText(f"可继续添加图片（最多{max_count}张）")

    def _prev_image(self):
        if self._current_index > 0:
            self._current_index -= 1
            self._show_current_image()
            self._update_navigation()

    def _next_image(self):
        if self._current_index < len(self.image_paths) - 1:
            self._current_index += 1
            self._show_current_image()
            self._update_navigation()

    def _go_to_page(self):
        text = self.ui.editGoToPage.text().strip()
        if not text:
            self._update_goto_field()
            return
        try:
            page = int(text)
        except ValueError:
            self._update_goto_field()
            return
        total = len(self.image_paths)
        page = max(1, min(total, page))
        new_index = page - 1
        if new_index != self._current_index:
            self._current_index = new_index
            self._show_current_image()
        self._update_navigation()

    def _reset_current(self):
        self._positions[self._current_index] = (TOP_POSITION, BOTTOM_POSITION)
        top_pct, bottom_pct = self._positions[self._current_index]
        self._overlay.set_positions(top_pct, bottom_pct)
        self._update_info_label()

    def _reset_all(self):
        reply = show_confirm(
            self, "重置全部",
            "是否要将所有图片的字幕边线恢复默认设置？",
        )
        if reply == QMessageBox.StandardButton.Yes:
            for i in range(len(self.image_paths)):
                self._positions[i] = (TOP_POSITION, BOTTOM_POSITION)
            top_pct, bottom_pct = self._positions[self._current_index]
            self._overlay.set_positions(top_pct, bottom_pct)
            self._update_info_label()

    def _sync_all(self):
        reply = show_confirm(
            self, "同步所有",
            "是否以当前图片边线为基准，同步所有图片的边线？",
        )
        if reply == QMessageBox.StandardButton.Yes:
            current_top, current_bottom = self._positions[self._current_index]
            for i in range(len(self.image_paths)):
                self._positions[i] = (current_top, current_bottom)
            self._update_info_label()

    def _add_images(self):
        from PySide6.QtWidgets import QFileDialog
        last_dir = os.path.dirname(self.image_paths[0]) if self.image_paths else ""
        file_paths, _ = QFileDialog.getOpenFileNames(
            self,
            "添加图片",
            last_dir,
            "图片文件 (*.jpg *.jpeg *.png *.gif *.webp)"
        )
        if file_paths:
            existing = set(os.path.normpath(p) for p in self.image_paths)
            new_paths = [
                p for p in file_paths
                if os.path.normpath(p) not in existing
            ]
            if not new_paths:
                QMessageBox.information(self, "提示", "所选图片已全部存在列表中。")
                return

            current_total = len(self.image_paths)
            max_count = get_max_image_count()
            remaining = max_count - current_total
            paths_to_add = new_paths[:remaining]
            skipped = len(new_paths) - len(paths_to_add)

            start_idx = len(self.image_paths)
            self.image_paths.extend(paths_to_add)
            for i, _ in enumerate(paths_to_add):
                self._positions[start_idx + i] = (TOP_POSITION, BOTTOM_POSITION)
            self._update_navigation()

            if skipped > 0:
                QMessageBox.warning(
                    self, "超出限制",
                    f"最多支持{max_count}张图片，已截取前{remaining}张"
                )

    def _on_generate(self):
        if not self.image_paths:
            QMessageBox.warning(self, "生成失败", "没有可用的图片。")
            return
        width_mode = self.ui.comboForceWidth.currentIndex()
        stitch_and_show_dialog(
            self, self.image_paths, self._positions,
            width_mode=width_mode, current_index=self._current_index,
        )

    def _back_to_main_window(self):
        if self._overlay:
            self._overlay.hide()
        self.hide()
        if self.main_window:
            self.main_window.show()
        self.deleteLater()

    def resizeEvent(self, event):
        super().resizeEvent(event)
        if self._overlay:
            self._overlay.setGeometry(self.ui.previewArea.rect())
        self._show_current_image()

    def showEvent(self, event):
        super().showEvent(event)
        if self._overlay:
            self._overlay.setGeometry(self.ui.previewArea.rect())
            self._overlay.raise_()
        self._show_current_image()
