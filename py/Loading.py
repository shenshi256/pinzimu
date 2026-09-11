#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------------
# @Time    : 2026/5/28 21:44
# @Author  : WXY
# @File    : Loading.py
# @PROJECT_NAME: 20260525_pinzimu_gui
# @PRODUCT_NAME: PyCharm
# -------------------------------------------------------------------------------
from PySide6.QtCore import Qt, QTimer, QRectF, QPointF
from PySide6.QtGui import QPainter, QColor, QPen, QFont
from PySide6.QtWidgets import QWidget


class LoadingOverlay(QWidget):
    def __init__(self, parent=None, color="#606c71", text="加载中..."):
        super().__init__(parent)
        self._angle = 0
        self._color = QColor(color)
        self._text = text
        self._timer = QTimer(self)
        self._timer.timeout.connect(self._rotate)
        self.setAttribute(Qt.WidgetAttribute.WA_TransparentForMouseEvents, False)
        self.setVisible(False)

    def start(self):
        if self.parent():
            self.setGeometry(self.parent().rect())
            self.parent().installEventFilter(self)
        self._angle = 0
        self._timer.start(50)
        self.show()
        self.raise_()

    def stop(self):
        self._timer.stop()
        self.hide()

    def set_color(self, color):
        self._color = QColor(color)
        self.update()

    def set_text(self, text):
        self._text = text
        self.update()

    def _rotate(self):
        self._angle = (self._angle + 30) % 360
        self.update()

    def eventFilter(self, watched, event):
        from PySide6.QtCore import QEvent
        if watched == self.parent() and event.type() == QEvent.Type.Resize:
            self.setGeometry(watched.rect())
        return super().eventFilter(watched, event)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        painter.fillRect(self.rect(), QColor(255, 255, 255, 200))

        center = QPointF(self.width() / 2.0, self.height() / 2.0)
        radius = min(self.width(), self.height()) / 6.0
        radius = max(radius, 20)

        pen = QPen()
        pen.setWidth(3)
        pen.setCapStyle(Qt.PenCapStyle.RoundCap)

        arc_count = 12
        for i in range(arc_count):
            alpha = max(30, 255 - i * 20)
            c = QColor(self._color)
            c.setAlpha(alpha)
            pen.setColor(c)
            painter.setPen(pen)

            painter.save()
            painter.translate(center)
            painter.rotate(self._angle + i * 30)
            start_angle = 0
            span_angle = 20 * 16
            arc_rect = QRectF(-radius, -radius, radius * 2, radius * 2)
            painter.drawArc(arc_rect, start_angle, span_angle)
            painter.restore()

        if self._text:
            font = QFont("Microsoft YaHei", 11)
            painter.setFont(font)
            painter.setPen(QColor("#6B7280"))
            text_rect = self.rect()
            text_rect.setTop(int(center.y() + radius + 16))
            painter.drawText(text_rect, Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignTop, self._text)

        painter.end()
