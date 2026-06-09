# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'projectinfo.ui'
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
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QTextBrowser, QVBoxLayout, QWidget)

class Ui_ProjectInfo(object):
    def setupUi(self, ProjectInfo):
        if not ProjectInfo.objectName():
            ProjectInfo.setObjectName(u"ProjectInfo")
        ProjectInfo.resize(720, 560)
        ProjectInfo.setMinimumSize(QSize(520, 400))
        ProjectInfo.setStyleSheet(u"QMainWindow {\n"
"    background-color: #FFFFFF;\n"
"    font-family: \"Microsoft YaHei\", \"Segoe UI\", sans-serif;\n"
"}\n"
"QLabel {\n"
"    color: #111827;\n"
"}")
        self.centralwidget = QWidget(ProjectInfo)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_main = QVBoxLayout(self.centralwidget)
        self.verticalLayout_main.setSpacing(0)
        self.verticalLayout_main.setObjectName(u"verticalLayout_main")
        self.verticalLayout_main.setContentsMargins(0, 0, 0, 0)
        self.headerFrame = QFrame(self.centralwidget)
        self.headerFrame.setObjectName(u"headerFrame")
        self.headerFrame.setMinimumSize(QSize(0, 56))
        self.headerFrame.setMaximumSize(QSize(16777215, 56))
        self.headerFrame.setStyleSheet(u"#headerFrame {\n"
"    background-color: #FFFFFF;\n"
"    border-bottom: 1px solid #E5E7EB;\n"
"}")
        self.headerFrame.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_header = QHBoxLayout(self.headerFrame)
        self.horizontalLayout_header.setObjectName(u"horizontalLayout_header")
        self.horizontalLayout_header.setContentsMargins(16, 0, 16, 0)
        self.labelTitle = QLabel(self.headerFrame)
        self.labelTitle.setObjectName(u"labelTitle")
        self.labelTitle.setAlignment(Qt.AlignCenter)
        self.labelTitle.setStyleSheet(u"#labelTitle {\n"
"    color: #111827;\n"
"    font-size: 18px;\n"
"    font-weight: 700;\n"
"}")

        self.horizontalLayout_header.addWidget(self.labelTitle)


        self.verticalLayout_main.addWidget(self.headerFrame)

        self.contentContainer = QFrame(self.centralwidget)
        self.contentContainer.setObjectName(u"contentContainer")
        self.contentContainer.setStyleSheet(u"#contentContainer {\n"
"    background-color: #FFFFFF;\n"
"}")
        self.contentContainer.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_content = QVBoxLayout(self.contentContainer)
        self.verticalLayout_content.setSpacing(16)
        self.verticalLayout_content.setObjectName(u"verticalLayout_content")
        self.verticalLayout_content.setContentsMargins(20, 16, 20, 16)
        self.textBrowserInfo = QTextBrowser(self.contentContainer)
        self.textBrowserInfo.setObjectName(u"textBrowserInfo")
        self.textBrowserInfo.setOpenExternalLinks(True)
        self.textBrowserInfo.setStyleSheet(u"QTextBrowser {\n"
"    background-color: #F9FAFB;\n"
"    border: 1px solid #E5E7EB;\n"
"    border-radius: 8px;\n"
"    padding: 12px;\n"
"    font-size: 14px;\n"
"    color: #111827;\n"
"}\n"
"QScrollBar:vertical {\n"
"    background: transparent;\n"
"    width: 6px;\n"
"    margin: 0;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"    background: #D1D5DB;\n"
"    border-radius: 3px;\n"
"    min-height: 30px;\n"
"}\n"
"QScrollBar::handle:vertical:hover {\n"
"    background: #9CA3AF;\n"
"}\n"
"QScrollBar::add-line:vertical,\n"
"QScrollBar::sub-line:vertical {\n"
"    height: 0px;\n"
"}")

        self.verticalLayout_content.addWidget(self.textBrowserInfo)

        self.labelFooter = QLabel(self.contentContainer)
        self.labelFooter.setObjectName(u"labelFooter")
        self.labelFooter.setOpenExternalLinks(True)
        self.labelFooter.setStyleSheet(u"#labelFooter {\n"
"    color: #6B7280;\n"
"    font-size: 14px;\n"
"}")
        self.labelFooter.setAlignment(Qt.AlignCenter)

        self.verticalLayout_content.addWidget(self.labelFooter)

        self.horizontalLayout_footer = QHBoxLayout()
        self.horizontalLayout_footer.setSpacing(0)
        self.horizontalLayout_footer.setObjectName(u"horizontalLayout_footer")
        self.horizontalSpacer_footerLeft = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_footer.addItem(self.horizontalSpacer_footerLeft)

        self.btnClose = QPushButton(self.contentContainer)
        self.btnClose.setObjectName(u"btnClose")
        self.btnClose.setMinimumSize(QSize(120, 40))
        self.btnClose.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnClose.setStyleSheet(u"#btnClose {\n"
"    background-color: #7C3BED;\n"
"    color: #FFFFFF;\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"    padding: 0 20px;\n"
"    font-size: 14px;\n"
"    font-weight: 600;\n"
"}\n"
"#btnClose:hover {\n"
"    background-color: #6D28D9;\n"
"}\n"
"#btnClose:pressed {\n"
"    background-color: #5B21B6;\n"
"}")

        self.horizontalLayout_footer.addWidget(self.btnClose)

        self.horizontalSpacer_footerRight = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_footer.addItem(self.horizontalSpacer_footerRight)


        self.verticalLayout_content.addLayout(self.horizontalLayout_footer)


        self.verticalLayout_main.addWidget(self.contentContainer)

        ProjectInfo.setCentralWidget(self.centralwidget)

        self.retranslateUi(ProjectInfo)

        QMetaObject.connectSlotsByName(ProjectInfo)
    # setupUi

    def retranslateUi(self, ProjectInfo):
        ProjectInfo.setWindowTitle(QCoreApplication.translate("ProjectInfo", u"\u9879\u76ee\u4ecb\u7ecd", None))
        self.labelTitle.setText(QCoreApplication.translate("ProjectInfo", u"\u9879\u76ee\u4ecb\u7ecd", None))
        self.textBrowserInfo.setHtml(QCoreApplication.translate("ProjectInfo", u"<h2>\u9879\u76ee\u4ecb\u7ecd</h2><p>\u5728\u6b64\u5904\u586b\u5199\u9879\u76ee\u7684 HTML \u4ecb\u7ecd\u5185\u5bb9\u3002</p>", None))
        self.labelFooter.setText(QCoreApplication.translate("ProjectInfo", u"<a href=\"https://www.yuanheyuekeji.com/\" style=\"text-decoration:none; color:#6B7280;\">\u00a9 2026 \u62fc\u5b57\u5e55 - \u5feb\u901f\u751f\u6210\u8fde\u7eed\u5b57\u5e55\u957f\u56fe</a>", None))
        self.btnClose.setText(QCoreApplication.translate("ProjectInfo", u"\u5173\u95ed", None))
    # retranslateUi

