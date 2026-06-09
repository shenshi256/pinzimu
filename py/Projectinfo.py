#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from PySide6.QtCore import QUrl
from PySide6.QtWidgets import QMainWindow
from py_gui.projectinfo_ui import Ui_ProjectInfo
from utils import COPYRIGHT, setup_window_title


class ProjectInfoWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_ProjectInfo()
        self.ui.setupUi(self)
        setup_window_title(self)
        self.ui.btnClose.clicked.connect(self.close)
        self._load_html()

    def _load_html(self):
        py_dir = os.path.dirname(os.path.abspath(__file__))
        html_path = os.path.join(py_dir, "project.html")
        self.ui.textBrowserInfo.setSource(QUrl.fromLocalFile(html_path))
