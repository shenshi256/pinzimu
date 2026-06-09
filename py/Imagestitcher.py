#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------------
# @Time    : 2026/5/27 18:08
# @Author  : WXY
# @File    : Imagestitcher
# @PROJECT_NAME: 20260525_pinzimu_gui
# @PRODUCT_NAME: PyCharm
# -------------------------------------------------------------------------------
import logging
import os
import shutil
from PIL import Image
from LoggerManager import logger_manager
from rapidocr_onnxruntime import RapidOCR

from PySide6.QtCore import Qt, QPoint, QPointF, QRect, QSize, QTimer, Signal
from PySide6.QtGui import QIcon, QPixmap, QPainter, QColor, QPen, QImage
from PySide6.QtWidgets import (
    QMainWindow, QWidget, QLayout, QPushButton,
    QLabel, QCheckBox, QMessageBox, QApplication, QFileDialog,
)
from py_gui.imagestitcher_ui import Ui_ImageStitcher
from py.utils import show_confirm, setup_window_icon, COPYRIGHT, get_project_root, setup_window_title
from py.ImageDialog import show_image_dialog
from py.Loading import LoadingOverlay

PADDING = 8
GAP = 8
CARD_BORDER_RADIUS = 6
BADGE_SIZE = 22
DELETE_BTN_SIZE = 22
MOVE_ICON_SIZE = 24
DRAG_THRESHOLD = 8
CARD_MIN_WIDTH = 120
CARD_MAX_WIDTH = 320


class FlowLayout(QLayout):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._items = []
        self._h_spacing = GAP
        self._v_spacing = GAP

    def addItem(self, item):
        self._items.append(item)

    def count(self):
        return len(self._items)

    def itemAt(self, index):
        if 0 <= index < len(self._items):
            return self._items[index]
        return None

    def takeAt(self, index):
        if 0 <= index < len(self._items):
            return self._items.pop(index)
        return None

    def expandingDirections(self):
        return Qt.Orientation(0)

    def hasHeightForWidth(self):
        return True

    def heightForWidth(self, width):
        return self._do_layout(QRect(0, 0, width, 0), True)

    def setGeometry(self, rect):
        super().setGeometry(rect)
        self._do_layout(rect, False)

    def sizeHint(self):
        return self.minimumSize()

    def minimumSize(self):
        size = QSize()
        for item in self._items:
            size = size.expandedTo(item.minimumSize())
        margins = self.contentsMargins()
        size += QSize(margins.left() + margins.right(), margins.top() + margins.bottom())
        return size

    def _do_layout(self, rect, test_only):
        margins = self.contentsMargins()
        available_width = rect.width() - margins.left() - margins.right()
        x = margins.left()
        y = margins.top()
        row_height = 0

        for item in self._items:
            item_size = item.sizeHint()
            next_x = x + item_size.width() + self._h_spacing
            if x > margins.left() and next_x > margins.left() + available_width:
                x = margins.left()
                y += row_height + self._v_spacing
                row_height = 0
            if not test_only:
                item.setGeometry(QRect(QPoint(x, y), item_size))
            x += item_size.width() + self._h_spacing
            row_height = max(row_height, item_size.height())

        return y + row_height + margins.bottom()


