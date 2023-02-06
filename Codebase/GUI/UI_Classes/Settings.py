# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SettingsXWJbwM.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class SettingsUI(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(836, 628)
        Form.setMinimumSize(QSize(600, 400))
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.SettingsScrollArea = QScrollArea(Form)
        self.SettingsScrollArea.setObjectName(u"SettingsScrollArea")
        self.SettingsScrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 799, 1271))
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.PrColorSettingsFrame = QFrame(self.scrollAreaWidgetContents)
        self.PrColorSettingsFrame.setObjectName(u"PrColorSettingsFrame")
        self.PrColorSettingsFrame.setFrameShape(QFrame.StyledPanel)
        self.PrColorSettingsFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.PrColorSettingsFrame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.ColorSettingsLabel = QLabel(self.PrColorSettingsFrame)
        self.ColorSettingsLabel.setObjectName(u"ColorSettingsLabel")
        font = QFont()
        font.setPointSize(16)
        self.ColorSettingsLabel.setFont(font)
        self.ColorSettingsLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.ColorSettingsLabel)

        self.DisplayBehavioursFrame = QFrame(self.PrColorSettingsFrame)
        self.DisplayBehavioursFrame.setObjectName(u"DisplayBehavioursFrame")
        self.DisplayBehavioursFrame.setFrameShape(QFrame.StyledPanel)
        self.DisplayBehavioursFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.DisplayBehavioursFrame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.SidebarScaleLabel = QLabel(self.DisplayBehavioursFrame)
        self.SidebarScaleLabel.setObjectName(u"SidebarScaleLabel")
        font1 = QFont()
        font1.setPointSize(9)
        self.SidebarScaleLabel.setFont(font1)
        self.SidebarScaleLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.SidebarScaleLabel, 4, 0, 2, 2)

        self.SecDispHeight = QSpinBox(self.DisplayBehavioursFrame)
        self.SecDispHeight.setObjectName(u"SecDispHeight")
        self.SecDispHeight.setMinimumSize(QSize(0, 40))
        self.SecDispHeight.setMinimum(100)
        self.SecDispHeight.setMaximum(16777215)
        self.SecDispHeight.setSingleStep(5)

        self.gridLayout_2.addWidget(self.SecDispHeight, 2, 3, 1, 1)

        self.MinTaskHtLabel = QLabel(self.DisplayBehavioursFrame)
        self.MinTaskHtLabel.setObjectName(u"MinTaskHtLabel")
        self.MinTaskHtLabel.setFont(font1)
        self.MinTaskHtLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.MinTaskHtLabel, 1, 0, 1, 2)

        self.MinProjButHtLabel = QLabel(self.DisplayBehavioursFrame)
        self.MinProjButHtLabel.setObjectName(u"MinProjButHtLabel")
        self.MinProjButHtLabel.setFont(font1)
        self.MinProjButHtLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.MinProjButHtLabel, 3, 0, 1, 2)

        self.ProjButtonHeight = QSpinBox(self.DisplayBehavioursFrame)
        self.ProjButtonHeight.setObjectName(u"ProjButtonHeight")
        self.ProjButtonHeight.setMinimumSize(QSize(0, 40))
        self.ProjButtonHeight.setMinimum(20)
        self.ProjButtonHeight.setMaximum(16777215)
        self.ProjButtonHeight.setSingleStep(5)

        self.gridLayout_2.addWidget(self.ProjButtonHeight, 3, 3, 1, 1)

        self.TaskDispHeight = QSpinBox(self.DisplayBehavioursFrame)
        self.TaskDispHeight.setObjectName(u"TaskDispHeight")
        self.TaskDispHeight.setMinimumSize(QSize(0, 40))
        self.TaskDispHeight.setMinimum(100)
        self.TaskDispHeight.setMaximum(16777215)
        self.TaskDispHeight.setSingleStep(5)

        self.gridLayout_2.addWidget(self.TaskDispHeight, 1, 3, 1, 1)

        self.MinSecHtLabel = QLabel(self.DisplayBehavioursFrame)
        self.MinSecHtLabel.setObjectName(u"MinSecHtLabel")
        self.MinSecHtLabel.setFont(font1)
        self.MinSecHtLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.MinSecHtLabel, 2, 0, 1, 2)

        self.SidebarScaleFactor = QDoubleSpinBox(self.DisplayBehavioursFrame)
        self.SidebarScaleFactor.setObjectName(u"SidebarScaleFactor")
        self.SidebarScaleFactor.setMinimumSize(QSize(0, 40))
        self.SidebarScaleFactor.setDecimals(4)
        self.SidebarScaleFactor.setMaximum(1.000000000000000)
        self.SidebarScaleFactor.setSingleStep(0.010000000000000)

        self.gridLayout_2.addWidget(self.SidebarScaleFactor, 4, 3, 2, 1)

        self.DisplayBehaviourLabel = QLabel(self.DisplayBehavioursFrame)
        self.DisplayBehaviourLabel.setObjectName(u"DisplayBehaviourLabel")
        self.DisplayBehaviourLabel.setFont(font)
        self.DisplayBehaviourLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.DisplayBehaviourLabel, 0, 0, 1, 4)

        self.HelpBehaviour = QCheckBox(self.DisplayBehavioursFrame)
        self.HelpBehaviour.setObjectName(u"HelpBehaviour")
        self.HelpBehaviour.setMinimumSize(QSize(0, 30))
        font2 = QFont()
        font2.setPointSize(10)
        self.HelpBehaviour.setFont(font2)
        self.HelpBehaviour.setStyleSheet(u"")
        self.HelpBehaviour.setChecked(False)

        self.gridLayout_2.addWidget(self.HelpBehaviour, 6, 0, 1, 4)

        self.ResetButton = QPushButton(self.DisplayBehavioursFrame)
        self.ResetButton.setObjectName(u"ResetButton")
        self.ResetButton.setMinimumSize(QSize(0, 40))

        self.gridLayout_2.addWidget(self.ResetButton, 7, 0, 1, 2)


        self.verticalLayout_2.addWidget(self.DisplayBehavioursFrame)

        self.PRColorLabel = QLabel(self.PrColorSettingsFrame)
        self.PRColorLabel.setObjectName(u"PRColorLabel")
        font3 = QFont()
        font3.setPointSize(14)
        self.PRColorLabel.setFont(font3)
        self.PRColorLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.PRColorLabel)

        self.Pr1 = QPushButton(self.PrColorSettingsFrame)
        self.Pr1.setObjectName(u"Pr1")
        self.Pr1.setMinimumSize(QSize(0, 40))

        self.verticalLayout_2.addWidget(self.Pr1)

        self.Pr2 = QPushButton(self.PrColorSettingsFrame)
        self.Pr2.setObjectName(u"Pr2")
        self.Pr2.setMinimumSize(QSize(0, 40))

        self.verticalLayout_2.addWidget(self.Pr2)

        self.Pr3 = QPushButton(self.PrColorSettingsFrame)
        self.Pr3.setObjectName(u"Pr3")
        self.Pr3.setMinimumSize(QSize(0, 40))

        self.verticalLayout_2.addWidget(self.Pr3)

        self.Pr4 = QPushButton(self.PrColorSettingsFrame)
        self.Pr4.setObjectName(u"Pr4")
        self.Pr4.setMinimumSize(QSize(0, 40))

        self.verticalLayout_2.addWidget(self.Pr4)

        self.Pr5 = QPushButton(self.PrColorSettingsFrame)
        self.Pr5.setObjectName(u"Pr5")
        self.Pr5.setMinimumSize(QSize(0, 40))

        self.verticalLayout_2.addWidget(self.Pr5)

        self.Pr6 = QPushButton(self.PrColorSettingsFrame)
        self.Pr6.setObjectName(u"Pr6")
        self.Pr6.setMinimumSize(QSize(0, 40))

        self.verticalLayout_2.addWidget(self.Pr6)

        self.Pr7 = QPushButton(self.PrColorSettingsFrame)
        self.Pr7.setObjectName(u"Pr7")
        self.Pr7.setMinimumSize(QSize(0, 40))

        self.verticalLayout_2.addWidget(self.Pr7)

        self.Pr8 = QPushButton(self.PrColorSettingsFrame)
        self.Pr8.setObjectName(u"Pr8")
        self.Pr8.setMinimumSize(QSize(0, 40))

        self.verticalLayout_2.addWidget(self.Pr8)

        self.Pr9 = QPushButton(self.PrColorSettingsFrame)
        self.Pr9.setObjectName(u"Pr9")
        self.Pr9.setMinimumSize(QSize(0, 40))

        self.verticalLayout_2.addWidget(self.Pr9)

        self.Pr10 = QPushButton(self.PrColorSettingsFrame)
        self.Pr10.setObjectName(u"Pr10")
        self.Pr10.setMinimumSize(QSize(0, 40))

        self.verticalLayout_2.addWidget(self.Pr10)

        self.DefaultValueButton = QPushButton(self.PrColorSettingsFrame)
        self.DefaultValueButton.setObjectName(u"DefaultValueButton")
        self.DefaultValueButton.setMinimumSize(QSize(0, 40))

        self.verticalLayout_2.addWidget(self.DefaultValueButton)


        self.verticalLayout.addWidget(self.PrColorSettingsFrame)

        self.ThemesFrame = QFrame(self.scrollAreaWidgetContents)
        self.ThemesFrame.setObjectName(u"ThemesFrame")
        self.ThemesFrame.setFrameShape(QFrame.StyledPanel)
        self.ThemesFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.ThemesFrame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.ThemesLabel = QLabel(self.ThemesFrame)
        self.ThemesLabel.setObjectName(u"ThemesLabel")
        self.ThemesLabel.setMinimumSize(QSize(0, 50))
        self.ThemesLabel.setFont(font)
        self.ThemesLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.ThemesLabel)

        self.PreSetThemesFrame = QFrame(self.ThemesFrame)
        self.PreSetThemesFrame.setObjectName(u"PreSetThemesFrame")
        self.PreSetThemesFrame.setFrameShape(QFrame.StyledPanel)
        self.PreSetThemesFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.PreSetThemesFrame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.DefaultTheme = QPushButton(self.PreSetThemesFrame)
        self.DefaultTheme.setObjectName(u"DefaultTheme")
        self.DefaultTheme.setMinimumSize(QSize(0, 40))

        self.verticalLayout_4.addWidget(self.DefaultTheme)

        self.DayTheme = QPushButton(self.PreSetThemesFrame)
        self.DayTheme.setObjectName(u"DayTheme")
        self.DayTheme.setMinimumSize(QSize(0, 40))

        self.verticalLayout_4.addWidget(self.DayTheme)

        self.TwilightTheme = QPushButton(self.PreSetThemesFrame)
        self.TwilightTheme.setObjectName(u"TwilightTheme")
        self.TwilightTheme.setMinimumSize(QSize(0, 40))

        self.verticalLayout_4.addWidget(self.TwilightTheme)

        self.Phantasmagoric = QPushButton(self.PreSetThemesFrame)
        self.Phantasmagoric.setObjectName(u"Phantasmagoric")
        self.Phantasmagoric.setMinimumSize(QSize(0, 40))

        self.verticalLayout_4.addWidget(self.Phantasmagoric)


        self.verticalLayout_3.addWidget(self.PreSetThemesFrame)

        self.frame = QFrame(self.ThemesFrame)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Sunken)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.CancelChanges = QPushButton(self.frame)
        self.CancelChanges.setObjectName(u"CancelChanges")
        self.CancelChanges.setMinimumSize(QSize(0, 50))

        self.horizontalLayout.addWidget(self.CancelChanges)

        self.SaveChanges = QPushButton(self.frame)
        self.SaveChanges.setObjectName(u"SaveChanges")
        self.SaveChanges.setMinimumSize(QSize(0, 50))

        self.horizontalLayout.addWidget(self.SaveChanges)

        self.SaveChangesRestart = QPushButton(self.frame)
        self.SaveChangesRestart.setObjectName(u"SaveChangesRestart")
        self.SaveChangesRestart.setMinimumSize(QSize(0, 50))

        self.horizontalLayout.addWidget(self.SaveChangesRestart)


        self.verticalLayout_3.addWidget(self.frame)


        self.verticalLayout.addWidget(self.ThemesFrame)

        self.SettingsScrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout.addWidget(self.SettingsScrollArea, 1, 1, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.ColorSettingsLabel.setText(QCoreApplication.translate("Form", u"Color Settings", None))
        self.SidebarScaleLabel.setText(QCoreApplication.translate("Form", u"SideBar Scaling Factor (Requires Restart)", None))
        self.SecDispHeight.setSuffix(QCoreApplication.translate("Form", u" pixels", None))
        self.SecDispHeight.setPrefix("")
        self.MinTaskHtLabel.setText(QCoreApplication.translate("Form", u"Minimum Task Display Height (Tasks Displayed are atleast this tall)", None))
        self.MinProjButHtLabel.setText(QCoreApplication.translate("Form", u"Minimum Project Button Height (Requires Restart)", None))
        self.ProjButtonHeight.setSuffix(QCoreApplication.translate("Form", u" pixels", None))
        self.ProjButtonHeight.setPrefix("")
        self.TaskDispHeight.setSuffix(QCoreApplication.translate("Form", u" pixels", None))
        self.TaskDispHeight.setPrefix("")
        self.MinSecHtLabel.setText(QCoreApplication.translate("Form", u"Minimum Section Display Height ", None))
        self.DisplayBehaviourLabel.setText(QCoreApplication.translate("Form", u"Display Behaviours (Requires Program Restart)", None))
        self.HelpBehaviour.setText(QCoreApplication.translate("Form", u"Show Help Page when Opening up app (Shows today's tasks if this option is turned off)", None))
        self.ResetButton.setText(QCoreApplication.translate("Form", u"Reset Values To Default", None))
        self.PRColorLabel.setText(QCoreApplication.translate("Form", u"Priority Level Color Settings", None))
        self.Pr1.setText(QCoreApplication.translate("Form", u"Priority 1", None))
        self.Pr2.setText(QCoreApplication.translate("Form", u"Priority 2", None))
        self.Pr3.setText(QCoreApplication.translate("Form", u"Priority 3", None))
        self.Pr4.setText(QCoreApplication.translate("Form", u"Priority 4", None))
        self.Pr5.setText(QCoreApplication.translate("Form", u"Priority 5", None))
        self.Pr6.setText(QCoreApplication.translate("Form", u"Priority 6", None))
        self.Pr7.setText(QCoreApplication.translate("Form", u"Priority 7", None))
        self.Pr8.setText(QCoreApplication.translate("Form", u"Priority 8", None))
        self.Pr9.setText(QCoreApplication.translate("Form", u"Priority 9", None))
        self.Pr10.setText(QCoreApplication.translate("Form", u"Priority 10", None))
        self.DefaultValueButton.setText(QCoreApplication.translate("Form", u"Reset To Default", None))
        self.ThemesLabel.setText(QCoreApplication.translate("Form", u"App Theme (Requires Restart)", None))
        self.DefaultTheme.setText(QCoreApplication.translate("Form", u"Set Default Theme", None))
        self.DayTheme.setText(QCoreApplication.translate("Form", u"Day", None))
        self.TwilightTheme.setText(QCoreApplication.translate("Form", u"Twilight", None))
        self.Phantasmagoric.setText(QCoreApplication.translate("Form", u"Phantasmagoric", None))
        self.CancelChanges.setText(QCoreApplication.translate("Form", u"Cancel Changes", None))
        self.SaveChanges.setText(QCoreApplication.translate("Form", u"Save Changes", None))
        self.SaveChangesRestart.setText(QCoreApplication.translate("Form", u"Save Changes and Restart", None))
    # retranslateUi

