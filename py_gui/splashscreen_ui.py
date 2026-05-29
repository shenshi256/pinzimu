# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'splashscreen.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QMenuBar, QProgressBar, QPushButton,
    QSizePolicy, QSpacerItem, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_splashscreen(object):
    def setupUi(self, splashscreen):
        if not splashscreen.objectName():
            splashscreen.setObjectName(u"splashscreen")
        splashscreen.resize(500, 349)
        splashscreen.setStyleSheet(u"QMainWindow#splashscreen {\n"
"    background-color: rgb(124, 59, 237);\n"
"    border: 0px;\n"
"    border-radius: 20px;\n"
"}\n"
"QWidget#centralwidget {\n"
"    background-color: rgb(124, 59, 237);\n"
"    border: 0px;\n"
"    border-radius: 20px;\n"
"}\n"
"QFrame#cardFrame {\n"
"    background-color: rgb(124, 59, 237);\n"
"    border: 0px;\n"
"    border-radius: 20px;\n"
"}\n"
"QLabel#titleLabel {\n"
"    color: #FFFFFF;\n"
"    font: 700 40px \"Microsoft YaHei\";\n"
"}\n"
"QLabel#subTitleLabel {\n"
"    color: #FFFFFF;\n"
"    font: 15px \"Microsoft YaHei\";\n"
"}\n"
"QLabel#statusLabel {\n"
"    color:rgba(202, 202, 197, 0.9);\n"
"    font: 12px \"Microsoft YaHei\";\n"
"}\n"
"QProgressBar {\n"
"    border: 1px solid #FFFFFF;\n"
"    border-radius: 7px;\n"
"    background-color: rgba(10, 15, 26, 120);\n"
"    text-align: center;\n"
"    color: rgba(218, 248, 246, 255);\n"
"    font: 10px \"Microsoft YaHei\";\n"
"}\n"
"QProgressBar::chunk {\n"
"    border-radius: 6px;\n"
"    background-color: qlineargradi"
                        "ent(spread:pad, x1:0, y1:0, x2:1, y2:0,\n"
"      stop:0 rgba(124, 59, 237, 220),\n"
"      stop:1 rgba(59, 237, 230, 220));\n"
"}\n"
"QPushButton#closeButton {\n"
"    min-width: 28px;\n"
"    max-width: 28px;\n"
"    min-height: 28px;\n"
"    max-height: 28px;\n"
"    border-radius: 14px;\n"
"    border: 1px solid #FFFFFF;\n"
"    background-color: rgba(124, 59, 237, 70);\n"
"    color: rgba(235, 245, 255, 240);\n"
"    font: 700 14px \"Microsoft YaHei\";\n"
"}\n"
"QPushButton#closeButton:hover {\n"
"    background-color: rgba(124, 59, 237, 120);\n"
"}\n"
"QPushButton#closeButton:pressed {\n"
"    background-color: rgba(124, 59, 237, 160);\n"
"}\n"
"")
        self.centralwidget = QWidget(splashscreen)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutRoot = QVBoxLayout(self.centralwidget)
        self.verticalLayoutRoot.setObjectName(u"verticalLayoutRoot")
        self.verticalLayoutRoot.setContentsMargins(0, 0, 0, 0)
        self.closeButtonLayout = QHBoxLayout()
        self.closeButtonLayout.setObjectName(u"closeButtonLayout")
        self.closeButtonLayout.setContentsMargins(0, 16, 16, 0)
        self.closeBtnLeftSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.closeButtonLayout.addItem(self.closeBtnLeftSpacer)

        self.closeButton = QPushButton(self.centralwidget)
        self.closeButton.setObjectName(u"closeButton")
        self.closeButton.setMinimumSize(QSize(30, 30))
        self.closeButton.setMaximumSize(QSize(30, 30))

        self.closeButtonLayout.addWidget(self.closeButton)


        self.verticalLayoutRoot.addLayout(self.closeButtonLayout)

        self.cardWrapper = QHBoxLayout()
        self.cardWrapper.setObjectName(u"cardWrapper")
        self.cardWrapper.setContentsMargins(120, -1, 120, -1)
        self.cardFrame = QFrame(self.centralwidget)
        self.cardFrame.setObjectName(u"cardFrame")
        self.verticalLayoutCard = QVBoxLayout(self.cardFrame)
        self.verticalLayoutCard.setSpacing(14)
        self.verticalLayoutCard.setObjectName(u"verticalLayoutCard")
        self.verticalLayoutCard.setContentsMargins(0, 0, 0, 0)
        self.logoLabel = QLabel(self.cardFrame)
        self.logoLabel.setObjectName(u"logoLabel")
        self.logoLabel.setMinimumSize(QSize(96, 96))
        self.logoLabel.setMaximumSize(QSize(96, 96))
        self.logoLabel.setPixmap(QPixmap(u"../../imgs/logo.png"))
        self.logoLabel.setScaledContents(True)
        self.logoLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayoutCard.addWidget(self.logoLabel, 0, Qt.AlignHCenter)

        self.titleLabel = QLabel(self.cardFrame)
        self.titleLabel.setObjectName(u"titleLabel")
        self.titleLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayoutCard.addWidget(self.titleLabel)

        self.subTitleLabel = QLabel(self.cardFrame)
        self.subTitleLabel.setObjectName(u"subTitleLabel")
        self.subTitleLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayoutCard.addWidget(self.subTitleLabel)

        self.loadingProgressBar = QProgressBar(self.cardFrame)
        self.loadingProgressBar.setObjectName(u"loadingProgressBar")
        self.loadingProgressBar.setMinimumSize(QSize(0, 16))
        self.loadingProgressBar.setMaximumSize(QSize(16777215, 16))
        self.loadingProgressBar.setMinimum(0)
        self.loadingProgressBar.setMaximum(100)
        self.loadingProgressBar.setValue(0)
        self.loadingProgressBar.setTextVisible(True)

        self.verticalLayoutCard.addWidget(self.loadingProgressBar)

        self.statusLabel = QLabel(self.cardFrame)
        self.statusLabel.setObjectName(u"statusLabel")
        self.statusLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayoutCard.addWidget(self.statusLabel)


        self.cardWrapper.addWidget(self.cardFrame)


        self.verticalLayoutRoot.addLayout(self.cardWrapper)

        splashscreen.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(splashscreen)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 500, 17))
        splashscreen.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(splashscreen)
        self.statusbar.setObjectName(u"statusbar")
        splashscreen.setStatusBar(self.statusbar)

        self.retranslateUi(splashscreen)

        QMetaObject.connectSlotsByName(splashscreen)
    # setupUi

    def retranslateUi(self, splashscreen):
        splashscreen.setWindowTitle(QCoreApplication.translate("splashscreen", u"\u62fc\u5b57\u5e55 - \u542f\u52a8\u4e2d", None))
        self.closeButton.setText(QCoreApplication.translate("splashscreen", u"X", None))
        self.titleLabel.setText(QCoreApplication.translate("splashscreen", u"\u62fc\u5b57\u5e55", None))
        self.subTitleLabel.setText(QCoreApplication.translate("splashscreen", u"\u6b63\u5728\u51c6\u5907\u5b57\u5e55\u957f\u56fe\u5f15\u64ce...", None))
        self.loadingProgressBar.setFormat(QCoreApplication.translate("splashscreen", u"%p%", None))
        self.statusLabel.setText(QCoreApplication.translate("splashscreen", u"\u521d\u59cb\u5316\u7ec4\u4ef6\u4e2d \u00b7 \u8bf7\u7a0d\u5019", None))
    # retranslateUi

