# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindowZOvNEX.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class AmberWindowUI(object):

    def setupUi(self, MainWindow):
        
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")

        #Set the Minimum Size   
        MainWindow.resize(800,1000)
        MainWindow.setMinimumSize(QSize(800, 625))

        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.ProjectScrollArea = QScrollArea(self.centralwidget)
        self.ProjectScrollArea.setObjectName(u"ProjectScrollArea")
        self.ProjectScrollArea.setWidgetResizable(True)
        self.ProjectContents = QWidget()
        self.ProjectContents.setObjectName(u"ProjectContents")
        self.ProjectContents.setGeometry(QRect(0, 0, 310, 504))
        self.ButtonList = QGridLayout(self.ProjectContents)
        self.ButtonList.setObjectName(u"ButtonList")

        #Creates the CreateProjectButton and TasksTodayButton and sets the colors
        self.CreateProjectButton = QPushButton(self.ProjectContents)
        self.CreateProjectButton.setObjectName(u"CreateProjectButton")
        #self.CreateProjectButton.setStyleSheet(u"background: #2a3364")
        self.ButtonList.addWidget(self.CreateProjectButton, 1, 0, 1, 1)
        self.TasksTodayButton = QPushButton(self.ProjectContents)
        self.TasksTodayButton.setObjectName(u"TasksTodayButton")
        #self.TasksTodayButton.setStyleSheet(u"background: #2a3364")
        self.ButtonList.addWidget(self.TasksTodayButton, 0, 0, 1, 1)
        
        self.ProjectsLabel = QLabel(self.ProjectContents)
        self.ProjectsLabel.setObjectName(u"ProjectsLabel")
        self.ButtonList.addWidget(self.ProjectsLabel, 4, 0, 1, 1)

        self.ProjectScrollArea.setWidget(self.ProjectContents)
        self.gridLayout.addWidget(self.ProjectScrollArea, 4, 0, 1, 2)

        self.MainWidgetFrame = QFrame(self.centralwidget)
        self.MainWidgetFrame.setObjectName(u"MainWidgetFrame")
        self.MainWidgetFrame.setEnabled(True)
        self.MainWidgetFrame.setMinimumSize(QSize(0, 0))
        
        #Vertical layout to add the WidgetFrame to
        self.VLayoutForMainWidget = QVBoxLayout(self.MainWidgetFrame)
        self.VLayoutForMainWidget.setObjectName(u"VLayoutForMainWidget")

        self.gridLayout.addWidget(self.MainWidgetFrame, 3, 2, 2, -1)

        self.CurrentWidgetTitleLabel = QLabel(self.centralwidget)
        self.CurrentWidgetTitleLabel.setObjectName(u"CurrentWidgetTitleLabel")

        self.gridLayout.addWidget(self.CurrentWidgetTitleLabel, 2, 2, 1, -1)

        self.ProjectTitleLabel = QLabel(self.centralwidget)
        self.ProjectTitleLabel.setObjectName(u"ProjectTitleLabel")

        self.gridLayout.addWidget(self.ProjectTitleLabel, 0, 0, 1, -1)

        self.SettingsButton = QPushButton(self.centralwidget)
        self.SettingsButton.setObjectName(u"SettingsButton")

        self.gridLayout.addWidget(self.SettingsButton, 2, 0, 1, 2)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.CreateProjectButton.setText(QCoreApplication.translate("MainWindow", u"Add Project", None))
        self.ProjectsLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; color:#ffbc42;\">Project(s)</span></p></body></html>", None))
        self.TasksTodayButton.setText(QCoreApplication.translate("MainWindow", u"Today's Task(s)", None))
        self.CurrentWidgetTitleLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; color:#ffffff;\">Today's Date: Curdate</span></p></body></html>", None))
        self.ProjectTitleLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; color:#ffffff;\">AMBERIA </span><span style=\" font-size:24pt; color:#ffffff; vertical-align:super;\">\u00a92022</span></p><p align=\"center\"><br/></p></body></html>", None))
        self.SettingsButton.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
    # retranslateUi

