# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
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
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1245, 721)
        MainWindow.setMinimumSize(QSize(800, 600))
        MainWindow.setStyleSheet(u"QMainWindow {\n"
"    background-color: #FFFFFF;\n"
"    font-family: \"Microsoft YaHei\", \"Segoe UI\", sans-serif;\n"
"}\n"
"QLabel {\n"
"    color: #111827;\n"
"}")
        self.centralWidget = QWidget(MainWindow)
        self.centralWidget.setObjectName(u"centralWidget")
        self.centralWidget.setStyleSheet(u"#centralWidget {\n"
"    background-color: #FFFFFF;\n"
"}")
        self.verticalLayout_main = QVBoxLayout(self.centralWidget)
        self.verticalLayout_main.setSpacing(0)
        self.verticalLayout_main.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_main.setObjectName(u"verticalLayout_main")
        self.verticalLayout_main.setContentsMargins(0, 0, 0, 0)
        self.headerFrame = QFrame(self.centralWidget)
        self.headerFrame.setObjectName(u"headerFrame")
        self.headerFrame.setMinimumSize(QSize(0, 56))
        self.headerFrame.setMaximumSize(QSize(16777215, 56))
        self.headerFrame.setStyleSheet(u"#headerFrame {\n"
"    background-color: #FFFFFF;\n"
"    border-bottom: 1px solid #E5E7EB;\n"
"}")
        self.headerFrame.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_header = QHBoxLayout(self.headerFrame)
        self.horizontalLayout_header.setSpacing(8)
        self.horizontalLayout_header.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_header.setObjectName(u"horizontalLayout_header")
        self.horizontalLayout_header.setContentsMargins(12, 10, 12, 10)
        self.logoIconLabel = QLabel(self.headerFrame)
        self.logoIconLabel.setObjectName(u"logoIconLabel")
        self.logoIconLabel.setMinimumSize(QSize(40, 40))
        self.logoIconLabel.setMaximumSize(QSize(40, 40))
        self.logoIconLabel.setStyleSheet(u"#logoIconLabel {\n"
"    border-radius: 8px;\n"
"}")
        self.logoIconLabel.setPixmap(QPixmap(u"imgs/logo.png"))
        self.logoIconLabel.setScaledContents(True)
        self.logoIconLabel.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_header.addWidget(self.logoIconLabel)

        self.logoLabel = QLabel(self.headerFrame)
        self.logoLabel.setObjectName(u"logoLabel")
        self.logoLabel.setStyleSheet(u"#logoLabel {\n"
"    color: #111827;\n"
"    font-size: 26px;\n"
"    font-weight: 800;\n"
"}")

        self.horizontalLayout_header.addWidget(self.logoLabel)

        self.horizontalSpacer_header = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_header.addItem(self.horizontalSpacer_header)

        self.btnSettings = QPushButton(self.headerFrame)
        self.btnSettings.setObjectName(u"btnSettings")
        self.btnSettings.setMinimumSize(QSize(100, 36))
        self.btnSettings.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnSettings.setStyleSheet(u"#btnSettings {\n"
"    background-color: #FFFFFF;\n"
"    color: #374151;\n"
"    border: 1px solid #E5E7EB;\n"
"    border-radius: 6px;\n"
"    padding: 0 16px;\n"
"    font-size: 14px;\n"
"    font-weight: 500;\n"
"}\n"
"#btnSettings:hover {\n"
"    background-color: #F9FAFB;\n"
"}")

        self.horizontalLayout_header.addWidget(self.btnSettings)

        self.btnProjectInfo = QPushButton(self.headerFrame)
        self.btnProjectInfo.setObjectName(u"btnProjectInfo")
        self.btnProjectInfo.setMinimumSize(QSize(100, 36))
        self.btnProjectInfo.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnProjectInfo.setStyleSheet(u"#btnProjectInfo {\n"
"    background-color: #FFFFFF;\n"
"    color: #374151;\n"
"    border: 1px solid #E5E7EB;\n"
"    border-radius: 6px;\n"
"    padding: 0 16px;\n"
"    font-size: 14px;\n"
"    font-weight: 500;\n"
"}\n"
"#btnProjectInfo:hover {\n"
"    background-color: #F9FAFB;\n"
"}")

        self.horizontalLayout_header.addWidget(self.btnProjectInfo)


        self.verticalLayout_main.addWidget(self.headerFrame)

        self.contentContainer = QWidget(self.centralWidget)
        self.contentContainer.setObjectName(u"contentContainer")
        self.contentContainer.setStyleSheet(u"#contentContainer {\n"
"    background-color: #FFFFFF;\n"
"}")
        self.verticalLayout_contentOuter = QVBoxLayout(self.contentContainer)
        self.verticalLayout_contentOuter.setSpacing(32)
        self.verticalLayout_contentOuter.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_contentOuter.setObjectName(u"verticalLayout_contentOuter")
        self.verticalLayout_contentOuter.setContentsMargins(0, 32, 0, 30)
        self.verticalSpacer_uploadTop = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_contentOuter.addItem(self.verticalSpacer_uploadTop)

        self.horizontalLayout_uploadWrap = QHBoxLayout()
        self.horizontalLayout_uploadWrap.setSpacing(0)
        self.horizontalLayout_uploadWrap.setObjectName(u"horizontalLayout_uploadWrap")
        self.horizontalSpacer_uploadLeft = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_uploadWrap.addItem(self.horizontalSpacer_uploadLeft)

        self.uploadFrame = QFrame(self.contentContainer)
        self.uploadFrame.setObjectName(u"uploadFrame")
        self.uploadFrame.setMinimumSize(QSize(896, 404))
        self.uploadFrame.setMaximumSize(QSize(896, 404))
        self.uploadFrame.setStyleSheet(u"#uploadFrame {\n"
"    background-color: #FFFFFF;\n"
"    border: 2px dashed #E5E7EB;\n"
"    border-radius: 12px;\n"
"}")
        self.uploadFrame.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_upload = QVBoxLayout(self.uploadFrame)
        self.verticalLayout_upload.setSpacing(0)
        self.verticalLayout_upload.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_upload.setObjectName(u"verticalLayout_upload")
        self.verticalLayout_upload.setContentsMargins(0, 32, 0, 32)
        self.horizontalLayout_modeButtons = QHBoxLayout()
        self.horizontalLayout_modeButtons.setSpacing(16)
        self.horizontalLayout_modeButtons.setObjectName(u"horizontalLayout_modeButtons")
        self.horizontalSpacer_modeLeft = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_modeButtons.addItem(self.horizontalSpacer_modeLeft)

        self.imageModeFrame = QFrame(self.uploadFrame)
        self.imageModeFrame.setObjectName(u"imageModeFrame")
        self.imageModeFrame.setMinimumSize(QSize(92, 144))
        self.imageModeFrame.setMaximumSize(QSize(92, 144))
        self.imageModeFrame.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.imageModeFrame.setStyleSheet(u"#imageModeFrame {\n"
"    background-color: #F5F0FF;\n"
"    border: 2px solid #7C3BED;\n"
"    border-radius: 8px;\n"
"}\n"
"#imageModeIconBg {\n"
"    background-color: #DDD0FF;\n"
"    border-radius: 22px;\n"
"}\n"
"#imageModeTitle {\n"
"    color: #7C3BED;\n"
"    font-size: 14px;\n"
"}\n"
"#imageModeSubTitle {\n"
"    color: #4B5563;\n"
"    font-size: 12px;\n"
"}")
        self.imageModeFrame.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_imageMode = QVBoxLayout(self.imageModeFrame)
        self.verticalLayout_imageMode.setSpacing(8)
        self.verticalLayout_imageMode.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_imageMode.setObjectName(u"verticalLayout_imageMode")
        self.verticalLayout_imageMode.setContentsMargins(8, 16, 8, 14)
        self.horizontalLayout_imageIconWrap = QHBoxLayout()
        self.horizontalLayout_imageIconWrap.setSpacing(0)
        self.horizontalLayout_imageIconWrap.setObjectName(u"horizontalLayout_imageIconWrap")
        self.horizontalSpacer_imageIconLeft = QSpacerItem(10, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_imageIconWrap.addItem(self.horizontalSpacer_imageIconLeft)

        self.imageModeIconBg = QFrame(self.imageModeFrame)
        self.imageModeIconBg.setObjectName(u"imageModeIconBg")
        self.imageModeIconBg.setMinimumSize(QSize(44, 44))
        self.imageModeIconBg.setMaximumSize(QSize(44, 44))
        self.imageModeIconBg.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_imageIconBg = QVBoxLayout(self.imageModeIconBg)
        self.verticalLayout_imageIconBg.setSpacing(0)
        self.verticalLayout_imageIconBg.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_imageIconBg.setObjectName(u"verticalLayout_imageIconBg")
        self.verticalLayout_imageIconBg.setContentsMargins(8, 8, 8, 8)
        self.imageModeIconLabel = QLabel(self.imageModeIconBg)
        self.imageModeIconLabel.setObjectName(u"imageModeIconLabel")
        self.imageModeIconLabel.setMinimumSize(QSize(28, 28))
        self.imageModeIconLabel.setMaximumSize(QSize(28, 28))
        self.imageModeIconLabel.setPixmap(QPixmap(u"../../imgs/image.png"))
        self.imageModeIconLabel.setScaledContents(True)
        self.imageModeIconLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_imageIconBg.addWidget(self.imageModeIconLabel)


        self.horizontalLayout_imageIconWrap.addWidget(self.imageModeIconBg)

        self.horizontalSpacer_imageIconRight = QSpacerItem(10, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_imageIconWrap.addItem(self.horizontalSpacer_imageIconRight)


        self.verticalLayout_imageMode.addLayout(self.horizontalLayout_imageIconWrap)

        self.imageModeTitle = QLabel(self.imageModeFrame)
        self.imageModeTitle.setObjectName(u"imageModeTitle")
        self.imageModeTitle.setAlignment(Qt.AlignCenter)

        self.verticalLayout_imageMode.addWidget(self.imageModeTitle)

        self.imageModeSubTitle = QLabel(self.imageModeFrame)
        self.imageModeSubTitle.setObjectName(u"imageModeSubTitle")
        self.imageModeSubTitle.setAlignment(Qt.AlignCenter)

        self.verticalLayout_imageMode.addWidget(self.imageModeSubTitle)


        self.horizontalLayout_modeButtons.addWidget(self.imageModeFrame)

        self.videoModeFrame = QFrame(self.uploadFrame)
        self.videoModeFrame.setObjectName(u"videoModeFrame")
        self.videoModeFrame.setMinimumSize(QSize(92, 144))
        self.videoModeFrame.setMaximumSize(QSize(92, 144))
        self.videoModeFrame.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.videoModeFrame.setStyleSheet(u"#videoModeFrame {\n"
"    background-color: #F3F4F6;\n"
"    border: 1px solid #F3F4F6;\n"
"    border-radius: 8px;\n"
"}\n"
"#videoModeIconBg {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}\n"
"#videoModeTitle {\n"
"    color: #4B5563;\n"
"    font-size: 14px;\n"
"}\n"
"#videoModeSubTitle {\n"
"    color: #4B5563;\n"
"    font-size: 12px;\n"
"}")
        self.videoModeFrame.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_videoMode = QVBoxLayout(self.videoModeFrame)
        self.verticalLayout_videoMode.setSpacing(8)
        self.verticalLayout_videoMode.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_videoMode.setObjectName(u"verticalLayout_videoMode")
        self.verticalLayout_videoMode.setContentsMargins(8, 16, 8, 14)
        self.horizontalLayout_videoIconWrap = QHBoxLayout()
        self.horizontalLayout_videoIconWrap.setSpacing(0)
        self.horizontalLayout_videoIconWrap.setObjectName(u"horizontalLayout_videoIconWrap")
        self.horizontalSpacer_videoIconLeft = QSpacerItem(10, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_videoIconWrap.addItem(self.horizontalSpacer_videoIconLeft)

        self.videoModeIconBg = QFrame(self.videoModeFrame)
        self.videoModeIconBg.setObjectName(u"videoModeIconBg")
        self.videoModeIconBg.setMinimumSize(QSize(44, 44))
        self.videoModeIconBg.setMaximumSize(QSize(44, 44))
        self.videoModeIconBg.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_videoIconBg = QVBoxLayout(self.videoModeIconBg)
        self.verticalLayout_videoIconBg.setSpacing(0)
        self.verticalLayout_videoIconBg.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_videoIconBg.setObjectName(u"verticalLayout_videoIconBg")
        self.verticalLayout_videoIconBg.setContentsMargins(8, 8, 8, 8)
        self.videoModeIconLabel = QLabel(self.videoModeIconBg)
        self.videoModeIconLabel.setObjectName(u"videoModeIconLabel")
        self.videoModeIconLabel.setMinimumSize(QSize(28, 28))
        self.videoModeIconLabel.setMaximumSize(QSize(28, 28))
        self.videoModeIconLabel.setPixmap(QPixmap(u"../../imgs/video.png"))
        self.videoModeIconLabel.setScaledContents(True)
        self.videoModeIconLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_videoIconBg.addWidget(self.videoModeIconLabel)


        self.horizontalLayout_videoIconWrap.addWidget(self.videoModeIconBg)

        self.horizontalSpacer_videoIconRight = QSpacerItem(10, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_videoIconWrap.addItem(self.horizontalSpacer_videoIconRight)


        self.verticalLayout_videoMode.addLayout(self.horizontalLayout_videoIconWrap)

        self.videoModeTitle = QLabel(self.videoModeFrame)
        self.videoModeTitle.setObjectName(u"videoModeTitle")
        self.videoModeTitle.setAlignment(Qt.AlignCenter)

        self.verticalLayout_videoMode.addWidget(self.videoModeTitle)

        self.videoModeSubTitle = QLabel(self.videoModeFrame)
        self.videoModeSubTitle.setObjectName(u"videoModeSubTitle")
        self.videoModeSubTitle.setAlignment(Qt.AlignCenter)

        self.verticalLayout_videoMode.addWidget(self.videoModeSubTitle)


        self.horizontalLayout_modeButtons.addWidget(self.videoModeFrame)

        self.horizontalSpacer_modeRight = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_modeButtons.addItem(self.horizontalSpacer_modeRight)


        self.verticalLayout_upload.addLayout(self.horizontalLayout_modeButtons)

        self.verticalSpacer_afterMode = QSpacerItem(20, 26, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_upload.addItem(self.verticalSpacer_afterMode)

        self.labelUploadTitle = QLabel(self.uploadFrame)
        self.labelUploadTitle.setObjectName(u"labelUploadTitle")
        self.labelUploadTitle.setStyleSheet(u"#labelUploadTitle {\n"
"    color: #000000;\n"
"    font-size: 20px;\n"
"    font-weight: 700;\n"
"}")
        self.labelUploadTitle.setAlignment(Qt.AlignCenter)

        self.verticalLayout_upload.addWidget(self.labelUploadTitle)

        self.verticalSpacer_afterTitle = QSpacerItem(20, 12, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_upload.addItem(self.verticalSpacer_afterTitle)

        self.labelUploadSubtitle = QLabel(self.uploadFrame)
        self.labelUploadSubtitle.setObjectName(u"labelUploadSubtitle")
        self.labelUploadSubtitle.setStyleSheet(u"#labelUploadSubtitle {\n"
"    color: #4B5563;\n"
"    font-size: 14px;\n"
"}")
        self.labelUploadSubtitle.setAlignment(Qt.AlignCenter)

        self.verticalLayout_upload.addWidget(self.labelUploadSubtitle)

        self.verticalSpacer_afterSubtitle = QSpacerItem(20, 22, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_upload.addItem(self.verticalSpacer_afterSubtitle)

        self.horizontalLayout_button = QHBoxLayout()
        self.horizontalLayout_button.setSpacing(0)
        self.horizontalLayout_button.setObjectName(u"horizontalLayout_button")
        self.horizontalSpacer_button_left = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_button.addItem(self.horizontalSpacer_button_left)

        self.btnSelectFile = QPushButton(self.uploadFrame)
        self.btnSelectFile.setObjectName(u"btnSelectFile")
        self.btnSelectFile.setMinimumSize(QSize(152, 40))
        self.btnSelectFile.setMaximumSize(QSize(152, 40))
        self.btnSelectFile.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnSelectFile.setStyleSheet(u"#btnSelectFile {\n"
"    background-color: #7C3BED;\n"
"    color: #FFFFFF;\n"
"    border: none;\n"
"    border-radius: 6px;\n"
"    padding: 0 22px;\n"
"    font-size: 14px;\n"
"    font-weight: 500;\n"
"}\n"
"#btnSelectFile:hover {\n"
"    background-color: #6D28D9;\n"
"}")

        self.horizontalLayout_button.addWidget(self.btnSelectFile)

        self.horizontalSpacer_button_right = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_button.addItem(self.horizontalSpacer_button_right)


        self.verticalLayout_upload.addLayout(self.horizontalLayout_button)

        self.verticalSpacer_afterButton = QSpacerItem(20, 18, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_upload.addItem(self.verticalSpacer_afterButton)

        self.labelFormats = QLabel(self.uploadFrame)
        self.labelFormats.setObjectName(u"labelFormats")
        self.labelFormats.setStyleSheet(u"#labelFormats {\n"
"    color: #4B5563;\n"
"    font-size: 12px;\n"
"}")
        self.labelFormats.setAlignment(Qt.AlignCenter)

        self.verticalLayout_upload.addWidget(self.labelFormats)

        self.verticalSpacer_uploadBottom = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_upload.addItem(self.verticalSpacer_uploadBottom)


        self.horizontalLayout_uploadWrap.addWidget(self.uploadFrame)

        self.horizontalSpacer_uploadRight = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_uploadWrap.addItem(self.horizontalSpacer_uploadRight)


        self.verticalLayout_contentOuter.addLayout(self.horizontalLayout_uploadWrap)

        self.verticalSpacer_contentBottom = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_contentOuter.addItem(self.verticalSpacer_contentBottom)


        self.verticalLayout_main.addWidget(self.contentContainer)

        self.footerFrame = QFrame(self.centralWidget)
        self.footerFrame.setObjectName(u"footerFrame")
        self.footerFrame.setMinimumSize(QSize(0, 72))
        self.footerFrame.setMaximumSize(QSize(16777215, 72))
        self.footerFrame.setStyleSheet(u"#footerFrame {\n"
"    background-color: #FFFFFF;\n"
"    border-top: 1px solid #E5E7EB;\n"
"}")
        self.footerFrame.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_footer = QVBoxLayout(self.footerFrame)
        self.verticalLayout_footer.setSpacing(0)
        self.verticalLayout_footer.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_footer.setObjectName(u"verticalLayout_footer")
        self.verticalLayout_footer.setContentsMargins(0, 0, 0, 0)
        self.labelFooter = QLabel(self.footerFrame)
        self.labelFooter.setObjectName(u"labelFooter")
        self.labelFooter.setOpenExternalLinks(True)
        self.labelFooter.setStyleSheet(u"#labelFooter {\n"
"    color: #6B7280;\n"
"    font-size: 14px;\n"
"}")
        self.labelFooter.setAlignment(Qt.AlignCenter)

        self.verticalLayout_footer.addWidget(self.labelFooter)


        self.verticalLayout_main.addWidget(self.footerFrame)

        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u62fc\u5b57\u5e55", None))
        self.logoLabel.setText(QCoreApplication.translate("MainWindow", u"\u62fc\u5b57\u5e55", None))
        self.btnSettings.setText(QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e", None))
        self.btnProjectInfo.setText(QCoreApplication.translate("MainWindow", u"\u9879\u76ee\u4ecb\u7ecd", None))
        self.imageModeTitle.setText(QCoreApplication.translate("MainWindow", u"\u4e0a\u4f20\u56fe\u7247", None))
        self.imageModeSubTitle.setText(QCoreApplication.translate("MainWindow", u"\u6700\u591a50\u5f20", None))
        self.videoModeTitle.setText(QCoreApplication.translate("MainWindow", u"\u4e0a\u4f20\u89c6\u9891", None))
        self.videoModeSubTitle.setText(QCoreApplication.translate("MainWindow", u"\u4ec5\u96501\u4e2a", None))
        self.labelUploadTitle.setText(QCoreApplication.translate("MainWindow", u"\u4e0a\u4f20\u56fe\u7247\u6587\u4ef6", None))
        self.labelUploadSubtitle.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u591a\u5f20\u56fe\u7247\uff0c\u7cfb\u7edf\u5c06\u6309\u987a\u5e8f\u62fc\u63a5\u6210\u5b57\u5e55\u957f\u56fe", None))
        self.btnSelectFile.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u56fe\u7247", None))
        self.labelFormats.setText(QCoreApplication.translate("MainWindow", u"\u652f\u6301\u683c\u5f0f\uff1aJPG\u3001PNG\u3001GIF\u3001WEBP", None))
        self.labelFooter.setText(QCoreApplication.translate("MainWindow", u"<a href=\"https://www.yuanheyuekeji.com/\" style=\"text-decoration:none; color:#6B7280;\">\u00a9 2026 \u62fc\u5b57\u5e55 - \u5feb\u901f\u751f\u6210\u8fde\u7eed\u5b57\u5e55\u957f\u56fe</a>", None))
    # retranslateUi