class FrameCard(QWidget):
    delete_clicked = Signal(int)
    check_changed = Signal(int, bool)
    drag_started = Signal(int)
    drag_moved = Signal(int, QPoint)
    drag_finished = Signal(int)
    drag_cancelled = Signal()

    def __init__(self, index, image_path, card_size, subtitle_line_top, subtitle_line_bottom, parent=None):
        super().__init__(parent)
        self._index = index
        self._image_path = image_path
        self._card_size = card_size
        self._subtitle_line_top = subtitle_line_top
        self._subtitle_line_bottom = subtitle_line_bottom
        self._checked = False
        self._hovered = False
        self._is_drag_source = False
        self._drag_start_pos = None
        self._dragging = False
        self._project_dir = get_project_root()

        self.setFixedSize(card_size)
        self.setMouseTracking(True)
        self.setCursor(Qt.CursorShape.PointingHandCursor)

        self._thumbnail = self._load_thumbnail()

        self._badge = QLabel(str(index + 1), self)
        self._badge.setFixedSize(BADGE_SIZE, BADGE_SIZE)
        self._badge.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self._badge.setStyleSheet(
            "background-color: #6D28D9; color: #FFFFFF; border-radius: 11px; "
            "font-size: 11px; font-weight: 700;"
        )
        self._badge.move(6, 6)
        self._badge.raise_()

        self._checkbox = QCheckBox(self)
        self._checkbox.setFixedSize(20, 20)
        self._checkbox.setStyleSheet(
            "QCheckBox::indicator { width: 16px; height: 16px; }"
        )
        self._checkbox.move(card_size.width() - 48, 6)
        self._checkbox.stateChanged.connect(self._on_check_changed)
        self._checkbox.raise_()

        self._delete_btn = QPushButton(self)
        self._delete_btn.setFixedSize(DELETE_BTN_SIZE, DELETE_BTN_SIZE)
        close_path = os.path.join(self._project_dir, "imgs", "close.png")
        if os.path.exists(close_path):
            self._delete_btn.setIcon(QIcon(close_path))
            self._delete_btn.setIconSize(QSize(12, 12))
        else:
            self._delete_btn.setText("X")
        self._delete_btn.setStyleSheet(
            "QPushButton { background-color: #EF4343; border: none; border-radius: 11px; }"
            "QPushButton:hover { background-color: #DC2626; }"
        )
        self._delete_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        self._delete_btn.clicked.connect(self._on_delete_clicked)
        self._delete_btn.move(card_size.width() - DELETE_BTN_SIZE - 4, 4)
        self._delete_btn.hide()
        self._delete_btn.raise_()

        self._move_icon = QLabel(self)
        move_path = os.path.join(self._project_dir, "imgs", "move.png")
        if os.path.exists(move_path):
            self._move_icon.setPixmap(QPixmap(move_path).scaled(
                MOVE_ICON_SIZE, MOVE_ICON_SIZE, Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation
            ))
        self._move_icon.setFixedSize(MOVE_ICON_SIZE, MOVE_ICON_SIZE)
        self._move_icon.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self._move_icon.move(
            (card_size.width() - MOVE_ICON_SIZE) // 2,
            (card_size.height() - MOVE_ICON_SIZE) // 2,
        )
        self._move_icon.hide()
        self._move_icon.raise_()

    def _load_thumbnail(self):
        if os.path.exists(self._image_path):
            pixmap = QPixmap(self._image_path)
            if not pixmap.isNull():
                return pixmap.scaled(
                    self._card_size,
                    Qt.AspectRatioMode.KeepAspectRatio,
                    Qt.TransformationMode.SmoothTransformation,
                )
        return None

    def reload_thumbnail(self, new_size):
        self._card_size = new_size
        self._thumbnail = self._load_thumbnail()

    def set_index(self, index):
        self._index = index
        self._badge.setText(str(index + 1))

    def index(self):
        return self._index

    def image_path(self):
        return self._image_path

    def set_checked(self, checked):
        self._checked = checked
        self._checkbox.blockSignals(True)
        self._checkbox.setChecked(checked)
        self._checkbox.blockSignals(False)

    def is_checked(self):
        return self._checked

    def set_drag_source(self, is_source):
        self._is_drag_source = is_source
        self.update()

    def _on_check_changed(self, state):
        self._checked = (state == Qt.CheckState.Checked.value)
        self.check_changed.emit(self._index, self._checked)

    def _on_delete_clicked(self):
        self.delete_clicked.emit(self._index)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        painter.setPen(Qt.PenStyle.NoPen)
        if self._is_drag_source:
            painter.setBrush(QColor("#E8E0FC"))
        elif self._hovered:
            painter.setBrush(QColor("#F5F3FF"))
        else:
            painter.setBrush(QColor("#FFFFFF"))
        painter.drawRoundedRect(self.rect().adjusted(0, 0, -1, -1), CARD_BORDER_RADIUS, CARD_BORDER_RADIUS)

        if self._thumbnail and not self._thumbnail.isNull():
            img_rect = QRect(
                (self.width() - self._thumbnail.width()) // 2,
                (self.height() - self._thumbnail.height()) // 2,
                self._thumbnail.width(),
                self._thumbnail.height(),
            )
            painter.drawPixmap(img_rect, self._thumbnail)
            self._draw_subtitle_region(painter, img_rect)

        pen_color = QColor("#C4B5FD") if self._is_drag_source else QColor("#E5E7EB")
        pen_width = 2 if self._is_drag_source else 1
        painter.setPen(QPen(pen_color, pen_width))
        painter.setBrush(Qt.BrushStyle.NoBrush)
        painter.drawRoundedRect(self.rect().adjusted(0, 0, -1, -1), CARD_BORDER_RADIUS, CARD_BORDER_RADIUS)

    def _draw_subtitle_region(self, painter, img_rect):
        top_y = img_rect.top() + int(img_rect.height() * self._subtitle_line_top / 100.0)
        bottom_y = img_rect.top() + int(img_rect.height() * self._subtitle_line_bottom / 100.0)

        overlay = QColor(239, 68, 68, 40)
        painter.fillRect(
            QRect(img_rect.left(), top_y, img_rect.width(), bottom_y - top_y),
            overlay,
        )

        line_pen = QPen(QColor("#EF4444"), 2, Qt.PenStyle.DashLine)
        painter.setPen(line_pen)
        painter.drawLine(QPointF(img_rect.left(), top_y), QPointF(img_rect.right(), top_y))
        painter.drawLine(QPointF(img_rect.left(), bottom_y), QPointF(img_rect.right(), bottom_y))

    def enterEvent(self, event):
        self._hovered = True
        self._delete_btn.show()
        self._move_icon.show()
        self.update()

    def leaveEvent(self, event):
        self._hovered = False
        if not self._is_drag_source:
            self._delete_btn.hide()
            self._move_icon.hide()
        self.update()

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self._drag_start_pos = event.pos()
        super().mousePressEvent(event)

    def mouseMoveEvent(self, event):
        if self._drag_start_pos is not None:
            if not self._dragging:
                delta = (event.pos() - self._drag_start_pos).manhattanLength()
                if delta >= DRAG_THRESHOLD:
                    self._dragging = True
                    self.setCursor(Qt.CursorShape.ClosedHandCursor)
                    self.raise_()
                    self.drag_started.emit(self._index)
            if self._dragging:
                global_pos = self.mapToGlobal(event.pos())
                self.drag_moved.emit(self._index, global_pos)
        super().mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            was_dragging = self._dragging
            self._drag_start_pos = None
            self._dragging = False
            self.setCursor(Qt.CursorShape.PointingHandCursor)
            self.update()
            if was_dragging:
                self.drag_finished.emit(self._index)
        super().mouseReleaseEvent(event)


