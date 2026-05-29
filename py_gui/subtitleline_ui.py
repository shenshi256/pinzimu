# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'subtitleline.ui'
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
    QMainWindow, QPushButton, QSizePolicy, QSlider,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1000, 650)
        MainWindow.setMinimumSize(QSize(800, 600))
        MainWindow.setStyleSheet(u"QMainWindow {\n"
"    background-color: #FFFFFF;\n"
"    font-family: \"Microsoft YaHei\", \"Segoe UI\", sans-serif;\n"
"}\n"
"QLabel {\n"
"    color: #111827;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
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
        self.horizontalLayout_header.setSpacing(8)
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

        self.btnRestart = QPushButton(self.headerFrame)
        self.btnRestart.setObjectName(u"btnRestart")
        self.btnRestart.setMinimumSize(QSize(96, 36))
        self.btnRestart.setMaximumSize(QSize(120, 36))
        self.btnRestart.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnRestart.setStyleSheet(u"#btnRestart {\n"
"    background-color: #FFFFFF;\n"
"    color: #374151;\n"
"    border: 1px solid #E5E7EB;\n"
"    border-radius: 6px;\n"
"    padding: 0 14px;\n"
"    font-size: 14px;\n"
"    font-weight: 500;\n"
"}\n"
"#btnRestart:hover {\n"
"    background-color: #F9FAFB;\n"
"}")

        self.horizontalLayout_header.addWidget(self.btnRestart)


        self.verticalLayout_main.addWidget(self.headerFrame)

        self.contentContainer = QWidget(self.centralwidget)
        self.contentContainer.setObjectName(u"contentContainer")
        self.contentContainer.setStyleSheet(u"#contentContainer {\n"
"    background-color: #FFFFFF;\n"
"}")
        self.verticalLayout_contentOuter = QVBoxLayout(self.contentContainer)
        self.verticalLayout_contentOuter.setSpacing(24)
        self.verticalLayout_contentOuter.setObjectName(u"verticalLayout_contentOuter")
        self.verticalLayout_contentOuter.setContentsMargins(36, 24, 36, 24)
        self.horizontalLayout_titleRow = QHBoxLayout()
        self.horizontalLayout_titleRow.setSpacing(12)
        self.horizontalLayout_titleRow.setObjectName(u"horizontalLayout_titleRow")
        self.labelSubtitleTitle = QLabel(self.contentContainer)
        self.labelSubtitleTitle.setObjectName(u"labelSubtitleTitle")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelSubtitleTitle.sizePolicy().hasHeightForWidth())
        self.labelSubtitleTitle.setSizePolicy(sizePolicy)
        self.labelSubtitleTitle.setStyleSheet(u"#labelSubtitleTitle {\n"
"    color: #000000;\n"
"    font-size: 24px;\n"
"    font-weight: 700;\n"
"}")

        self.horizontalLayout_titleRow.addWidget(self.labelSubtitleTitle)

        self.horizontalSpacer_titleRow = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_titleRow.addItem(self.horizontalSpacer_titleRow)

        self.btnResetDefault = QPushButton(self.contentContainer)
        self.btnResetDefault.setObjectName(u"btnResetDefault")
        self.btnResetDefault.setMinimumSize(QSize(110, 36))
        self.btnResetDefault.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnResetDefault.setStyleSheet(u"#btnResetDefault {\n"
"    background-color: #FFFFFF;\n"
"    color: #374151;\n"
"    border: 1px solid #E5E7EB;\n"
"    border-radius: 6px;\n"
"    padding: 0 16px;\n"
"    font-size: 14px;\n"
"    font-weight: 500;\n"
"}\n"
"#btnResetDefault:hover {\n"
"    background-color: #F9FAFB;\n"
"}")

        self.horizontalLayout_titleRow.addWidget(self.btnResetDefault)


        self.verticalLayout_contentOuter.addLayout(self.horizontalLayout_titleRow)

        self.previewCard = QFrame(self.contentContainer)
        self.previewCard.setObjectName(u"previewCard")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(1)
        sizePolicy1.setVerticalStretch(1)
        sizePolicy1.setHeightForWidth(self.previewCard.sizePolicy().hasHeightForWidth())
        self.previewCard.setSizePolicy(sizePolicy1)
        self.previewCard.setMinimumSize(QSize(0, 0))
        self.previewCard.setStyleSheet(u"#previewCard {\n"
"    background-color: #F3F4F6;\n"
"    border: 1px solid #E5E7EB;\n"
"    border-radius: 10px;\n"
"}")
        self.previewCard.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_previewCard = QVBoxLayout(self.previewCard)
        self.verticalLayout_previewCard.setSpacing(0)
        self.verticalLayout_previewCard.setObjectName(u"verticalLayout_previewCard")
        self.verticalLayout_previewCard.setContentsMargins(0, 0, 0, 0)
        self.previewArea = QFrame(self.previewCard)
        self.previewArea.setObjectName(u"previewArea")
        sizePolicy1.setHeightForWidth(self.previewArea.sizePolicy().hasHeightForWidth())
        self.previewArea.setSizePolicy(sizePolicy1)
        self.previewArea.setMinimumSize(QSize(0, 0))
        self.previewArea.setStyleSheet(u"#previewArea {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}")
        self.previewArea.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_previewArea = QHBoxLayout(self.previewArea)
        self.horizontalLayout_previewArea.setSpacing(0)
        self.horizontalLayout_previewArea.setObjectName(u"horizontalLayout_previewArea")
        self.horizontalLayout_previewArea.setContentsMargins(0, 0, 0, 0)
        self.videoContainer = QFrame(self.previewArea)
        self.videoContainer.setObjectName(u"videoContainer")
        sizePolicy1.setHeightForWidth(self.videoContainer.sizePolicy().hasHeightForWidth())
        self.videoContainer.setSizePolicy(sizePolicy1)
        self.videoContainer.setStyleSheet(u"#videoContainer {\n"
"    background-color: #000000;\n"
"    border: none;\n"
"}")
        self.videoContainer.setFrameShape(QFrame.NoFrame)

        self.horizontalLayout_previewArea.addWidget(self.videoContainer)

        self.overlayPanel = QFrame(self.previewArea)
        self.overlayPanel.setObjectName(u"overlayPanel")
        sizePolicy1.setHeightForWidth(self.overlayPanel.sizePolicy().hasHeightForWidth())
        self.overlayPanel.setSizePolicy(sizePolicy1)
        self.overlayPanel.setStyleSheet(u"#overlayPanel {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}")
        self.overlayPanel.setFrameShape(QFrame.NoFrame)

        self.horizontalLayout_previewArea.addWidget(self.overlayPanel)


        self.verticalLayout_previewCard.addWidget(self.previewArea)

        self.videoProgressFrame = QFrame(self.previewCard)
        self.videoProgressFrame.setObjectName(u"videoProgressFrame")
        self.videoProgressFrame.setMinimumSize(QSize(0, 56))
        self.videoProgressFrame.setMaximumSize(QSize(16777215, 56))
        self.videoProgressFrame.setStyleSheet(u"#videoProgressFrame {\n"
"    background-color: rgba(17, 24, 39, 180);\n"
"    border: none;\n"
"    border-radius: 0 0 10px 10px;\n"
"}")
        self.videoProgressFrame.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_videoControls = QHBoxLayout(self.videoProgressFrame)
        self.horizontalLayout_videoControls.setSpacing(12)
        self.horizontalLayout_videoControls.setObjectName(u"horizontalLayout_videoControls")
        self.horizontalLayout_videoControls.setContentsMargins(12, 0, 12, 0)
        self.btnPlayPause = QPushButton(self.videoProgressFrame)
        self.btnPlayPause.setObjectName(u"btnPlayPause")
        self.btnPlayPause.setMinimumSize(QSize(36, 36))
        self.btnPlayPause.setMaximumSize(QSize(36, 36))
        self.btnPlayPause.setStyleSheet(u"#btnPlayPause {\n"
"    background-color: #7C3BED;\n"
"    border: none;\n"
"    border-radius: 18px;\n"
"}\n"
"#btnPlayPause:hover {\n"
"    background-color: #6D28D9;\n"
"}")
        self.btnPlayPause.setIconSize(QSize(18, 18))

        self.horizontalLayout_videoControls.addWidget(self.btnPlayPause)

        self.sliderVideoProgress = QSlider(self.videoProgressFrame)
        self.sliderVideoProgress.setObjectName(u"sliderVideoProgress")
        self.sliderVideoProgress.setMinimumSize(QSize(0, 20))
        self.sliderVideoProgress.setStyleSheet(u"#sliderVideoProgress::groove:horizontal {\n"
"    border: none;\n"
"    height: 4px;\n"
"    background: rgba(255, 255, 255, 60);\n"
"    border-radius: 2px;\n"
"}\n"
"#sliderVideoProgress::handle:horizontal {\n"
"    background: #FFFFFF;\n"
"    width: 14px;\n"
"    height: 14px;\n"
"    border-radius: 7px;\n"
"    margin: -5px 0;\n"
"}\n"
"#sliderVideoProgress::sub-page:horizontal {\n"
"    background: #7C3BED;\n"
"    border-radius: 2px;\n"
"}")
        self.sliderVideoProgress.setOrientation(Qt.Horizontal)

        self.horizontalLayout_videoControls.addWidget(self.sliderVideoProgress)

        self.labelVideoTime = QLabel(self.videoProgressFrame)
        self.labelVideoTime.setObjectName(u"labelVideoTime")
        self.labelVideoTime.setMinimumSize(QSize(80, 0))
        self.labelVideoTime.setStyleSheet(u"#labelVideoTime {\n"
"    color: #FFFFFF;\n"
"    font-size: 13px;\n"
"}")
        self.labelVideoTime.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_videoControls.addWidget(self.labelVideoTime)


        self.verticalLayout_previewCard.addWidget(self.videoProgressFrame)


        self.verticalLayout_contentOuter.addWidget(self.previewCard)

        self.infoFrame = QFrame(self.contentContainer)
        self.infoFrame.setObjectName(u"infoFrame")
        self.infoFrame.setStyleSheet(u"#infoFrame {\n"
"    background-color: #F9FAFB;\n"
"    border: 1px solid #E5E7EB;\n"
"    border-radius: 8px;\n"
"}")
        self.infoFrame.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_info = QVBoxLayout(self.infoFrame)
        self.verticalLayout_info.setSpacing(4)
        self.verticalLayout_info.setObjectName(u"verticalLayout_info")
        self.verticalLayout_info.setContentsMargins(14, 12, 14, 12)
        self.labelTip = QLabel(self.infoFrame)
        self.labelTip.setObjectName(u"labelTip")
        self.labelTip.setStyleSheet(u"#labelTip {\n"
"    color: #6B7280;\n"
"    font-size: 13px;\n"
"}")

        self.verticalLayout_info.addWidget(self.labelTip)

        self.labelAreaHeight = QLabel(self.infoFrame)
        self.labelAreaHeight.setObjectName(u"labelAreaHeight")
        self.labelAreaHeight.setStyleSheet(u"#labelAreaHeight {\n"
"    color: #9CA3AF;\n"
"    font-size: 12px;\n"
"}")

        self.verticalLayout_info.addWidget(self.labelAreaHeight)


        self.verticalLayout_contentOuter.addWidget(self.infoFrame)

        self.horizontalLayout_bottomButtons = QHBoxLayout()
        self.horizontalLayout_bottomButtons.setSpacing(16)
        self.horizontalLayout_bottomButtons.setObjectName(u"horizontalLayout_bottomButtons")
        self.btnBack = QPushButton(self.contentContainer)
        self.btnBack.setObjectName(u"btnBack")
        self.btnBack.setMinimumSize(QSize(110, 42))
        self.btnBack.setMaximumSize(QSize(140, 42))
        self.btnBack.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnBack.setStyleSheet(u"#btnBack {\n"
"    background-color: #FFFFFF;\n"
"    color: #374151;\n"
"    border: 1px solid #E5E7EB;\n"
"    border-radius: 6px;\n"
"    padding: 0 16px;\n"
"    font-size: 14px;\n"
"    font-weight: 500;\n"
"}\n"
"#btnBack:hover {\n"
"    background-color: #F9FAFB;\n"
"}")

        self.horizontalLayout_bottomButtons.addWidget(self.btnBack)

        self.horizontalSpacer_bottomButtons = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_bottomButtons.addItem(self.horizontalSpacer_bottomButtons)

        self.btnContinue = QPushButton(self.contentContainer)
        self.btnContinue.setObjectName(u"btnContinue")
        self.btnContinue.setMinimumSize(QSize(200, 42))
        self.btnContinue.setMaximumSize(QSize(300, 42))
        self.btnContinue.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnContinue.setStyleSheet(u"#btnContinue {\n"
"    background-color: #7C3BED;\n"
"    color: #FFFFFF;\n"
"    border: none;\n"
"    border-radius: 6px;\n"
"    padding: 0 22px;\n"
"    font-size: 14px;\n"
"    font-weight: 500;\n"
"}\n"
"#btnContinue:hover {\n"
"    background-color: #6D28D9;\n"
"}")

        self.horizontalLayout_bottomButtons.addWidget(self.btnContinue)


        self.verticalLayout_contentOuter.addLayout(self.horizontalLayout_bottomButtons)


        self.verticalLayout_main.addWidget(self.contentContainer)

        self.footerFrame = QFrame(self.centralwidget)
        self.footerFrame.setObjectName(u"footerFrame")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.footerFrame.sizePolicy().hasHeightForWidth())
        self.footerFrame.setSizePolicy(sizePolicy2)
        self.footerFrame.setMinimumSize(QSize(0, 0))
        self.footerFrame.setMaximumSize(QSize(16777215, 0))
        self.footerFrame.setStyleSheet(u"#footerFrame {\n"
"    background-color: #FFFFFF;\n"
"    border-top: 1px solid #E5E7EB;\n"
"}")
        self.footerFrame.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_footer = QVBoxLayout(self.footerFrame)
        self.verticalLayout_footer.setSpacing(0)
        self.verticalLayout_footer.setObjectName(u"verticalLayout_footer")
        self.verticalLayout_footer.setContentsMargins(0, 0, 0, 0)
        self.labelFooter = QLabel(self.footerFrame)
        self.labelFooter.setObjectName(u"labelFooter")
        self.labelFooter.setStyleSheet(u"#labelFooter {\n"
"    color: #6B7280;\n"
"    font-size: 14px;\n"
"}")
        self.labelFooter.setAlignment(Qt.AlignCenter)

        self.verticalLayout_footer.addWidget(self.labelFooter)


        self.verticalLayout_main.addWidget(self.footerFrame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u62fc\u5b57\u5e55 - \u8fb9\u7ebf\u8bbe\u7f6e", None))
        self.logoLabel.setText(QCoreApplication.translate("MainWindow", u"\u62fc\u5b57\u5e55", None))
        self.btnRestart.setText(QCoreApplication.translate("MainWindow", u"\u91cd\u65b0\u5f00\u59cb", None))
        self.labelSubtitleTitle.setText(QCoreApplication.translate("MainWindow", u"\u62d6\u52a8\u4e0a\u4e0b\u8fb9\u7f18\u7ebf\u8c03\u6574\u5b57\u5e55\u7ebf\u4f4d\u7f6e", None))
        self.btnResetDefault.setText(QCoreApplication.translate("MainWindow", u"\u91cd\u7f6e\u9ed8\u8ba4", None))
        self.btnPlayPause.setText("")
        self.labelVideoTime.setText(QCoreApplication.translate("MainWindow", u"0:00 / 0:00", None))
        self.labelTip.setText(QCoreApplication.translate("MainWindow", u"\u53ef\u4ee5\u64ad\u653e\u89c6\u9891\u9884\u89c8\uff0c\u76f4\u63a5\u62d6\u52a8\u5b57\u5e55\u7ebf\u4e0a\u7684\u624b\u67c4\u8c03\u6574\u4f4d\u7f6e", None))
        self.labelAreaHeight.setText(QCoreApplication.translate("MainWindow", u"\u5b57\u5e55\u533a\u57df\u9ad8\u5ea6\uff1a20% \u00b7 \u4f4d\u7f6e\u5df2\u81ea\u52a8\u4fdd\u5b58", None))
        self.btnBack.setText(QCoreApplication.translate("MainWindow", u"<- \u8fd4\u56de", None))
        self.btnContinue.setText(QCoreApplication.translate("MainWindow", u"\u7ee7\u7eed\u751f\u6210\u957f\u56fe", None))
        self.labelFooter.setText(QCoreApplication.translate("MainWindow", u"\u00a9 2026 \u62fc\u5b57\u5e55 - \u5feb\u901f\u751f\u6210\u8fde\u7eed\u5b57\u5e55\u957f\u56fe", None))
    # retranslateUi

