# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'videoselect.ui'
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
    QLabel, QMainWindow, QProgressBar, QPushButton,
    QSizePolicy, QSlider, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_fileselect(object):
    def setupUi(self, fileselect):
        if not fileselect.objectName():
            fileselect.setObjectName(u"fileselect")
        fileselect.resize(1000, 650)
        fileselect.setMinimumSize(QSize(800, 600))
        fileselect.setStyleSheet(u"QMainWindow {\n"
"    background-color: #FFFFFF;\n"
"    font-family: \"Microsoft YaHei\", \"Segoe UI\", sans-serif;\n"
"}\n"
"QLabel {\n"
"    color: #111827;\n"
"}")
        self.centralwidget = QWidget(fileselect)
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
        self.horizontalLayout_workArea = QHBoxLayout()
        self.horizontalLayout_workArea.setSpacing(20)
        self.horizontalLayout_workArea.setObjectName(u"horizontalLayout_workArea")
        self.leftPanel = QWidget(self.contentContainer)
        self.leftPanel.setObjectName(u"leftPanel")
        self.verticalLayout_leftPanel = QVBoxLayout(self.leftPanel)
        self.verticalLayout_leftPanel.setSpacing(18)
        self.verticalLayout_leftPanel.setObjectName(u"verticalLayout_leftPanel")
        self.verticalLayout_leftPanel.setContentsMargins(0, 0, 0, 0)
        self.labelExtractTitle = QLabel(self.leftPanel)
        self.labelExtractTitle.setObjectName(u"labelExtractTitle")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelExtractTitle.sizePolicy().hasHeightForWidth())
        self.labelExtractTitle.setSizePolicy(sizePolicy)
        self.labelExtractTitle.setStyleSheet(u"#labelExtractTitle {\n"
"    color: #000000;\n"
"    font-size: 24px;\n"
"    font-weight: 700;\n"
"}")

        self.verticalLayout_leftPanel.addWidget(self.labelExtractTitle)

        self.videoSummaryFrame = QFrame(self.leftPanel)
        self.videoSummaryFrame.setObjectName(u"videoSummaryFrame")
        sizePolicy.setHeightForWidth(self.videoSummaryFrame.sizePolicy().hasHeightForWidth())
        self.videoSummaryFrame.setSizePolicy(sizePolicy)
        self.videoSummaryFrame.setStyleSheet(u"#videoSummaryFrame {\n"
"    background-color: #F9FAFB;\n"
"    border: 1px solid #E5E7EB;\n"
"    border-radius: 8px;\n"
"}")
        self.videoSummaryFrame.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_videoSummary = QVBoxLayout(self.videoSummaryFrame)
        self.verticalLayout_videoSummary.setSpacing(6)
        self.verticalLayout_videoSummary.setObjectName(u"verticalLayout_videoSummary")
        self.verticalLayout_videoSummary.setContentsMargins(16, 12, 16, 12)
        self.labelExtractSubtitle = QLabel(self.videoSummaryFrame)
        self.labelExtractSubtitle.setObjectName(u"labelExtractSubtitle")
        self.labelExtractSubtitle.setStyleSheet(u"#labelExtractSubtitle {\n"
"    color: #111827;\n"
"    font-size: 16px;\n"
"    font-weight: 500;\n"
"}")

        self.verticalLayout_videoSummary.addWidget(self.labelExtractSubtitle)

        self.labelVideoInfo = QLabel(self.videoSummaryFrame)
        self.labelVideoInfo.setObjectName(u"labelVideoInfo")
        self.labelVideoInfo.setStyleSheet(u"#labelVideoInfo {\n"
"    color: #6B7280;\n"
"    font-size: 13px;\n"
"}")

        self.verticalLayout_videoSummary.addWidget(self.labelVideoInfo)


        self.verticalLayout_leftPanel.addWidget(self.videoSummaryFrame)

        self.videoPreviewFrame = QFrame(self.leftPanel)
        self.videoPreviewFrame.setObjectName(u"videoPreviewFrame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(1)
        sizePolicy1.setVerticalStretch(1)
        sizePolicy1.setHeightForWidth(self.videoPreviewFrame.sizePolicy().hasHeightForWidth())
        self.videoPreviewFrame.setSizePolicy(sizePolicy1)
        self.videoPreviewFrame.setStyleSheet(u"#videoPreviewFrame {\n"
"    background-color: #111827;\n"
"    border: 1px solid #E5E7EB;\n"
"    border-radius: 10px;\n"
"}")
        self.videoPreviewFrame.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_videoPreview = QVBoxLayout(self.videoPreviewFrame)
        self.verticalLayout_videoPreview.setSpacing(0)
        self.verticalLayout_videoPreview.setObjectName(u"verticalLayout_videoPreview")
        self.verticalLayout_videoPreview.setContentsMargins(0, 0, 0, 0)
        self.videoAreaFrame = QFrame(self.videoPreviewFrame)
        self.videoAreaFrame.setObjectName(u"videoAreaFrame")
        self.videoAreaFrame.setStyleSheet(u"#videoAreaFrame {\n"
"    background-color: #000000;\n"
"    border: none;\n"
"    border-radius: 10px 10px 0 0;\n"
"}")
        self.videoAreaFrame.setFrameShape(QFrame.NoFrame)

        self.verticalLayout_videoPreview.addWidget(self.videoAreaFrame)

        self.videoProgressFrame = QFrame(self.videoPreviewFrame)
        self.videoProgressFrame.setObjectName(u"videoProgressFrame")
        self.videoProgressFrame.setMinimumSize(QSize(0, 56))
        self.videoProgressFrame.setMaximumSize(QSize(16777215, 56))
        self.videoProgressFrame.setStyleSheet(u"#videoProgressFrame {\n"
"    background-color: rgba(17, 24, 39, 200);\n"
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

        self.sliderCurrentTime = QSlider(self.videoProgressFrame)
        self.sliderCurrentTime.setObjectName(u"sliderCurrentTime")
        self.sliderCurrentTime.setMinimumSize(QSize(0, 20))
        self.sliderCurrentTime.setOrientation(Qt.Horizontal)

        self.horizontalLayout_videoControls.addWidget(self.sliderCurrentTime)

        self.btnAudioPlayPause = QPushButton(self.videoProgressFrame)
        self.btnAudioPlayPause.setObjectName(u"btnAudioPlayPause")
        self.btnAudioPlayPause.setMinimumSize(QSize(36, 36))
        self.btnAudioPlayPause.setMaximumSize(QSize(36, 36))
        self.btnAudioPlayPause.setStyleSheet(u"#btnAudioPlayPause {\n"
"    background-color: #7C3BED;\n"
"    border: none;\n"
"    border-radius: 18px;\n"
"}\n"
"#btnAudioPlayPause:hover {\n"
"    background-color: #6D28D9;\n"
"}")
        self.btnAudioPlayPause.setIconSize(QSize(18, 18))

        self.horizontalLayout_videoControls.addWidget(self.btnAudioPlayPause)

        self.labelCurrentTime = QLabel(self.videoProgressFrame)
        self.labelCurrentTime.setObjectName(u"labelCurrentTime")
        self.labelCurrentTime.setMinimumSize(QSize(90, 0))
        self.labelCurrentTime.setStyleSheet(u"#labelCurrentTime {\n"
"    color: #FFFFFF;\n"
"    font-size: 13px;\n"
"}")
        self.labelCurrentTime.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_videoControls.addWidget(self.labelCurrentTime)


        self.verticalLayout_videoPreview.addWidget(self.videoProgressFrame)


        self.verticalLayout_leftPanel.addWidget(self.videoPreviewFrame)


        self.horizontalLayout_workArea.addWidget(self.leftPanel)

        self.operationPanel = QFrame(self.contentContainer)
        self.operationPanel.setObjectName(u"operationPanel")
        sizePolicy.setHeightForWidth(self.operationPanel.sizePolicy().hasHeightForWidth())
        self.operationPanel.setSizePolicy(sizePolicy)
        self.operationPanel.setMinimumSize(QSize(420, 0))
        self.operationPanel.setMaximumSize(QSize(460, 16777215))
        self.operationPanel.setStyleSheet(u"#operationPanel {\n"
"    background-color: #FFFFFF;\n"
"    border: 1px solid #E5E7EB;\n"
"    border-radius: 10px;\n"
"}")
        self.operationPanel.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_operationPanel = QVBoxLayout(self.operationPanel)
        self.verticalLayout_operationPanel.setSpacing(16)
        self.verticalLayout_operationPanel.setObjectName(u"verticalLayout_operationPanel")
        self.verticalLayout_operationPanel.setContentsMargins(18, 18, 18, 18)
        self.rangePanel = QFrame(self.operationPanel)
        self.rangePanel.setObjectName(u"rangePanel")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.rangePanel.sizePolicy().hasHeightForWidth())
        self.rangePanel.setSizePolicy(sizePolicy2)
        self.rangePanel.setMinimumSize(QSize(0, 276))
        self.rangePanel.setStyleSheet(u"#rangePanel {\n"
"    background-color: #F9FAFB;\n"
"    border: 1px solid #E5E7EB;\n"
"    border-radius: 8px;\n"
"}")
        self.rangePanel.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_rangePanel = QVBoxLayout(self.rangePanel)
        self.verticalLayout_rangePanel.setSpacing(12)
        self.verticalLayout_rangePanel.setObjectName(u"verticalLayout_rangePanel")
        self.verticalLayout_rangePanel.setContentsMargins(14, 14, 14, 14)
        self.labelRangeTitle = QLabel(self.rangePanel)
        self.labelRangeTitle.setObjectName(u"labelRangeTitle")
        self.labelRangeTitle.setStyleSheet(u"#labelRangeTitle {\n"
"    color: #111827;\n"
"    font-size: 15px;\n"
"    font-weight: 600;\n"
"}")

        self.verticalLayout_rangePanel.addWidget(self.labelRangeTitle)

        self.horizontalLayout_startTimeHeader = QHBoxLayout()
        self.horizontalLayout_startTimeHeader.setObjectName(u"horizontalLayout_startTimeHeader")
        self.labelStartTimeTitle = QLabel(self.rangePanel)
        self.labelStartTimeTitle.setObjectName(u"labelStartTimeTitle")

        self.horizontalLayout_startTimeHeader.addWidget(self.labelStartTimeTitle)

        self.labelStartTimeValue = QLabel(self.rangePanel)
        self.labelStartTimeValue.setObjectName(u"labelStartTimeValue")
        self.labelStartTimeValue.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_startTimeHeader.addWidget(self.labelStartTimeValue)

        self.btnSetStartCurrent = QPushButton(self.rangePanel)
        self.btnSetStartCurrent.setObjectName(u"btnSetStartCurrent")
        self.btnSetStartCurrent.setMinimumSize(QSize(24, 24))

        self.horizontalLayout_startTimeHeader.addWidget(self.btnSetStartCurrent)


        self.verticalLayout_rangePanel.addLayout(self.horizontalLayout_startTimeHeader)

        self.sliderStartTime = QSlider(self.rangePanel)
        self.sliderStartTime.setObjectName(u"sliderStartTime")
        self.sliderStartTime.setOrientation(Qt.Horizontal)

        self.verticalLayout_rangePanel.addWidget(self.sliderStartTime)

        self.horizontalLayout_endTimeHeader = QHBoxLayout()
        self.horizontalLayout_endTimeHeader.setObjectName(u"horizontalLayout_endTimeHeader")
        self.labelEndTimeTitle = QLabel(self.rangePanel)
        self.labelEndTimeTitle.setObjectName(u"labelEndTimeTitle")

        self.horizontalLayout_endTimeHeader.addWidget(self.labelEndTimeTitle)

        self.labelEndTimeValue = QLabel(self.rangePanel)
        self.labelEndTimeValue.setObjectName(u"labelEndTimeValue")
        self.labelEndTimeValue.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_endTimeHeader.addWidget(self.labelEndTimeValue)

        self.btnSetEndCurrent = QPushButton(self.rangePanel)
        self.btnSetEndCurrent.setObjectName(u"btnSetEndCurrent")
        self.btnSetEndCurrent.setMinimumSize(QSize(24, 24))

        self.horizontalLayout_endTimeHeader.addWidget(self.btnSetEndCurrent)


        self.verticalLayout_rangePanel.addLayout(self.horizontalLayout_endTimeHeader)

        self.sliderEndTime = QSlider(self.rangePanel)
        self.sliderEndTime.setObjectName(u"sliderEndTime")
        self.sliderEndTime.setOrientation(Qt.Horizontal)

        self.verticalLayout_rangePanel.addWidget(self.sliderEndTime)

        self.rangeInfoFrame = QFrame(self.rangePanel)
        self.rangeInfoFrame.setObjectName(u"rangeInfoFrame")
        self.rangeInfoFrame.setMinimumSize(QSize(0, 70))
        self.rangeInfoFrame.setStyleSheet(u"#rangeInfoFrame {\n"
"    background-color: #FFFFFF;\n"
"    border-radius: 6px;\n"
"}")
        self.rangeInfoFrame.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_rangeInfo = QVBoxLayout(self.rangeInfoFrame)
        self.verticalLayout_rangeInfo.setSpacing(8)
        self.verticalLayout_rangeInfo.setObjectName(u"verticalLayout_rangeInfo")
        self.verticalLayout_rangeInfo.setContentsMargins(12, 10, 12, 10)
        self.horizontalLayout_selectedDuration = QHBoxLayout()
        self.horizontalLayout_selectedDuration.setObjectName(u"horizontalLayout_selectedDuration")
        self.labelSelectedDurationTitle = QLabel(self.rangeInfoFrame)
        self.labelSelectedDurationTitle.setObjectName(u"labelSelectedDurationTitle")
        self.labelSelectedDurationTitle.setMinimumSize(QSize(0, 12))

        self.horizontalLayout_selectedDuration.addWidget(self.labelSelectedDurationTitle)

        self.labelSelectedDurationValue = QLabel(self.rangeInfoFrame)
        self.labelSelectedDurationValue.setObjectName(u"labelSelectedDurationValue")
        self.labelSelectedDurationValue.setMinimumSize(QSize(0, 12))
        self.labelSelectedDurationValue.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_selectedDuration.addWidget(self.labelSelectedDurationValue)


        self.verticalLayout_rangeInfo.addLayout(self.horizontalLayout_selectedDuration)

        self.horizontalLayout_estimatedFrames = QHBoxLayout()
        self.horizontalLayout_estimatedFrames.setObjectName(u"horizontalLayout_estimatedFrames")
        self.labelEstimatedFramesTitle = QLabel(self.rangeInfoFrame)
        self.labelEstimatedFramesTitle.setObjectName(u"labelEstimatedFramesTitle")
        self.labelEstimatedFramesTitle.setMinimumSize(QSize(0, 12))

        self.horizontalLayout_estimatedFrames.addWidget(self.labelEstimatedFramesTitle)

        self.labelEstimatedFramesValue = QLabel(self.rangeInfoFrame)
        self.labelEstimatedFramesValue.setObjectName(u"labelEstimatedFramesValue")
        self.labelEstimatedFramesValue.setMinimumSize(QSize(0, 12))
        self.labelEstimatedFramesValue.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_estimatedFrames.addWidget(self.labelEstimatedFramesValue)


        self.verticalLayout_rangeInfo.addLayout(self.horizontalLayout_estimatedFrames)


        self.verticalLayout_rangePanel.addWidget(self.rangeInfoFrame)


        self.verticalLayout_operationPanel.addWidget(self.rangePanel)

        self.horizontalLayout_frequency = QHBoxLayout()
        self.horizontalLayout_frequency.setObjectName(u"horizontalLayout_frequency")
        self.labelFrequencyTitle = QLabel(self.operationPanel)
        self.labelFrequencyTitle.setObjectName(u"labelFrequencyTitle")

        self.horizontalLayout_frequency.addWidget(self.labelFrequencyTitle)

        self.comboFrequency = QComboBox(self.operationPanel)
        self.comboFrequency.addItem("")
        self.comboFrequency.addItem("")
        self.comboFrequency.addItem("")
        self.comboFrequency.addItem("")
        self.comboFrequency.addItem("")
        self.comboFrequency.setObjectName(u"comboFrequency")

        self.horizontalLayout_frequency.addWidget(self.comboFrequency)


        self.verticalLayout_operationPanel.addLayout(self.horizontalLayout_frequency)

        self.progressExtract = QProgressBar(self.operationPanel)
        self.progressExtract.setObjectName(u"progressExtract")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.progressExtract.sizePolicy().hasHeightForWidth())
        self.progressExtract.setSizePolicy(sizePolicy3)
        self.progressExtract.setMinimumSize(QSize(0, 20))
        self.progressExtract.setMaximumSize(QSize(16777215, 20))
        self.progressExtract.setValue(0)

        self.verticalLayout_operationPanel.addWidget(self.progressExtract)

        self.labelProgressText = QLabel(self.operationPanel)
        self.labelProgressText.setObjectName(u"labelProgressText")
        self.labelProgressText.setStyleSheet(u"#labelProgressText {\n"
"    color: #6B7280;\n"
"    font-size: 13px;\n"
"}")
        self.labelProgressText.setAlignment(Qt.AlignCenter)

        self.verticalLayout_operationPanel.addWidget(self.labelProgressText)

        self.btnStartExtract = QPushButton(self.operationPanel)
        self.btnStartExtract.setObjectName(u"btnStartExtract")
        self.btnStartExtract.setMinimumSize(QSize(0, 42))
        self.btnStartExtract.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnStartExtract.setStyleSheet(u"#btnStartExtract {\n"
"    background-color: #7C3BED;\n"
"    color: #FFFFFF;\n"
"    border: none;\n"
"    border-radius: 6px;\n"
"    padding: 0 22px;\n"
"    font-size: 14px;\n"
"    font-weight: 500;\n"
"}\n"
"#btnStartExtract:hover {\n"
"    background-color: #6D28D9;\n"
"}")

        self.verticalLayout_operationPanel.addWidget(self.btnStartExtract)

        self.btnBackToMain = QPushButton(self.operationPanel)
        self.btnBackToMain.setObjectName(u"btnBackToMain")
        self.btnBackToMain.setMinimumSize(QSize(0, 42))
        self.btnBackToMain.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnBackToMain.setStyleSheet(u"#btnBackToMain {\n"
"    background-color: #FFFFFF;\n"
"    color: #374151;\n"
"    border: 1px solid #D1D5DB;\n"
"    border-radius: 6px;\n"
"    padding: 0 22px;\n"
"    font-size: 14px;\n"
"    font-weight: 500;\n"
"}\n"
"#btnBackToMain:hover {\n"
"    background-color: #F9FAFB;\n"
"}")

        self.verticalLayout_operationPanel.addWidget(self.btnBackToMain)

        self.labelExtractTip = QLabel(self.operationPanel)
        self.labelExtractTip.setObjectName(u"labelExtractTip")
        self.labelExtractTip.setStyleSheet(u"#labelExtractTip {\n"
"    color: #6B7280;\n"
"    font-size: 12px;\n"
"}")
        self.labelExtractTip.setWordWrap(True)

        self.verticalLayout_operationPanel.addWidget(self.labelExtractTip)


        self.horizontalLayout_workArea.addWidget(self.operationPanel)


        self.verticalLayout_contentOuter.addLayout(self.horizontalLayout_workArea)


        self.verticalLayout_main.addWidget(self.contentContainer)

        self.footerFrame = QFrame(self.centralwidget)
        self.footerFrame.setObjectName(u"footerFrame")
        sizePolicy3.setHeightForWidth(self.footerFrame.sizePolicy().hasHeightForWidth())
        self.footerFrame.setSizePolicy(sizePolicy3)
        self.footerFrame.setMinimumSize(QSize(0, 56))
        self.footerFrame.setMaximumSize(QSize(16777215, 56))
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

        fileselect.setCentralWidget(self.centralwidget)

        self.retranslateUi(fileselect)

        self.comboFrequency.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(fileselect)
    # setupUi

    def retranslateUi(self, fileselect):
        fileselect.setWindowTitle(QCoreApplication.translate("fileselect", u"\u62fc\u5b57\u5e55 - \u63d0\u53d6\u5e27\u753b\u9762", None))
        self.logoLabel.setText(QCoreApplication.translate("fileselect", u"\u62fc\u5b57\u5e55", None))
        self.btnRestart.setText(QCoreApplication.translate("fileselect", u"\u91cd\u65b0\u5f00\u59cb", None))
        self.labelExtractTitle.setText(QCoreApplication.translate("fileselect", u"\u89c6\u9891\u5e27\u63d0\u53d6", None))
        self.labelExtractSubtitle.setText("")
        self.labelVideoInfo.setText(QCoreApplication.translate("fileselect", u"\u65f6\u957f: 00:00  | \u5e27\u7387: 24fps | \u5e27\u6570: 6000", None))
        self.btnPlayPause.setText("")
        self.btnAudioPlayPause.setText("")
        self.labelCurrentTime.setText(QCoreApplication.translate("fileselect", u"00:00 / 00:00", None))
        self.labelRangeTitle.setText(QCoreApplication.translate("fileselect", u"\u9009\u62e9\u63d0\u53d6\u8303\u56f4", None))
        self.labelStartTimeTitle.setText(QCoreApplication.translate("fileselect", u"\u5f00\u59cb\u65f6\u95f4", None))
        self.labelStartTimeValue.setText(QCoreApplication.translate("fileselect", u"00:00", None))
        self.btnSetStartCurrent.setText(QCoreApplication.translate("fileselect", u"\u8bbe\u4e3a\u5f00\u59cb", None))
        self.labelEndTimeTitle.setText(QCoreApplication.translate("fileselect", u"\u7ed3\u675f\u65f6\u95f4", None))
        self.labelEndTimeValue.setText(QCoreApplication.translate("fileselect", u"00:00", None))
        self.btnSetEndCurrent.setText(QCoreApplication.translate("fileselect", u"\u8bbe\u4e3a\u7ed3\u675f", None))
        self.labelSelectedDurationTitle.setText(QCoreApplication.translate("fileselect", u"\u9009\u4e2d\u65f6\u957f\uff1a", None))
        self.labelSelectedDurationValue.setText(QCoreApplication.translate("fileselect", u"00:00", None))
        self.labelEstimatedFramesTitle.setText(QCoreApplication.translate("fileselect", u"\u9884\u8ba1\u63d0\u53d6\u5e27\u6570\uff1a", None))
        self.labelEstimatedFramesValue.setText(QCoreApplication.translate("fileselect", u"0 \u5e27", None))
        self.labelFrequencyTitle.setText(QCoreApplication.translate("fileselect", u"\u63d0\u53d6\u9891\u7387", None))
        self.comboFrequency.setItemText(0, QCoreApplication.translate("fileselect", u"0.5s/\u5e27", None))
        self.comboFrequency.setItemText(1, QCoreApplication.translate("fileselect", u"1s/\u5e27", None))
        self.comboFrequency.setItemText(2, QCoreApplication.translate("fileselect", u"2s/\u5e27", None))
        self.comboFrequency.setItemText(3, QCoreApplication.translate("fileselect", u"3s/\u5e27", None))
        self.comboFrequency.setItemText(4, QCoreApplication.translate("fileselect", u"\u5168\u90e8\u5e27", None))

        self.labelProgressText.setText(QCoreApplication.translate("fileselect", u"\u7b49\u5f85\u5f00\u59cb\u63d0\u53d6", None))
        self.btnStartExtract.setText(QCoreApplication.translate("fileselect", u"\u5f00\u59cb\u63d0\u53d6\u5e27\u753b\u9762", None))
        self.btnBackToMain.setText(QCoreApplication.translate("fileselect", u"\u8fd4\u56de", None))
        self.labelExtractTip.setText(QCoreApplication.translate("fileselect", u"\u7cfb\u7edf\u5c06\u5728\u9009\u4e2d\u7684\u65f6\u95f4\u8303\u56f4\u5185\u6309\u6240\u9009\u9891\u7387\u63d0\u53d6\u753b\u9762\uff0c\u7528\u4e8e\u751f\u6210\u5b57\u5e55\u957f\u56fe", None))
        self.labelFooter.setText(QCoreApplication.translate("fileselect", u"\u00a9 2026 \u62fc\u5b57\u5e55 - \u5feb\u901f\u751f\u6210\u8fde\u7eed\u5b57\u5e55\u957f\u56fe", None))
    # retranslateUi

