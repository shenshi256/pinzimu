#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------------
# @Time    : 2026/5/28 17:48
# @Author  : WXY
# @File    : ImageDialog.py
# @PROJECT_NAME: 20260525_pinzimu_gui
# @PRODUCT_NAME: PyCharm
# -------------------------------------------------------------------------------
from PIL import Image
from PIL.ImageQt import ImageQt

from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout, QScrollArea,
    QLabel, QPushButton, QWidget, QFileDialog, QMessageBox,
)

from py.utils import setup_window_icon, get_last_save_dir, set_last_save_dir


def show_image_dialog(parent, pil_image, title="字幕长图预览"):
    dialog = QDialog(parent)
    dialog.setWindowTitle(title)
    dialog.resize(900, 700)
    dialog.setWindowModality(Qt.WindowModality.ApplicationModal)
    setup_window_icon(dialog)

    layout = QVBoxLayout(dialog)
    layout.setContentsMargins(0, 0, 0, 0)
    layout.setSpacing(0)

    stitched_rgb = pil_image.convert("RGB")
    qimage = ImageQt(stitched_rgb)
    original_pixmap = QPixmap.fromImage(qimage)

    image_label = QLabel()
    image_label.setPixmap(original_pixmap)
    image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
    image_label.setStyleSheet("background-color: #F3F4F6;")

    zoom_state = {"scale": 1.0, "auto_fit": True}

    scroll = QScrollArea(dialog)
    scroll.setWidgetResizable(False)
    scroll.setAlignment(Qt.AlignmentFlag.AlignCenter)
    scroll.setWidget(image_label)
    scroll.setStyleSheet("QScrollArea { border: none; background-color: #F3F4F6; }")

    def update_zoom():
        scaled = original_pixmap.scaled(
            original_pixmap.size() * zoom_state["scale"],
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation,
        )
        image_label.setPixmap(scaled)
        image_label.adjustSize()

        h_bar = scroll.horizontalScrollBar()
        v_bar = scroll.verticalScrollBar()
        vp = scroll.viewport()

        scaled_width = scaled.width()
        scaled_height = scaled.height()

        h_bar.setValue((scaled_width - vp.width()) // 2)
        v_bar.setValue((scaled_height - vp.height()) // 2)

    drag_state = {"dragging": False, "start_pos": None, "start_h": 0, "start_v": 0}

    def scroll_wheel_event(event):
        if event.modifiers() == Qt.KeyboardModifier.ControlModifier:
            delta = event.angleDelta().y()
            if delta > 0:
                new_scale = zoom_state["scale"] * 1.15
                if new_scale <= 5.0:
                    zoom_state["scale"] = new_scale
                    zoom_state["auto_fit"] = False
                    update_zoom()
            else:
                new_scale = zoom_state["scale"] / 1.15
                if new_scale >= 0.1:
                    zoom_state["scale"] = new_scale
                    zoom_state["auto_fit"] = False
                    update_zoom()
        else:
            QScrollArea.wheelEvent(scroll, event)

    def image_mouse_press(event):
        if event.button() == Qt.MouseButton.LeftButton:
            drag_state["dragging"] = True
            drag_state["start_pos"] = event.pos()
            drag_state["start_h"] = scroll.horizontalScrollBar().value()
            drag_state["start_v"] = scroll.verticalScrollBar().value()
            image_label.setCursor(Qt.CursorShape.ClosedHandCursor)

    def image_mouse_move(event):
        if drag_state["dragging"]:
            delta = event.pos() - drag_state["start_pos"]
            scroll.horizontalScrollBar().setValue(drag_state["start_h"] - delta.x())
            scroll.verticalScrollBar().setValue(drag_state["start_v"] - delta.y())

    def image_mouse_release(event):
        if event.button() == Qt.MouseButton.LeftButton:
            drag_state["dragging"] = False
            image_label.setCursor(Qt.CursorShape.OpenHandCursor)

    image_label.mousePressEvent = image_mouse_press
    image_label.mouseMoveEvent = image_mouse_move
    image_label.mouseReleaseEvent = image_mouse_release
    image_label.setCursor(Qt.CursorShape.OpenHandCursor)

    scroll.wheelEvent = scroll_wheel_event

    def fit_to_width():
        if zoom_state["auto_fit"]:
            view_width = scroll.viewport().width() - 4
            img_width = original_pixmap.width()
            if img_width > 0:
                zoom_state["scale"] = view_width / img_width
                update_zoom()

    scroll.resizeEvent = lambda event: (
        QScrollArea.resizeEvent(scroll, event),
        fit_to_width(),
    )

    layout.addWidget(scroll)

    btn_row = QWidget()
    btn_layout = QHBoxLayout(btn_row)
    btn_layout.setContentsMargins(16, 12, 16, 12)
    btn_layout.setSpacing(12)

    zoom_label = QLabel("ctrl + 滚轮缩放图片")
    zoom_label.setStyleSheet("color: #9CA3AF; font-size: 13px;")
    btn_layout.addWidget(zoom_label)
    btn_layout.addStretch()

    btn_save = QPushButton("保存图片")
    btn_save.setMinimumHeight(40)
    btn_save.setCursor(Qt.CursorShape.PointingHandCursor)
    btn_save.setStyleSheet(
        "QPushButton { background-color: #7C3BED; color: #FFFFFF; border: none; "
        "border-radius: 8px; font-size: 15px; font-weight: 600; padding: 0 24px; }"
        "QPushButton:hover { background-color: #6D28D9; }"
    )
    btn_layout.addWidget(btn_save)
    layout.addWidget(btn_row)

    def save_image():
        from datetime import datetime
        from os import path
        default_name = datetime.now().strftime("%Y%m%d%H%M%S") + ".png"
        last_dir = get_last_save_dir()
        if last_dir and path.exists(last_dir):
            default_path = path.join(last_dir, default_name)
        else:
            default_path = default_name
        file_path, _ = QFileDialog.getSaveFileName(
            dialog, "保存字幕长图", default_path,
            "PNG (*.png);;JPEG (*.jpg *.jpeg)",
        )
        if file_path:
            stitched_rgb.save(file_path)
            set_last_save_dir(path.dirname(file_path))
            QMessageBox.information(dialog, "保存成功", f"字幕长图已保存到：\n{file_path}")

    btn_save.clicked.connect(save_image)
    fit_to_width()
    dialog.exec()


def stitch_and_show_dialog(parent, image_paths, positions_dict, title="字幕长图预览", width_mode=0, current_index=0):
    """根据图片路径和位置字典生成拼接长图并弹窗显示

    Args:
        parent: 父窗口
        image_paths: 图片路径列表
        positions_dict: {index: (top_pct, bottom_pct)} 每张图的字幕线位置
        title: 弹窗标题
        width_mode: 0=不强制 1=按最窄 2=按最宽 3=按当前
        current_index: 当前图片索引，width_mode=3时使用
    """
    if not image_paths:
        return

    images = []
    cropped_images = []
    for idx, path in enumerate(image_paths):
        img = Image.open(path)
        images.append(img)
        img_w, img_h = img.size
        top_pct, bottom_pct = positions_dict.get(idx, (80.0, 99.0))
        top_y = int(img_h * top_pct / 100.0)
        bottom_y = int(img_h * bottom_pct / 100.0)
        top_y = max(0, min(img_h - 1, top_y))
        bottom_y = max(top_y + 1, min(img_h, bottom_y))
        if idx == 0:
            cropped = img.crop((0, 0, img_w, bottom_y))
        else:
            cropped = img.crop((0, top_y, img_w, bottom_y))
        cropped_images.append(cropped)

    widths = [img.size[0] for img in images]
    if width_mode == 0:
        target_width = max(widths)
    elif width_mode == 1:
        target_width = min(widths)
    elif width_mode == 2:
        target_width = max(widths)
    elif width_mode == 3:
        ci = max(0, min(current_index, len(widths) - 1))
        target_width = widths[ci]
    else:
        target_width = max(widths)

    if width_mode != 0:
        for i in range(len(cropped_images)):
            cw, ch = cropped_images[i].size
            if cw != target_width:
                new_h = int(ch * target_width / cw)
                cropped_images[i] = cropped_images[i].resize(
                    (target_width, new_h), Image.LANCZOS
                )

    total_height = sum(img.size[1] for img in cropped_images)
    stitched = Image.new("RGB", (target_width, total_height), (255, 255, 255))
    y_offset = 0
    for img in cropped_images:
        stitched.paste(img, (0, y_offset))
        y_offset += img.size[1]

    show_image_dialog(parent, stitched, title)
