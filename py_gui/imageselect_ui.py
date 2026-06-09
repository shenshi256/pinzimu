# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'imageselect.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QSpacerItem, QStatusBar,
    QVBoxLayout, QWidget)

class Ui_ImageSelect(object):
    def setupUi(self, ImageSelect):
        if not ImageSelect.objectName():
            ImageSelect.setObjectName(u"ImageSelect")
        ImageSelect.resize(1000, 650)
        ImageSelect.setMinimumSize(QSize(800, 600))
        ImageSelect.setStyleSheet(u"QMainWindow {\n"
"    background-color: #FFFFFF;\n"
"    font-family: \"Microsoft YaHei\", \"Segoe UI\", sans-serif;\n"
"}\n"
"QLabel {\n"
"    color: #111827;\n"
"}")
        self.centralwidget = QWidget(ImageSelect)
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
        self.verticalLayout_contentOuter.setSpacing(16)
        self.verticalLayout_contentOuter.setObjectName(u"verticalLayout_contentOuter")
        self.verticalLayout_contentOuter.setContentsMargins(36, 20, 36, 20)
        self.horizontalLayout_titleRow = QHBoxLayout()
        self.horizontalLayout_titleRow.setSpacing(12)
        self.horizontalLayout_titleRow.setObjectName(u"horizontalLayout_titleRow")
        self.labelTitle = QLabel(self.contentContainer)
        self.labelTitle.setObjectName(u"labelTitle")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelTitle.sizePolicy().hasHeightForWidth())
        self.labelTitle.setSizePolicy(sizePolicy)
        self.labelTitle.setStyleSheet(u"#labelTitle {\n"
"    color: #000000;\n"
"    font-size: 24px;\n"
"    font-weight: 700;\n"
"}")

        self.horizontalLayout_titleRow.addWidget(self.labelTitle)

        self.horizontalSpacer_titleRow = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_titleRow.addItem(self.horizontalSpacer_titleRow)

        self.labelForceWidth = QLabel(self.contentContainer)
        self.labelForceWidth.setObjectName(u"labelForceWidth")
        self.labelForceWidth.setStyleSheet(u"#labelForceWidth {\n"
"    color: #6B7280;\n"
"    font-size: 13px;\n"
"}")

        self.horizontalLayout_titleRow.addWidget(self.labelForceWidth)

        self.comboForceWidth = QComboBox(self.contentContainer)
        self.comboForceWidth.addItem("")
        self.comboForceWidth.addItem("")
        self.comboForceWidth.addItem("")
        self.comboForceWidth.addItem("")
        self.comboForceWidth.setObjectName(u"comboForceWidth")
        self.comboForceWidth.setMinimumSize(QSize(80, 36))
        self.comboForceWidth.setStyleSheet(u"#comboForceWidth {\n"
"    background-color: #FFFFFF;\n"
"    color: #374151;\n"
"    border: 1px solid #D1D5DB;\n"
"    border-radius: 6px;\n"
"    padding: 0 8px;\n"
"    font-size: 13px;\n"
"    font-weight: 500;\n"
"}")

        self.horizontalLayout_titleRow.addWidget(self.comboForceWidth)

        self.btnSyncAll = QPushButton(self.contentContainer)
        self.btnSyncAll.setObjectName(u"btnSyncAll")
        self.btnSyncAll.setMinimumSize(QSize(100, 36))
        self.btnSyncAll.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnSyncAll.setStyleSheet(u"#btnSyncAll {\n"
"    background-color: #FFFFFF;\n"
"    color: #374151;\n"
"    border: 1px solid #E5E7EB;\n"
"    border-radius: 6px;\n"
"    padding: 0 16px;\n"
"    font-size: 14px;\n"
"    font-weight: 500;\n"
"}\n"
"#btnSyncAll:hover {\n"
"    background-color: #F9FAFB;\n"
"}")

        self.horizontalLayout_titleRow.addWidget(self.btnSyncAll)

        self.btnResetDefault = QPushButton(self.contentContainer)
        self.btnResetDefault.setObjectName(u"btnResetDefault")
        self.btnResetDefault.setMinimumSize(QSize(130, 36))
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

        self.btnResetAll = QPushButton(self.contentContainer)
        self.btnResetAll.setObjectName(u"btnResetAll")
        self.btnResetAll.setMinimumSize(QSize(130, 36))
        self.btnResetAll.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnResetAll.setStyleSheet(u"#btnResetAll {\n"
"    background-color: #FFFFFF;\n"
"    color: #374151;\n"
"    border: 1px solid #E5E7EB;\n"
"    border-radius: 6px;\n"
"    padding: 0 16px;\n"
"    font-size: 14px;\n"
"    font-weight: 500;\n"
"}\n"
"#btnResetAll:hover {\n"
"    background-color: #F9FAFB;\n"
"}")

        self.horizontalLayout_titleRow.addWidget(self.btnResetAll)


        self.verticalLayout_contentOuter.addLayout(self.horizontalLayout_titleRow)

        self.imageNavFrame = QFrame(self.contentContainer)
        self.imageNavFrame.setObjectName(u"imageNavFrame")
        self.imageNavFrame.setMinimumSize(QSize(0, 44))
        self.imageNavFrame.setMaximumSize(QSize(16777215, 44))
        self.imageNavFrame.setStyleSheet(u"#imageNavFrame {\n"
"    background-color: #F9FAFB;\n"
"    border: 1px solid #E5E7EB;\n"
"    border-radius: 8px;\n"
"}")
        self.imageNavFrame.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_imageNav = QHBoxLayout(self.imageNavFrame)
        self.horizontalLayout_imageNav.setSpacing(12)
        self.horizontalLayout_imageNav.setObjectName(u"horizontalLayout_imageNav")
        self.horizontalLayout_imageNav.setContentsMargins(12, 8, 12, 8)
        self.btnPrevImage = QPushButton(self.imageNavFrame)
        self.btnPrevImage.setObjectName(u"btnPrevImage")
        self.btnPrevImage.setMinimumSize(QSize(80, 28))
        self.btnPrevImage.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnPrevImage.setStyleSheet(u"#btnPrevImage {\n"
"    background-color: #FFFFFF;\n"
"    color: #374151;\n"
"    border: 1px solid #D1D5DB;\n"
"    border-radius: 4px;\n"
"    padding: 0 12px;\n"
"    font-size: 13px;\n"
"    font-weight: 500;\n"
"}\n"
"#btnPrevImage:hover {\n"
"    background-color: #F3F4F6;\n"
"}\n"
"#btnPrevImage:disabled {\n"
"    background-color: #F3F4F6;\n"
"    color: #9CA3AF;\n"
"    border-color: #E5E7EB;\n"
"}")

        self.horizontalLayout_imageNav.addWidget(self.btnPrevImage)

        self.horizontalSpacer_imageNav = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_imageNav.addItem(self.horizontalSpacer_imageNav)

        self.labelImageCounter = QLabel(self.imageNavFrame)
        self.labelImageCounter.setObjectName(u"labelImageCounter")
        self.labelImageCounter.setStyleSheet(u"#labelImageCounter {\n"
"    color: #374151;\n"
"    font-size: 14px;\n"
"    font-weight: 500;\n"
"}")
        self.labelImageCounter.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_imageNav.addWidget(self.labelImageCounter)

        self.horizontalSpacer_imageNav2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_imageNav.addItem(self.horizontalSpacer_imageNav2)

        self.btnNextImage = QPushButton(self.imageNavFrame)
        self.btnNextImage.setObjectName(u"btnNextImage")
        self.btnNextImage.setMinimumSize(QSize(80, 28))
        self.btnNextImage.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnNextImage.setStyleSheet(u"#btnNextImage {\n"
"    background-color: #FFFFFF;\n"
"    color: #374151;\n"
"    border: 1px solid #D1D5DB;\n"
"    border-radius: 4px;\n"
"    padding: 0 12px;\n"
"    font-size: 13px;\n"
"    font-weight: 500;\n"
"}\n"
"#btnNextImage:hover {\n"
"    background-color: #F3F4F6;\n"
"}\n"
"#btnNextImage:disabled {\n"
"    background-color: #F3F4F6;\n"
"    color: #9CA3AF;\n"
"    border-color: #E5E7EB;\n"
"}")

        self.horizontalLayout_imageNav.addWidget(self.btnNextImage)

        self.labelGoToPage = QLabel(self.imageNavFrame)
        self.labelGoToPage.setObjectName(u"labelGoToPage")
        self.labelGoToPage.setStyleSheet(u"#labelGoToPage {\n"
"    color: #6B7280;\n"
"    font-size: 14px;\n"
"}")

        self.horizontalLayout_imageNav.addWidget(self.labelGoToPage)

        self.editGoToPage = QLineEdit(self.imageNavFrame)
        self.editGoToPage.setObjectName(u"editGoToPage")
        self.editGoToPage.setMinimumSize(QSize(48, 28))
        self.editGoToPage.setMaximumSize(QSize(56, 28))
        self.editGoToPage.setAlignment(Qt.AlignCenter)
        self.editGoToPage.setStyleSheet(u"#editGoToPage {\n"
"    background-color: #FFFFFF;\n"
"    color: #374151;\n"
"    border: 1px solid #D1D5DB;\n"
"    border-radius: 4px;\n"
"    padding: 0 6px;\n"
"    font-size: 14px;\n"
"}")

        self.horizontalLayout_imageNav.addWidget(self.editGoToPage)

        self.labelGoToPageSuffix = QLabel(self.imageNavFrame)
        self.labelGoToPageSuffix.setObjectName(u"labelGoToPageSuffix")
        self.labelGoToPageSuffix.setStyleSheet(u"#labelGoToPageSuffix {\n"
"    color: #6B7280;\n"
"    font-size: 14px;\n"
"}")

        self.horizontalLayout_imageNav.addWidget(self.labelGoToPageSuffix)

        self.btnGoToPage = QPushButton(self.imageNavFrame)
        self.btnGoToPage.setObjectName(u"btnGoToPage")
        self.btnGoToPage.setMinimumSize(QSize(48, 28))
        self.btnGoToPage.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnGoToPage.setStyleSheet(u"#btnGoToPage {\n"
"    background-color: #FFFFFF;\n"
"    color: #374151;\n"
"    border: 1px solid #D1D5DB;\n"
"    border-radius: 4px;\n"
"    padding: 0 8px;\n"
"    font-size: 13px;\n"
"    font-weight: 500;\n"
"}\n"
"#btnGoToPage:hover {\n"
"    background-color: #F3F4F6;\n"
"}")

        self.horizontalLayout_imageNav.addWidget(self.btnGoToPage)


        self.verticalLayout_contentOuter.addWidget(self.imageNavFrame)

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

        self.verticalLayout_previewCard.addWidget(self.previewArea)

        self.infoFrame = QFrame(self.previewCard)
        self.infoFrame.setObjectName(u"infoFrame")
        self.infoFrame.setMinimumSize(QSize(0, 44))
        self.infoFrame.setMaximumSize(QSize(16777215, 52))
        self.infoFrame.setStyleSheet(u"#infoFrame {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}")
        self.infoFrame.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_infoFrame = QVBoxLayout(self.infoFrame)
        self.verticalLayout_infoFrame.setSpacing(2)
        self.verticalLayout_infoFrame.setObjectName(u"verticalLayout_infoFrame")
        self.verticalLayout_infoFrame.setContentsMargins(0, 8, 0, 8)
        self.labelInfoText = QLabel(self.infoFrame)
        self.labelInfoText.setObjectName(u"labelInfoText")
        self.labelInfoText.setStyleSheet(u"#labelInfoText {\n"
"    color: #6B7280;\n"
"    font-size: 13px;\n"
"}")

        self.verticalLayout_infoFrame.addWidget(self.labelInfoText)

        self.labelInfoDetail = QLabel(self.infoFrame)
        self.labelInfoDetail.setObjectName(u"labelInfoDetail")
        self.labelInfoDetail.setStyleSheet(u"#labelInfoDetail {\n"
"    color: #9CA3AF;\n"
"    font-size: 12px;\n"
"}")

        self.verticalLayout_infoFrame.addWidget(self.labelInfoDetail)


        self.verticalLayout_previewCard.addWidget(self.infoFrame)


        self.verticalLayout_contentOuter.addWidget(self.previewCard)

        self.imageAddFrame = QFrame(self.contentContainer)
        self.imageAddFrame.setObjectName(u"imageAddFrame")
        self.imageAddFrame.setMinimumSize(QSize(0, 56))
        self.imageAddFrame.setMaximumSize(QSize(16777215, 56))
        self.imageAddFrame.setStyleSheet(u"#imageAddFrame {\n"
"    background-color: #F9FAFB;\n"
"    border: 1px solid #E5E7EB;\n"
"    border-radius: 8px;\n"
"}")
        self.imageAddFrame.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_imageAdd = QHBoxLayout(self.imageAddFrame)
        self.horizontalLayout_imageAdd.setSpacing(12)
        self.horizontalLayout_imageAdd.setObjectName(u"horizontalLayout_imageAdd")
        self.horizontalLayout_imageAdd.setContentsMargins(16, 8, 16, 8)
        self.verticalLayout_imageAddLabels = QVBoxLayout()
        self.verticalLayout_imageAddLabels.setSpacing(2)
        self.verticalLayout_imageAddLabels.setObjectName(u"verticalLayout_imageAddLabels")
        self.labelImageCount = QLabel(self.imageAddFrame)
        self.labelImageCount.setObjectName(u"labelImageCount")
        self.labelImageCount.setStyleSheet(u"#labelImageCount {\n"
"    color: #6B7280;\n"
"    font-size: 13px;\n"
"}")

        self.verticalLayout_imageAddLabels.addWidget(self.labelImageCount)

        self.labelImageAddHint = QLabel(self.imageAddFrame)
        self.labelImageAddHint.setObjectName(u"labelImageAddHint")
        self.labelImageAddHint.setStyleSheet(u"#labelImageAddHint {\n"
"    color: #9CA3AF;\n"
"    font-size: 12px;\n"
"}")

        self.verticalLayout_imageAddLabels.addWidget(self.labelImageAddHint)


        self.horizontalLayout_imageAdd.addLayout(self.verticalLayout_imageAddLabels)

        self.horizontalSpacer_imageAdd = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_imageAdd.addItem(self.horizontalSpacer_imageAdd)

        self.btnAddImages = QPushButton(self.imageAddFrame)
        self.btnAddImages.setObjectName(u"btnAddImages")
        self.btnAddImages.setMinimumSize(QSize(120, 36))
        self.btnAddImages.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnAddImages.setStyleSheet(u"#btnAddImages {\n"
"    background-color: #7C3BED;\n"
"    color: #FFFFFF;\n"
"    border: none;\n"
"    border-radius: 6px;\n"
"    padding: 0 20px;\n"
"    font-size: 14px;\n"
"    font-weight: 500;\n"
"}\n"
"#btnAddImages:hover {\n"
"    background-color: #6D28D9;\n"
"}")

        self.horizontalLayout_imageAdd.addWidget(self.btnAddImages)


        self.verticalLayout_contentOuter.addWidget(self.imageAddFrame)

        self.btnGenerate = QPushButton(self.contentContainer)
        self.btnGenerate.setObjectName(u"btnGenerate")
        self.btnGenerate.setMinimumSize(QSize(0, 44))
        self.btnGenerate.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnGenerate.setStyleSheet(u"#btnGenerate {\n"
"    background-color: #7C3BED;\n"
"    color: #FFFFFF;\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"    font-size: 16px;\n"
"    font-weight: 600;\n"
"}\n"
"#btnGenerate:hover {\n"
"    background-color: #6D28D9;\n"
"}")

        self.verticalLayout_contentOuter.addWidget(self.btnGenerate)

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

        ImageSelect.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(ImageSelect)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1000, 17))
        ImageSelect.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(ImageSelect)
        self.statusbar.setObjectName(u"statusbar")
        ImageSelect.setStatusBar(self.statusbar)

        self.retranslateUi(ImageSelect)

        QMetaObject.connectSlotsByName(ImageSelect)
    # setupUi

    def retranslateUi(self, ImageSelect):
        ImageSelect.setWindowTitle(QCoreApplication.translate("ImageSelect", u"\u62fc\u5b57\u5e55 - \u9009\u62e9\u56fe\u7247", None))
        self.logoLabel.setText(QCoreApplication.translate("ImageSelect", u"\u62fc\u5b57\u5e55", None))
        self.btnRestart.setText(QCoreApplication.translate("ImageSelect", u"\u91cd\u65b0\u5f00\u59cb", None))
        self.labelTitle.setText(QCoreApplication.translate("ImageSelect", u"\u8c03\u6574\u5b57\u5e55\u7ebf\u4f4d\u7f6e", None))
        self.labelForceWidth.setText(QCoreApplication.translate("ImageSelect", u"\u5f3a\u5236\u7b49\u5bbd", None))
        self.comboForceWidth.setItemText(0, QCoreApplication.translate("ImageSelect", u"\u4e0d\u5f3a\u5236", None))
        self.comboForceWidth.setItemText(1, QCoreApplication.translate("ImageSelect", u"\u6309\u6700\u7a84", None))
        self.comboForceWidth.setItemText(2, QCoreApplication.translate("ImageSelect", u"\u6309\u6700\u5bbd", None))
        self.comboForceWidth.setItemText(3, QCoreApplication.translate("ImageSelect", u"\u6309\u5f53\u524d", None))

        self.btnSyncAll.setText(QCoreApplication.translate("ImageSelect", u"\u540c\u6b65\u6240\u6709", None))
        self.btnResetDefault.setText(QCoreApplication.translate("ImageSelect", u"\u91cd\u7f6e\u9ed8\u8ba4(\u5f53\u524d)", None))
        self.btnResetAll.setText(QCoreApplication.translate("ImageSelect", u"\u91cd\u7f6e\u9ed8\u8ba4(\u5168\u90e8)", None))
        self.btnPrevImage.setText(QCoreApplication.translate("ImageSelect", u"\u4e0a\u4e00\u5f20", None))
        self.labelImageCounter.setText(QCoreApplication.translate("ImageSelect", u"\u7b2c 1 / 1 \u5f20", None))
        self.btnNextImage.setText(QCoreApplication.translate("ImageSelect", u"\u4e0b\u4e00\u5f20", None))
        self.labelGoToPage.setText(QCoreApplication.translate("ImageSelect", u"\u8f6c\u5230\u7b2c", None))
        self.editGoToPage.setText(QCoreApplication.translate("ImageSelect", u"1", None))
        self.labelGoToPageSuffix.setText(QCoreApplication.translate("ImageSelect", u"\u5f20", None))
        self.btnGoToPage.setText(QCoreApplication.translate("ImageSelect", u"\u8f6c\u5230", None))
        self.labelInfoText.setText(QCoreApplication.translate("ImageSelect", u"\u76f4\u63a5\u62d6\u52a8\u5b57\u5e55\u7ebf\u4e0a\u7684\u624b\u67c4\u8c03\u6574\u4f4d\u7f6e", None))
        self.labelInfoDetail.setText(QCoreApplication.translate("ImageSelect", u"\u5b57\u5e55\u533a\u57df\u9ad8\u5ea6\uff1a20% \u00b7 \u4f4d\u7f6e\u5df2\u81ea\u52a8\u4fdd\u5b58", None))
        self.labelImageCount.setText(QCoreApplication.translate("ImageSelect", u"\u5f53\u524d\u5df2\u6709 3 \u5f20\u56fe\u7247", None))
        self.labelImageAddHint.setText(QCoreApplication.translate("ImageSelect", u"\u53ef\u7ee7\u7eed\u6dfb\u52a0\u56fe\u7247\uff08\u6700\u591a50\u5f20\uff09", None))
        self.btnAddImages.setText(QCoreApplication.translate("ImageSelect", u"\u6dfb\u52a0\u66f4\u591a\u56fe\u7247", None))
        self.btnGenerate.setText(QCoreApplication.translate("ImageSelect", u"\u751f\u6210\u5b57\u5e55\u957f\u56fe", None))
        self.labelFooter.setText(QCoreApplication.translate("ImageSelect", u"<a href=\"https://www.yuanheyuekeji.com/\" style=\"text-decoration:none; color:#9CA3AF;\">\u00a9 2026 \u62fc\u5b57\u5e55 - \u5feb\u901f\u751f\u6210\u8fde\u7eed\u5b57\u5e55\u957f\u56fe</a>", None))
    # retranslateUi