class Imagestitcher(QMainWindow):
    def __init__(self, frame_paths, subtitle_line_top, subtitle_line_bottom, main_window=None):
        super().__init__()
        self.ui = Ui_ImageStitcher()
        self.ui.setupUi(self)
        setup_window_icon(self)
        setup_window_title(self)
        self.frame_paths = list(frame_paths)
        self.subtitle_line_top = subtitle_line_top
        self.subtitle_line_bottom = subtitle_line_bottom
        self.main_window = main_window
        self._project_dir = get_project_root()
        self._cards = []
        self._card_size = QSize(0, 0)
        self._drag_source_index = -1
        self._drag_hover_index = -1
        self._layout_done = False
        self._ocr_engine = None
        self._loading_overlay = None
        self._init_ui()
        self._setup_image_grid()
        self._connect_signals()

    def showEvent(self, event):
        super().showEvent(event)
        if not self._layout_done:
            self._loading_overlay = LoadingOverlay(self.ui.imageListScrollArea)
            self._loading_overlay.start()
            QApplication.processEvents()
            QTimer.singleShot(30, self._load_cards)
            self._layout_done = True

    def _init_ui(self):
        self.ui.labelSubtitleLineValue.setText(
            f"上边线 {int(self.subtitle_line_top)}%  -  下边线 {int(self.subtitle_line_bottom)}%"
        )
        self.ui.labelImageCount.setText(f"共 {len(self.frame_paths)} 张截图")

    def _connect_signals(self):
        self.ui.btnRestart.clicked.connect(self._back_to_main_window)
        self.ui.btnSelectAll.clicked.connect(self._toggle_select_all)
        self.ui.btnDeleteSelected.clicked.connect(self._delete_selected)
        self.ui.btnAutoDeduplicate.clicked.connect(self._on_auto_deduplicate)
        self.ui.btnUndoDeduplicate.clicked.connect(self._on_undo_deduplicate)
        self.ui.btnGenerate.clicked.connect(self._on_generate)
        self.ui.btnOutputImages.clicked.connect(self._on_export_images)
        self.ui.btnBackToVideo.clicked.connect(self._on_back_to_video)

    def _setup_image_grid(self):
        container = self.ui.imageListContainer
        self._flow_layout = FlowLayout(container)
        self._flow_layout.setContentsMargins(PADDING, PADDING, PADDING, PADDING)
        self._flow_layout.setSpacing(GAP)

        self.ui.imageListScrollArea.installEventFilter(self)

        if self.frame_paths and os.path.exists(self.frame_paths[0]):
            sample = QPixmap(self.frame_paths[0])
            if not sample.isNull():
                self._aspect_ratio = sample.width() / max(sample.height(), 1)
            else:
                self._aspect_ratio = 16.0 / 9.0
        else:
            self._aspect_ratio = 16.0 / 9.0

    def eventFilter(self, watched, event):
        from PySide6.QtCore import QEvent
        if watched == self.ui.imageListScrollArea and event.type() == QEvent.Type.Resize:
            if self._layout_done:
                QTimer.singleShot(0, self._relayout_cards)
        return super().eventFilter(watched, event)

    def _safe_viewport_width(self):
        area = self.ui.imageListScrollArea
        vp = area.viewport()
        vw = vp.width() if vp else 0
        sb = area.verticalScrollBar()
        sw = sb.width() if sb and sb.isVisible() else 12
        if vw < 50:
            return area.width() - sw
        return vw

    def _calc_card_size(self):
        viewport_width = self._safe_viewport_width()
        available = viewport_width - PADDING * 2
        card_width = (available - GAP * 3) // 4
        card_width = max(CARD_MIN_WIDTH, min(CARD_MAX_WIDTH, card_width))
        card_height = int(card_width / self._aspect_ratio)
        return QSize(card_width, card_height)

    def _build_card(self, i, path):
        card = FrameCard(
            i, path, self._card_size,
            self.subtitle_line_top, self.subtitle_line_bottom,
        )
        card.delete_clicked.connect(self._on_card_delete)
        card.check_changed.connect(self._on_card_check_changed)
        card.drag_started.connect(self._on_card_drag_start)
        card.drag_moved.connect(self._on_card_drag_moved)
        card.drag_finished.connect(self._on_card_drag_finished)
        self._cards.append(card)
        self._flow_layout.addWidget(card)

    def _build_cards(self):
        for card in self._cards:
            card.deleteLater()
        self._cards.clear()
        self._card_size = self._calc_card_size()
        for i, path in enumerate(self.frame_paths):
            self._build_card(i, path)

    def _load_cards(self):
        self._card_size = self._calc_card_size()
        container = self.ui.imageListContainer
        container.setUpdatesEnabled(False)
        for i, path in enumerate(self.frame_paths):
            self._build_card(i, path)
            self._cards[-1].hide()
            if (i + 1) % 15 == 0:
                QApplication.processEvents()
        self._flow_layout.invalidate()
        self._flow_layout.activate()
        container.setUpdatesEnabled(True)
        self._load_index = 0
        self._show_next_card()

    def _show_next_card(self):
        if self._load_index >= len(self._cards):
            if self._loading_overlay:
                self._loading_overlay.stop()
            return
        self._cards[self._load_index].show()
        self._load_index += 1
        if self._load_index < len(self._cards):
            QTimer.singleShot(30, self._show_next_card)
        else:
            if self._loading_overlay:
                self._loading_overlay.stop()

    def _remove_card_at(self, index):
        item = self._flow_layout.takeAt(index)
        if item:
            w = item.widget()
            if w:
                w.blockSignals(True)
                w.setParent(None)
                w.deleteLater()
        self._cards.pop(index)
        self.frame_paths.pop(index)
        for i in range(index, len(self._cards)):
            self._cards[i].set_index(i)

    def _relayout_cards(self):
        new_size = self._calc_card_size()
        if new_size == self._card_size and self._cards:
            return
        self._card_size = new_size
        for card in self._cards:
            card.setFixedSize(self._card_size)
            card.reload_thumbnail(self._card_size)
            card._checkbox.move(self._card_size.width() - 48, 6)
            card._delete_btn.move(self._card_size.width() - DELETE_BTN_SIZE - 4, 4)
            card._move_icon.move(
                (self._card_size.width() - MOVE_ICON_SIZE) // 2,
                (self._card_size.height() - MOVE_ICON_SIZE) // 2,
            )
            card.update()
        self._flow_layout.invalidate()
        self._flow_layout.activate()

    def _on_card_delete(self, index):
        if len(self._cards) <= 1:
            return
        self._remove_card_at(index)
        self._flow_layout.invalidate()
        self._flow_layout.activate()
        self.ui.labelImageCount.setText(f"共 {len(self.frame_paths)} 张截图")
        self._sync_select_all_button()

    def _on_card_check_changed(self, index, checked):
        self._sync_select_all_button()

    def _on_card_drag_start(self, index):
        self._drag_source_index = index
        self._cards[index].set_drag_source(True)

    def _on_card_drag_moved(self, index, global_pos):
        if self._drag_source_index < 0:
            return
        container = self.ui.imageListContainer
        local_pos = container.mapFromGlobal(global_pos)
        new_hover = -1
        for i, card in enumerate(self._cards):
            if i == self._drag_source_index:
                continue
            if card.geometry().contains(local_pos):
                new_hover = i
                break
        if new_hover != self._drag_hover_index:
            self._drag_hover_index = new_hover

    def _on_card_drag_finished(self, index):
        source = self._drag_source_index
        target = self._drag_hover_index
        self._cards[source].set_drag_source(False)
        self._drag_source_index = -1
        self._drag_hover_index = -1
        if target >= 0 and target != source:
            self._swap_cards(source, target)
        self._reindex_cards()

    def _swap_cards(self, a, b):
        self.frame_paths[a], self.frame_paths[b] = self.frame_paths[b], self.frame_paths[a]
        old_card_a = self._cards[a]
        old_card_b = self._cards[b]
        a_checked = old_card_a.is_checked()
        b_checked = old_card_b.is_checked()
        old_card_a.set_index(b)
        old_card_b.set_index(a)
        old_card_a.set_checked(b_checked)
        old_card_b.set_checked(a_checked)
        self._cards[a], self._cards[b] = old_card_b, old_card_a
        count = self._flow_layout.count()
        items = [self._flow_layout.takeAt(0) for _ in range(count)]
        for item in items:
            self._flow_layout.addItem(item)
        self._flow_layout.invalidate()
        self._flow_layout.activate()

    def _reindex_cards(self):
        for i, card in enumerate(self._cards):
            card.set_index(i)

    def _toggle_select_all(self):
        all_checked = all(card.is_checked() for card in self._cards)
        new_state = not all_checked
        for card in self._cards:
            card.set_checked(new_state)
        self._sync_select_all_button()

    def _sync_select_all_button(self):
        if self._cards:
            all_checked = all(card.is_checked() for card in self._cards)
            self.ui.btnSelectAll.setText("取消全选" if all_checked else "全选")

    def _delete_selected(self):
        indices_to_remove = [
            i for i, card in enumerate(self._cards)
            if card.is_checked()
        ]
        if not indices_to_remove:
            return
        if len(indices_to_remove) == len(self._cards):
            return
        count = len(indices_to_remove)
        reply = show_confirm(
            self,
            "删除提示",
            f"您选择了 {count} 张图片，是否删除？",
        )
        if reply != QMessageBox.StandardButton.Yes:
            return
        for i in sorted(indices_to_remove, reverse=True):
            self._remove_card_at(i)
        self._flow_layout.invalidate()
        self._flow_layout.activate()
        self.ui.labelImageCount.setText(f"共 {len(self.frame_paths)} 张截图")
        self._sync_select_all_button()

    def _on_generate(self):
        if not self.frame_paths:
            QMessageBox.warning(self, "生成失败", "没有可用的图片帧。")
            return

        total = len(self.frame_paths)
        self.ui.progressBar.setValue(0)
        self.ui.progressBar.setVisible(True)
        self.ui.imageListToolbarFrame.setEnabled(False)
        QApplication.processEvents()

        cropped_images = []
        max_width = 0
        for idx, path in enumerate(self.frame_paths):
            img = Image.open(path)
            img_w, img_h = img.size
            top_y = int(img_h * self.subtitle_line_top / 100.0)
            bottom_y = int(img_h * self.subtitle_line_bottom / 100.0)
            top_y = max(0, min(img_h - 1, top_y))
            bottom_y = max(top_y + 1, min(img_h, bottom_y))
            if idx == 0:
                cropped = img.crop((0, 0, img_w, bottom_y))
            else:
                cropped = img.crop((0, top_y, img_w, bottom_y))
            cropped_images.append(cropped)
            max_width = max(max_width, img_w)
            self.ui.progressBar.setValue(int((idx + 1) / total * 100))
            QApplication.processEvents()

        total_height = sum(img.size[1] for img in cropped_images)
        stitched = Image.new("RGB", (max_width, total_height), (255, 255, 255))
        y_offset = 0
        for img in cropped_images:
            stitched.paste(img, (0, y_offset))
            y_offset += img.size[1]

        self.ui.progressBar.setVisible(False)
        self.ui.imageListToolbarFrame.setEnabled(True)

        show_image_dialog(self, stitched)

    def _on_export_images(self):
        checked_indices = [i for i, card in enumerate(self._cards) if card.is_checked()]
        if checked_indices:
            export_paths = [self.frame_paths[i] for i in checked_indices]
        else:
            export_paths = list(self.frame_paths)

        count = len(export_paths)
        reply = show_confirm(
            self,
            "导出提示",
            f"您将要导出 {count} 张图片，是否继续？",
        )
        if reply != QMessageBox.StandardButton.Yes:
            return

        output_dir = QFileDialog.getExistingDirectory(self, "选择导出目录")
        if not output_dir:
            return

        for path in export_paths:
            dest = os.path.join(output_dir, os.path.basename(path))
            shutil.copy2(path, dest)

        QMessageBox.information(
            self, "导出提示",
            f"导出完成，{count} 张图片已保存到：\n{output_dir}",
        )

    def _ocr_subtitle_text(self, image_path):
        if self._ocr_engine is None:
            self._ocr_engine = RapidOCR()
        pixmap = QPixmap(image_path)
        if pixmap.isNull():
            return ""
        img_h = pixmap.height()
        top_y = int(img_h * self.subtitle_line_top / 100.0)
        bottom_y = int(img_h * self.subtitle_line_bottom / 100.0)
        top_y = max(0, min(img_h - 1, top_y))
        bottom_y = max(top_y + 1, min(img_h, bottom_y))
        crop_rect = QRect(0, top_y, pixmap.width(), bottom_y - top_y)
        cropped = pixmap.copy(crop_rect)
        image = cropped.toImage()
        image = image.convertToFormat(QImage.Format.Format_RGB888)
        ptr = image.constBits()
        import numpy as np
        arr = np.array(ptr).reshape(image.height(), image.width(), 3)
        result, _ = self._ocr_engine(arr)
        if result:
            return " ".join(item[1] for item in result if item[1]).strip()
        return ""

    def _run_ocr_batch(self, title, remove_empty_only):
        reply = show_confirm(
            self,
            title,
            "根据字幕文本自动去重，自动删除空字幕的图片，是否继续？" if not remove_empty_only
            else "自动删除空字幕的图片，是否继续？",
        )
        if reply != QMessageBox.StandardButton.Yes:
            return

        self.ui.imageListToolbarFrame.setEnabled(False)
        self.ui.progressBar.setValue(0)
        self.ui.progressBar.setVisible(True)

        total = len(self.frame_paths)
        texts = []
        for idx, path in enumerate(self.frame_paths):
            text = self._ocr_subtitle_text(path)

            texts.append((idx, text))

            self.ui.progressBar.setValue(int((idx + 1) / total * 100))
            QApplication.processEvents()
        logger_manager.info(texts)
        self.ui.progressBar.setVisible(False)

        seen_texts = set()
        indices_to_remove = set()
        for idx, text in texts:
            if not text:
                indices_to_remove.add(idx)
            elif not remove_empty_only:
                if text in seen_texts:
                    indices_to_remove.add(idx)
                else:
                    seen_texts.add(text)

        if not indices_to_remove:
            self.ui.imageListToolbarFrame.setEnabled(True)
            QMessageBox.information(self, title, "未发现需要移除的图片。")
            return

        self.ui.imageListScrollArea.setUpdatesEnabled(False)
        for idx in sorted(indices_to_remove, reverse=True):
            self.frame_paths.pop(idx)
        self._build_cards()
        self._flow_layout.invalidate()
        self._flow_layout.activate()
        self.ui.imageListScrollArea.setUpdatesEnabled(True)
        self.ui.labelImageCount.setText(f"共 {len(self.frame_paths)} 张截图")
        self._sync_select_all_button()

        self.ui.imageListToolbarFrame.setEnabled(True)
        QMessageBox.information(
            self, title,
            f"处理完成，已移除 {len(indices_to_remove)} 张图片。",
        )

    def _on_auto_deduplicate(self):
        self._run_ocr_batch("智能去重", remove_empty_only=False)

    def _on_undo_deduplicate(self):
        self._run_ocr_batch("去除空字幕", remove_empty_only=True)

    def _back_to_main_window(self):
        if self.main_window is not None:
            self.main_window.show()
            self.main_window.raise_()
            self.main_window.activateWindow()
        self.hide()
        self.deleteLater()

    def _on_back_to_video(self):
        reply = show_confirm(
            self, "返回上一页",
            "确定要返回到视频提取画面吗？",
        )
        if reply == QMessageBox.StandardButton.Yes:
            if self.main_window is not None:
                self.main_window.show()
                self.main_window.raise_()
                self.main_window.activateWindow()
            self.hide()
            self.deleteLater()
