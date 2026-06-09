# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settings.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGroupBox, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QMenuBar,
    QPushButton, QRadioButton, QSizePolicy, QSpacerItem,
    QStatusBar, QVBoxLayout, QWidget)

class Ui_SettingsWindow(object):
    def setupUi(self, SettingsWindow):
        if not SettingsWindow.objectName():
            SettingsWindow.setObjectName(u"SettingsWindow")
        SettingsWindow.resize(480, 420)
        SettingsWindow.setMinimumSize(QSize(420, 380))
        SettingsWindow.setStyleSheet(u"QMainWindow {\n"
"    background-color: #F9FAFB;\n"
"}")
        self.centralwidget = QWidget(SettingsWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_main = QVBoxLayout(self.centralwidget)
        self.verticalLayout_main.setSpacing(16)
        self.verticalLayout_main.setObjectName(u"verticalLayout_main")
        self.verticalLayout_main.setContentsMargins(24, 24, 24, 24)
        self.frameContent = QFrame(self.centralwidget)
        self.frameContent.setObjectName(u"frameContent")
        self.frameContent.setStyleSheet(u"#frameContent {\n"
"    background-color: #FFFFFF;\n"
"    border: 1px solid #E5E7EB;\n"
"    border-radius: 12px;\n"
"    padding: 0px;\n"
"}")
        self.verticalLayout_content = QVBoxLayout(self.frameContent)
        self.verticalLayout_content.setSpacing(20)
        self.verticalLayout_content.setObjectName(u"verticalLayout_content")
        self.verticalLayout_content.setContentsMargins(20, 20, 20, 20)
        self.labelTitle = QLabel(self.frameContent)
        self.labelTitle.setObjectName(u"labelTitle")
        self.labelTitle.setStyleSheet(u"color: #111827;\n"
"font-size: 18px;\n"
"font-weight: 700;")

        self.verticalLayout_content.addWidget(self.labelTitle)

        self.groupLogging = QGroupBox(self.frameContent)
        self.groupLogging.setObjectName(u"groupLogging")
        self.groupLogging.setMinimumSize(QSize(0, 70))
        self.groupLogging.setStyleSheet(u"QGroupBox {\n"
"    font-size: 14px;\n"
"    font-weight: 600;\n"
"    color: #374151;\n"
"    border: 1px solid #E5E7EB;\n"
"    border-radius: 8px;\n"
"    margin-top: 10px;\n"
"    padding: 8px;\n"
"}\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top left;\n"
"    padding: 0 8px;\n"
"    background-color: #FFFFFF;\n"
"}")
        self.horizontalLayout_logging = QHBoxLayout(self.groupLogging)
        self.horizontalLayout_logging.setSpacing(24)
        self.horizontalLayout_logging.setObjectName(u"horizontalLayout_logging")
        self.radioLogYes = QRadioButton(self.groupLogging)
        self.radioLogYes.setObjectName(u"radioLogYes")
        self.radioLogYes.setStyleSheet(u"QRadioButton {\n"
"    font-size: 14px;\n"
"    color: #374151;\n"
"}\n"
"QRadioButton::indicator {\n"
"    width: 18px;\n"
"    height: 18px;\n"
"}")
        self.radioLogYes.setChecked(True)

        self.horizontalLayout_logging.addWidget(self.radioLogYes)

        self.radioLogNo = QRadioButton(self.groupLogging)
        self.radioLogNo.setObjectName(u"radioLogNo")
        self.radioLogNo.setStyleSheet(u"QRadioButton {\n"
"    font-size: 14px;\n"
"    color: #374151;\n"
"}\n"
"QRadioButton::indicator {\n"
"    width: 18px;\n"
"    height: 18px;\n"
"}")

        self.horizontalLayout_logging.addWidget(self.radioLogNo)

        self.horizontalSpacer_logging = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_logging.addItem(self.horizontalSpacer_logging)


        self.verticalLayout_content.addWidget(self.groupLogging)

        self.frameImageCount = QFrame(self.frameContent)
        self.frameImageCount.setObjectName(u"frameImageCount")
        self.horizontalLayout_imageCount = QHBoxLayout(self.frameImageCount)
        self.horizontalLayout_imageCount.setSpacing(12)
        self.horizontalLayout_imageCount.setObjectName(u"horizontalLayout_imageCount")
        self.horizontalLayout_imageCount.setContentsMargins(-1, 10, -1, -1)
        self.labelImageCount = QLabel(self.frameImageCount)
        self.labelImageCount.setObjectName(u"labelImageCount")
        self.labelImageCount.setMinimumSize(QSize(100, 0))
        self.labelImageCount.setStyleSheet(u"color: #374151;\n"
"font-size: 14px;\n"
"font-weight: 500;")

        self.horizontalLayout_imageCount.addWidget(self.labelImageCount)

        self.editImageCount = QLineEdit(self.frameImageCount)
        self.editImageCount.setObjectName(u"editImageCount")
        self.editImageCount.setMinimumSize(QSize(120, 36))
        self.editImageCount.setMaximumSize(QSize(16777215, 36))
        self.editImageCount.setStyleSheet(u"QLineEdit {\n"
"    border: 1px solid #D1D5DB;\n"
"    border-radius: 6px;\n"
"    padding: 6px 10px;\n"
"    font-size: 14px;\n"
"    color: #374151;\n"
"    background-color: #FFFFFF;\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 1px solid #7C3BED;\n"
"}")

        self.horizontalLayout_imageCount.addWidget(self.editImageCount)

        self.horizontalSpacer_imageCount = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_imageCount.addItem(self.horizontalSpacer_imageCount)


        self.verticalLayout_content.addWidget(self.frameImageCount)

        self.frameVideoFrames = QFrame(self.frameContent)
        self.frameVideoFrames.setObjectName(u"frameVideoFrames")
        self.horizontalLayout_videoFrames = QHBoxLayout(self.frameVideoFrames)
        self.horizontalLayout_videoFrames.setSpacing(12)
        self.horizontalLayout_videoFrames.setObjectName(u"horizontalLayout_videoFrames")
        self.labelVideoFrames = QLabel(self.frameVideoFrames)
        self.labelVideoFrames.setObjectName(u"labelVideoFrames")
        self.labelVideoFrames.setMinimumSize(QSize(100, 0))
        self.labelVideoFrames.setStyleSheet(u"color: #374151;\n"
"font-size: 14px;\n"
"font-weight: 500;")

        self.horizontalLayout_videoFrames.addWidget(self.labelVideoFrames)

        self.editVideoFrames = QLineEdit(self.frameVideoFrames)
        self.editVideoFrames.setObjectName(u"editVideoFrames")
        self.editVideoFrames.setMinimumSize(QSize(120, 36))
        self.editVideoFrames.setMaximumSize(QSize(16777215, 36))
        self.editVideoFrames.setStyleSheet(u"QLineEdit {\n"
"    border: 1px solid #D1D5DB;\n"
"    border-radius: 6px;\n"
"    padding: 6px 10px;\n"
"    font-size: 14px;\n"
"    color: #374151;\n"
"    background-color: #FFFFFF;\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 1px solid #7C3BED;\n"
"}")

        self.horizontalLayout_videoFrames.addWidget(self.editVideoFrames)

        self.horizontalSpacer_videoFrames = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_videoFrames.addItem(self.horizontalSpacer_videoFrames)


        self.verticalLayout_content.addWidget(self.frameVideoFrames)

        self.verticalSpacer_inner = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_content.addItem(self.verticalSpacer_inner)


        self.verticalLayout_main.addWidget(self.frameContent)

        self.frameFooter = QFrame(self.centralwidget)
        self.frameFooter.setObjectName(u"frameFooter")
        self.horizontalLayout_footer = QHBoxLayout(self.frameFooter)
        self.horizontalLayout_footer.setObjectName(u"horizontalLayout_footer")
        self.horizontalLayout_footer.setContentsMargins(0, 0, 0, 0)
        self.labelFooter = QLabel(self.frameFooter)
        self.labelFooter.setObjectName(u"labelFooter")
        self.labelFooter.setOpenExternalLinks(True)
        self.labelFooter.setStyleSheet(u"color: #9CA3AF;\n"
"font-size: 12px;")

        self.horizontalLayout_footer.addWidget(self.labelFooter)

        self.horizontalSpacer_footer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_footer.addItem(self.horizontalSpacer_footer)

        self.btnSave = QPushButton(self.frameFooter)
        self.btnSave.setObjectName(u"btnSave")
        self.btnSave.setMinimumSize(QSize(100, 40))
        self.btnSave.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnSave.setStyleSheet(u"#btnSave {\n"
"    background-color: #7C3BED;\n"
"    color: #FFFFFF;\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"    font-size: 14px;\n"
"    font-weight: 600;\n"
"    padding: 0 24px;\n"
"}\n"
"#btnSave:hover {\n"
"    background-color: #6D28D9;\n"
"}")

        self.horizontalLayout_footer.addWidget(self.btnSave)


        self.verticalLayout_main.addWidget(self.frameFooter)

        SettingsWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(SettingsWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 480, 17))
        SettingsWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(SettingsWindow)
        self.statusbar.setObjectName(u"statusbar")
        SettingsWindow.setStatusBar(self.statusbar)

        self.retranslateUi(SettingsWindow)

        QMetaObject.connectSlotsByName(SettingsWindow)
    # setupUi

    def retranslateUi(self, SettingsWindow):
        SettingsWindow.setWindowTitle(QCoreApplication.translate("SettingsWindow", u"\u8bbe\u7f6e", None))
        self.labelTitle.setText(QCoreApplication.translate("SettingsWindow", u"\u5e94\u7528\u8bbe\u7f6e", None))
        self.groupLogging.setTitle(QCoreApplication.translate("SettingsWindow", u"\u65e5\u5fd7\u8bb0\u5f55", None))
        self.radioLogYes.setText(QCoreApplication.translate("SettingsWindow", u"\u662f", None))
        self.radioLogNo.setText(QCoreApplication.translate("SettingsWindow", u"\u5426", None))
        self.labelImageCount.setText(QCoreApplication.translate("SettingsWindow", u"\u56fe\u7247\u6570\u91cf", None))
        self.editImageCount.setPlaceholderText(QCoreApplication.translate("SettingsWindow", u"1 - 999999", None))
        self.editImageCount.setText(QCoreApplication.translate("SettingsWindow", u"50", None))
        self.labelVideoFrames.setText(QCoreApplication.translate("SettingsWindow", u"\u89c6\u9891\u5e27\u6570\u91cf", None))
        self.editVideoFrames.setPlaceholderText(QCoreApplication.translate("SettingsWindow", u"1 - 999999", None))
        self.editVideoFrames.setText(QCoreApplication.translate("SettingsWindow", u"200", None))
        self.labelFooter.setText(QCoreApplication.translate("SettingsWindow", u"<a href=\"https://www.yuanheyuekeji.com/\" style=\"text-decoration:none; color:#9CA3AF;\">\u00a9 2026 \u62fc\u5b57\u5e55 - \u5feb\u901f\u751f\u6210\u8fde\u7eed\u5b57\u5e55\u957f\u56fe</a>", None))
        self.btnSave.setText(QCoreApplication.translate("SettingsWindow", u"\u4fdd\u5b58", None))
    # retranslateUi

