# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'imagestitcher.ui'
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
    QScrollArea, QSizePolicy, QSpacerItem, QStatusBar,
    QVBoxLayout, QWidget)
class Ui_ImageStitcher(object):
    def setupUi(self, ImageStitcher):
        if not ImageStitcher.objectName():
            ImageStitcher.setObjectName(u"ImageStitcher")
        ImageStitcher.resize(1000, 650)
        ImageStitcher.setMinimumSize(QSize(800, 600))
        ImageStitcher.setStyleSheet(u"QMainWindow {\n"
"    background-color: #FFFFFF;\n"
"    font-family: \"Microsoft YaHei\", \"Segoe UI\", sans-serif;\n"
"}\n"
"QLabel {\n"
"    color: #111827;\n"
"}")
        self.centralwidget = QWidget(ImageStitcher)
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
        self.verticalLayout_contentOuter.setSpacing(18)
        self.verticalLayout_contentOuter.setObjectName(u"verticalLayout_contentOuter")
        self.verticalLayout_contentOuter.setContentsMargins(36, 24, 36, 24)
        self.labelStitchTitle = QLabel(self.contentContainer)
        self.labelStitchTitle.setObjectName(u"labelStitchTitle")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelStitchTitle.sizePolicy().hasHeightForWidth())
        self.labelStitchTitle.setSizePolicy(sizePolicy)
        self.labelStitchTitle.setStyleSheet(u"#labelStitchTitle {\n"
"    color: #000000;\n"
"    font-size: 24px;\n"
"    font-weight: 700;\n"
"}")

        self.verticalLayout_contentOuter.addWidget(self.labelStitchTitle)

        self.horizontalLayout_infoRow = QHBoxLayout()
        self.horizontalLayout_infoRow.setSpacing(12)
        self.horizontalLayout_infoRow.setObjectName(u"horizontalLayout_infoRow")
        self.subtitleLineInfoFrame = QFrame(self.contentContainer)
        self.subtitleLineInfoFrame.setObjectName(u"subtitleLineInfoFrame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.subtitleLineInfoFrame.sizePolicy().hasHeightForWidth())
        self.subtitleLineInfoFrame.setSizePolicy(sizePolicy1)
        self.subtitleLineInfoFrame.setStyleSheet(u"#subtitleLineInfoFrame {\n"
"    background-color: #F3F4F6;\n"
"    border: 1px solid #E5E7EB;\n"
"    border-radius: 8px;\n"
"}")
        self.subtitleLineInfoFrame.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_subtitleLineInfo = QHBoxLayout(self.subtitleLineInfoFrame)
        self.horizontalLayout_subtitleLineInfo.setSpacing(4)
        self.horizontalLayout_subtitleLineInfo.setObjectName(u"horizontalLayout_subtitleLineInfo")
        self.horizontalLayout_subtitleLineInfo.setContentsMargins(14, 10, 14, 10)
        self.labelSubtitleLineHint = QLabel(self.subtitleLineInfoFrame)
        self.labelSubtitleLineHint.setObjectName(u"labelSubtitleLineHint")
        self.labelSubtitleLineHint.setStyleSheet(u"#labelSubtitleLineHint {\n"
"    color: #6B7280;\n"
"    font-size: 13px;\n"
"}")

        self.horizontalLayout_subtitleLineInfo.addWidget(self.labelSubtitleLineHint)

        self.labelSubtitleLineValue = QLabel(self.subtitleLineInfoFrame)
        self.labelSubtitleLineValue.setObjectName(u"labelSubtitleLineValue")
        self.labelSubtitleLineValue.setStyleSheet(u"#labelSubtitleLineValue {\n"
"    color: #111827;\n"
"    font-size: 13px;\n"
"    font-weight: 500;\n"
"}")

        self.horizontalLayout_subtitleLineInfo.addWidget(self.labelSubtitleLineValue)

        self.horizontalSpacer_subtitleLineInfo = QSpacerItem(10, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_subtitleLineInfo.addItem(self.horizontalSpacer_subtitleLineInfo)


        self.horizontalLayout_infoRow.addWidget(self.subtitleLineInfoFrame)

        self.imageListToolbarFrame = QFrame(self.contentContainer)
        self.imageListToolbarFrame.setObjectName(u"imageListToolbarFrame")
        self.imageListToolbarFrame.setStyleSheet(u"#imageListToolbarFrame {\n"
"    background-color: transparent;\n"
"}")
        self.imageListToolbarFrame.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_imageListToolbar = QHBoxLayout(self.imageListToolbarFrame)
        self.horizontalLayout_imageListToolbar.setSpacing(8)
        self.horizontalLayout_imageListToolbar.setObjectName(u"horizontalLayout_imageListToolbar")
        self.horizontalLayout_imageListToolbar.setContentsMargins(0, 0, 0, 0)
        self.labelImageCount = QLabel(self.imageListToolbarFrame)
        self.labelImageCount.setObjectName(u"labelImageCount")
        self.labelImageCount.setStyleSheet(u"#labelImageCount {\n"
"    color: #6B7280;\n"
"    font-size: 14px;\n"
"    font-weight: 500;\n"
"}")

        self.horizontalLayout_imageListToolbar.addWidget(self.labelImageCount)

        self.horizontalSpacer_toolbar = QSpacerItem(10, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_imageListToolbar.addItem(self.horizontalSpacer_toolbar)

        self.btnSelectAll = QPushButton(self.imageListToolbarFrame)
        self.btnSelectAll.setObjectName(u"btnSelectAll")
        self.btnSelectAll.setMinimumSize(QSize(72, 32))
        self.btnSelectAll.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnSelectAll.setStyleSheet(u"#btnSelectAll {\n"
"    background-color: #FFFFFF;\n"
"    color: #374151;\n"
"    border: 1px solid #E5E7EB;\n"
"    border-radius: 6px;\n"
"    padding: 0 10px;\n"
"    font-size: 13px;\n"
"    font-weight: 500;\n"
"}\n"
"#btnSelectAll:hover {\n"
"    background-color: #F9FAFB;\n"
"}")

        self.horizontalLayout_imageListToolbar.addWidget(self.btnSelectAll)

        self.btnDeleteSelected = QPushButton(self.imageListToolbarFrame)
        self.btnDeleteSelected.setObjectName(u"btnDeleteSelected")
        self.btnDeleteSelected.setMinimumSize(QSize(72, 32))
        self.btnDeleteSelected.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnDeleteSelected.setStyleSheet(u"#btnDeleteSelected {\n"
"    background-color: #FFFFFF;\n"
"    color: #EF4444;\n"
"    border: 1px solid #FECACA;\n"
"    border-radius: 6px;\n"
"    padding: 0 10px;\n"
"    font-size: 13px;\n"
"    font-weight: 500;\n"
"}\n"
"#btnDeleteSelected:hover {\n"
"    background-color: #FEF2F2;\n"
"}")

        self.horizontalLayout_imageListToolbar.addWidget(self.btnDeleteSelected)

        self.btnAutoDeduplicate = QPushButton(self.imageListToolbarFrame)
        self.btnAutoDeduplicate.setObjectName(u"btnAutoDeduplicate")
        self.btnAutoDeduplicate.setMinimumSize(QSize(72, 32))
        self.btnAutoDeduplicate.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnAutoDeduplicate.setStyleSheet(u"#btnAutoDeduplicate {\n"
"    background-color: #FFFFFF;\n"
"    color: #374151;\n"
"    border: 1px solid #E5E7EB;\n"
"    border-radius: 6px;\n"
"    padding: 0 10px;\n"
"    font-size: 13px;\n"
"    font-weight: 500;\n"
"}\n"
"#btnAutoDeduplicate:hover {\n"
"    background-color: #F9FAFB;\n"
"}")

        self.horizontalLayout_imageListToolbar.addWidget(self.btnAutoDeduplicate)

        self.btnUndoDeduplicate = QPushButton(self.imageListToolbarFrame)
        self.btnUndoDeduplicate.setObjectName(u"btnUndoDeduplicate")
        self.btnUndoDeduplicate.setMinimumSize(QSize(56, 32))
        self.btnUndoDeduplicate.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnUndoDeduplicate.setStyleSheet(u"#btnUndoDeduplicate {\n"
"    background-color: #FFFFFF;\n"
"    color: #374151;\n"
"    border: 1px solid #E5E7EB;\n"
"    border-radius: 6px;\n"
"    padding: 0 10px;\n"
"    font-size: 13px;\n"
"    font-weight: 500;\n"
"}\n"
"#btnUndoDeduplicate:hover {\n"
"    background-color: #F9FAFB;\n"
"}\n"
"#btnUndoDeduplicate:disabled {\n"
"    color: #D1D5DB;\n"
"}")

        self.horizontalLayout_imageListToolbar.addWidget(self.btnUndoDeduplicate)

        self.btnOutputImages = QPushButton(self.imageListToolbarFrame)
        self.btnOutputImages.setObjectName(u"btnOutputImages")
        self.btnOutputImages.setMinimumSize(QSize(64, 32))
        self.btnOutputImages.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnOutputImages.setStyleSheet(u"#btnOutputImages {\n"
"    background-color: #FFFFFF;\n"
"    color: #374151;\n"
"    border: 1px solid #E5E7EB;\n"
"    border-radius: 6px;\n"
"    padding: 0 10px;\n"
"    font-size: 13px;\n"
"    font-weight: 500;\n"
"}\n"
"#btnOutputImages:hover {\n"
"    background-color: #F9FAFB;\n"
"}\n"
"#btnOutputImages:disabled {\n"
"    color: #D1D5DB;\n"
"}")

        self.horizontalLayout_imageListToolbar.addWidget(self.btnOutputImages)


        self.horizontalLayout_infoRow.addWidget(self.imageListToolbarFrame)


        self.verticalLayout_contentOuter.addLayout(self.horizontalLayout_infoRow)

        self.imageListScrollArea = QScrollArea(self.contentContainer)
        self.imageListScrollArea.setObjectName(u"imageListScrollArea")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(1)
        sizePolicy2.setHeightForWidth(self.imageListScrollArea.sizePolicy().hasHeightForWidth())
        self.imageListScrollArea.setSizePolicy(sizePolicy2)
        self.imageListScrollArea.setMinimumSize(QSize(0, 200))
        self.imageListScrollArea.setStyleSheet(u"QScrollArea {\n"
"    background-color: #FFFFFF;\n"
"    border: 1px solid #E5E7EB;\n"
"    border-radius: 8px;\n"
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
        self.imageListScrollArea.setFrameShape(QFrame.NoFrame)
        self.imageListScrollArea.setWidgetResizable(True)
        self.imageListContainer = QWidget()
        self.imageListContainer.setObjectName(u"imageListContainer")
        self.imageListContainer.setGeometry(QRect(0, 0, 800, 400))
        self.imageListScrollArea.setWidget(self.imageListContainer)

        self.verticalLayout_contentOuter.addWidget(self.imageListScrollArea)

        self.progressBar = QProgressBar(self.contentContainer)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setMinimumSize(QSize(0, 8))
        self.progressBar.setMaximumSize(QSize(16777215, 8))
        self.progressBar.setStyleSheet(u"QProgressBar {\n"
"    background-color: #E5E7EB;\n"
"    border: none;\n"
"    border-radius: 4px;\n"
"}\n"
"QProgressBar::chunk {\n"
"    background-color: #7C3BED;\n"
"    border-radius: 4px;\n"
"}")
        self.progressBar.setValue(0)
        self.progressBar.setTextVisible(False)

        self.verticalLayout_contentOuter.addWidget(self.progressBar)

        self.horizontalLayout_actionButtons = QHBoxLayout()
        self.horizontalLayout_actionButtons.setSpacing(12)
        self.horizontalLayout_actionButtons.setObjectName(u"horizontalLayout_actionButtons")
        self.btnBackToVideo = QPushButton(self.contentContainer)
        self.btnBackToVideo.setObjectName(u"btnBackToVideo")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(1)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.btnBackToVideo.sizePolicy().hasHeightForWidth())
        self.btnBackToVideo.setSizePolicy(sizePolicy3)
        self.btnBackToVideo.setMinimumSize(QSize(0, 44))
        self.btnBackToVideo.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnBackToVideo.setStyleSheet(u"#btnBackToVideo {\n"
"    background-color: #FFFFFF;\n"
"    color: #374151;\n"
"    border: 1px solid #D1D5DB;\n"
"    border-radius: 8px;\n"
"    font-size: 16px;\n"
"    font-weight: 500;\n"
"}\n"
"#btnBackToVideo:hover {\n"
"    background-color: #F9FAFB;\n"
"}")

        self.horizontalLayout_actionButtons.addWidget(self.btnBackToVideo)

        self.btnGenerate = QPushButton(self.contentContainer)
        self.btnGenerate.setObjectName(u"btnGenerate")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(4)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.btnGenerate.sizePolicy().hasHeightForWidth())
        self.btnGenerate.setSizePolicy(sizePolicy4)
        self.btnGenerate.setMinimumSize(QSize(0, 44))
        self.btnGenerate.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnGenerate.setStyleSheet(u"#btnGenerate {\n"
"    background-color: #7C3BED;\n"
"    color: #FFFFFF;\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"    padding: 0 24px;\n"
"    font-size: 16px;\n"
"    font-weight: 600;\n"
"}\n"
"#btnGenerate:hover {\n"
"    background-color: #6D28D9;\n"
"}\n"
"#btnGenerate:disabled {\n"
"    background-color: #D1D5DB;\n"
"    color: #9CA3AF;\n"
"}")

        self.horizontalLayout_actionButtons.addWidget(self.btnGenerate)


        self.verticalLayout_contentOuter.addLayout(self.horizontalLayout_actionButtons)

        self.tipsFrame = QFrame(self.contentContainer)
        self.tipsFrame.setObjectName(u"tipsFrame")
        self.tipsFrame.setStyleSheet(u"#tipsFrame {\n"
"    background-color: #FFFBEB;\n"
"    border: 1px solid #FDE68A;\n"
"    border-radius: 8px;\n"
"}")
        self.tipsFrame.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_tips = QHBoxLayout(self.tipsFrame)
        self.horizontalLayout_tips.setSpacing(8)
        self.horizontalLayout_tips.setObjectName(u"horizontalLayout_tips")
        self.horizontalLayout_tips.setContentsMargins(14, 10, 14, 10)
        self.labelTips = QLabel(self.tipsFrame)
        self.labelTips.setObjectName(u"labelTips")
        self.labelTips.setStyleSheet(u"#labelTips {\n"
"    color: #92400E;\n"
"    font-size: 13px;\n"
"}")

        self.horizontalLayout_tips.addWidget(self.labelTips)


        self.verticalLayout_contentOuter.addWidget(self.tipsFrame)

        self.labelFooter = QLabel(self.contentContainer)
        self.labelFooter.setObjectName(u"labelFooter")
        self.labelFooter.setOpenExternalLinks(True)
        self.labelFooter.setMinimumSize(QSize(0, 48))
        self.labelFooter.setStyleSheet(u"#labelFooter {\n"
"    color: #9CA3AF;\n"
"    font-size: 13px;\n"
"    border-top: 1px solid #F3F4F6;\n"
"}")
        self.labelFooter.setAlignment(Qt.AlignCenter)

        self.verticalLayout_contentOuter.addWidget(self.labelFooter)


        self.verticalLayout_main.addWidget(self.contentContainer)

        ImageStitcher.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(ImageStitcher)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1100, 21))
        ImageStitcher.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(ImageStitcher)
        self.statusbar.setObjectName(u"statusbar")
        ImageStitcher.setStatusBar(self.statusbar)

        self.retranslateUi(ImageStitcher)

        QMetaObject.connectSlotsByName(ImageStitcher)
    # setupUi

    def retranslateUi(self, ImageStitcher):
        ImageStitcher.setWindowTitle(QCoreApplication.translate("ImageStitcher", u"\u62fc\u5b57\u5e55 - \u751f\u6210\u5b57\u5e55\u957f\u56fe", None))
        self.logoLabel.setText(QCoreApplication.translate("ImageStitcher", u"\u62fc\u5b57\u5e55", None))
        self.btnRestart.setText(QCoreApplication.translate("ImageStitcher", u"\u91cd\u65b0\u5f00\u59cb", None))
        self.labelStitchTitle.setText(QCoreApplication.translate("ImageStitcher", u"\u751f\u6210\u5b57\u5e55\u957f\u56fe", None))
        self.labelSubtitleLineHint.setText(QCoreApplication.translate("ImageStitcher", u"\u5b57\u5e55\u8303\u56f4:", None))
        self.labelSubtitleLineValue.setText(QCoreApplication.translate("ImageStitcher", u"\u4e0a\u8fb9\u7ebf 50%  -  \u4e0b\u8fb9\u7ebf 80%", None))
        self.labelImageCount.setText(QCoreApplication.translate("ImageStitcher", u"\u5171 0 \u5f20\u622a\u56fe", None))
        self.btnSelectAll.setText(QCoreApplication.translate("ImageStitcher", u"\u5168\u9009", None))
        self.btnDeleteSelected.setText(QCoreApplication.translate("ImageStitcher", u"\u5220\u9664\u9009\u4e2d", None))
        self.btnAutoDeduplicate.setText(QCoreApplication.translate("ImageStitcher", u"\u667a\u80fd\u53bb\u91cd", None))
        self.btnUndoDeduplicate.setText(QCoreApplication.translate("ImageStitcher", u"\u53bb\u9664\u7a7a\u5b57\u5e55", None))
        self.btnOutputImages.setText(QCoreApplication.translate("ImageStitcher", u"\u5bfc\u51fa", None))
        self.btnBackToVideo.setText(QCoreApplication.translate("ImageStitcher", u"\u8fd4\u56de", None))
        self.btnGenerate.setText(QCoreApplication.translate("ImageStitcher", u"\u751f\u6210\u5b57\u5e55\u957f\u56fe", None))
        self.labelTips.setText(QCoreApplication.translate("ImageStitcher", u"\u63d0\u793a\uff1a\u5148\u8bbe\u7f6e\u597d\u5b57\u5e55\u884c\u4f4d\u7f6e\uff0c\u518d\u622a\u56fe\u62fc\u63a5\u3002\u652f\u6301\u62d6\u62fd\u6392\u5e8f\u3001\u667a\u80fd\u53bb\u91cd\u548c\u9884\u89c8\u3002", None))
        self.labelFooter.setText(QCoreApplication.translate("ImageStitcher", u"<a href=\"https://www.yuanheyuekeji.com/\" style=\"text-decoration:none; color:#9CA3AF;\">\u00a9 2026 \u62fc\u5b57\u5e55 - \u5feb\u901f\u751f\u6210\u8fde\u7eed\u5b57\u5e55\u957f\u56fe</a>", None))
    # retranslateUi

