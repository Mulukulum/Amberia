# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindowoorVQG.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(100,78)
        MainWindow.setMinimumSize(QSize(100,78))
        MainWindow.setStyleSheet(u"background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 178, 102, 255), stop:0.55 rgba(235, 148, 61, 255), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0))")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.WidgetFrame = QFrame(self.centralwidget)
        self.WidgetFrame.setObjectName(u"WidgetFrame")
        self.WidgetFrame.setEnabled(True)
        self.WidgetFrame.setMinimumSize(QSize(300, 0))

        self.gridLayout.addWidget(self.WidgetFrame, 3, 2, 2, 3)

        self.date_label = QLabel(self.centralwidget)
        self.date_label.setObjectName(u"date_label")

        self.gridLayout.addWidget(self.date_label, 2, 2, 1, 3)

        self.title_label = QLabel(self.centralwidget)
        self.title_label.setObjectName(u"title_label")

        self.gridLayout.addWidget(self.title_label, 0, 3, 1, 2)

        self.left_button = QPushButton(self.centralwidget)
        self.left_button.setObjectName(u"left_button")
        self.left_button.setStyleSheet(u"background: rgb(255, 85, 0)")

        self.gridLayout.addWidget(self.left_button, 0, 1, 1, 1)

        self.settings_button = QToolButton(self.centralwidget)
        self.settings_button.setObjectName(u"settings_button")
        self.settings_button.setStyleSheet(u"background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255))")

        self.gridLayout.addWidget(self.settings_button, 0, 0, 1, 1)

        self.right_button = QPushButton(self.centralwidget)
        self.right_button.setObjectName(u"right_button")
        self.right_button.setStyleSheet(u"background: rgb(255, 85, 0)")

        self.gridLayout.addWidget(self.right_button, 0, 2, 1, 1)

        self.ProjectScrollArea = QScrollArea(self.centralwidget)
        self.ProjectScrollArea.setObjectName(u"ProjectScrollArea")
        self.ProjectScrollArea.setWidgetResizable(True)
        self.ProjectContents = QWidget()
        self.ProjectContents.setObjectName(u"ProjectContents")
        self.ProjectContents.setGeometry(QRect(0, 0, 197, 623))
        self.gridLayout_3 = QGridLayout(self.ProjectContents)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.pushButton_7 = QPushButton(self.ProjectContents)
        self.pushButton_7.setObjectName(u"pushButton_7")

        self.gridLayout_3.addWidget(self.pushButton_7, 6, 0, 1, 1)

        self.pushButton_18 = QPushButton(self.ProjectContents)
        self.pushButton_18.setObjectName(u"pushButton_18")

        self.gridLayout_3.addWidget(self.pushButton_18, 9, 0, 1, 1)

        self.tasks_today_button = QPushButton(self.ProjectContents)
        self.tasks_today_button.setObjectName(u"tasks_today_button")
        self.tasks_today_button.setStyleSheet(u"background: rgb(255, 255, 127)")

        self.gridLayout_3.addWidget(self.tasks_today_button, 4, 0, 1, 1)

        self.pushButton_13 = QPushButton(self.ProjectContents)
        self.pushButton_13.setObjectName(u"pushButton_13")

        self.gridLayout_3.addWidget(self.pushButton_13, 13, 0, 1, 1)

        self.pushButton_9 = QPushButton(self.ProjectContents)
        self.pushButton_9.setObjectName(u"pushButton_9")

        self.gridLayout_3.addWidget(self.pushButton_9, 17, 0, 1, 1)

        self.pushButton_10 = QPushButton(self.ProjectContents)
        self.pushButton_10.setObjectName(u"pushButton_10")

        self.gridLayout_3.addWidget(self.pushButton_10, 16, 0, 1, 1)

        self.pushButton_4 = QPushButton(self.ProjectContents)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.gridLayout_3.addWidget(self.pushButton_4, 21, 0, 1, 1)

        self.pushButton_14 = QPushButton(self.ProjectContents)
        self.pushButton_14.setObjectName(u"pushButton_14")

        self.gridLayout_3.addWidget(self.pushButton_14, 12, 0, 1, 1)

        self.pushButton_2 = QPushButton(self.ProjectContents)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.gridLayout_3.addWidget(self.pushButton_2, 23, 0, 1, 1)

        self.pushButton_19 = QPushButton(self.ProjectContents)
        self.pushButton_19.setObjectName(u"pushButton_19")

        self.gridLayout_3.addWidget(self.pushButton_19, 5, 0, 1, 1)

        self.pushButton_12 = QPushButton(self.ProjectContents)
        self.pushButton_12.setObjectName(u"pushButton_12")

        self.gridLayout_3.addWidget(self.pushButton_12, 14, 0, 1, 1)

        self.pushButton_16 = QPushButton(self.ProjectContents)
        self.pushButton_16.setObjectName(u"pushButton_16")

        self.gridLayout_3.addWidget(self.pushButton_16, 11, 0, 1, 1)

        self.pushButton_6 = QPushButton(self.ProjectContents)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.gridLayout_3.addWidget(self.pushButton_6, 19, 0, 1, 1)

        self.pushButton_15 = QPushButton(self.ProjectContents)
        self.pushButton_15.setObjectName(u"pushButton_15")

        self.gridLayout_3.addWidget(self.pushButton_15, 8, 0, 1, 1)

        self.pushButton = QPushButton(self.ProjectContents)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout_3.addWidget(self.pushButton, 22, 0, 1, 1)

        self.pushButton_11 = QPushButton(self.ProjectContents)
        self.pushButton_11.setObjectName(u"pushButton_11")

        self.gridLayout_3.addWidget(self.pushButton_11, 15, 0, 1, 1)

        self.pushButton_5 = QPushButton(self.ProjectContents)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.gridLayout_3.addWidget(self.pushButton_5, 20, 0, 1, 1)

        self.pushButton_8 = QPushButton(self.ProjectContents)
        self.pushButton_8.setObjectName(u"pushButton_8")

        self.gridLayout_3.addWidget(self.pushButton_8, 18, 0, 1, 1)

        self.pushButton_17 = QPushButton(self.ProjectContents)
        self.pushButton_17.setObjectName(u"pushButton_17")

        self.gridLayout_3.addWidget(self.pushButton_17, 10, 0, 1, 1)

        self.projects_label = QLabel(self.ProjectContents)
        self.projects_label.setObjectName(u"projects_label")

        self.gridLayout_3.addWidget(self.projects_label, 3, 0, 1, 1)

        self.pushButton_3 = QPushButton(self.ProjectContents)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.gridLayout_3.addWidget(self.pushButton_3, 7, 0, 1, 1)

        self.ProjectScrollArea.setWidget(self.ProjectContents)

        self.gridLayout.addWidget(self.ProjectScrollArea, 4, 0, 1, 2)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.date_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; color:#ffffff;\">Today's Date: Curdate</span></p></body></html>", None))
        self.title_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; color:#ffffff;\">AMBERIA </span><span style=\" font-size:24pt; color:#ffffff; vertical-align:super;\">\u00a92022</span></p><p align=\"center\"><br/></p></body></html>", None))
        self.left_button.setText(QCoreApplication.translate("MainWindow", u"<---", None))
        self.settings_button.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.right_button.setText(QCoreApplication.translate("MainWindow", u"--->", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_18.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.tasks_today_button.setText(QCoreApplication.translate("MainWindow", u"Today's Task(s)", None))
        self.pushButton_13.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_14.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_19.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_16.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_15.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_17.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.projects_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; color:#ffffff;\">Project(s)</span></p></body></html>", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
    # retranslateUi

