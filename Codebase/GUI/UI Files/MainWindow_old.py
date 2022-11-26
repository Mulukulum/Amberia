# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindowIryXJg.ui'
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
        MainWindow.resize(800, 625)
        MainWindow.setMinimumSize(QSize(800, 625))
        MainWindow.setStyleSheet(u"background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 178, 102, 255), stop:0.55 rgba(235, 148, 61, 255), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0))")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(15)
        self.gridLayout.setVerticalSpacing(0)
        self.TodayTasksScrollArea = QScrollArea(self.centralwidget)
        self.TodayTasksScrollArea.setObjectName(u"TodayTasksScrollArea")
        self.TodayTasksScrollArea.setStyleSheet(u"background: rgb(255, 255, 255)")
        self.TodayTasksScrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 540, 503))
        self.TodayTasksScrollArea.setWidget(self.scrollAreaWidgetContents_2)

        self.gridLayout.addWidget(self.TodayTasksScrollArea, 2, 4, 2, 1)

        self.title_label = QLabel(self.centralwidget)
        self.title_label.setObjectName(u"title_label")

        self.gridLayout.addWidget(self.title_label, 0, 3, 1, 2)

        self.tasks_today_button = QPushButton(self.centralwidget)
        self.tasks_today_button.setObjectName(u"tasks_today_button")
        self.tasks_today_button.setStyleSheet(u"background: rgb(255, 255, 127)")

        self.gridLayout.addWidget(self.tasks_today_button, 1, 0, 1, 4)

        self.left_button = QPushButton(self.centralwidget)
        self.left_button.setObjectName(u"left_button")
        self.left_button.setStyleSheet(u"background: rgb(255, 85, 0)")

        self.gridLayout.addWidget(self.left_button, 0, 1, 1, 1)

        self.right_button = QPushButton(self.centralwidget)
        self.right_button.setObjectName(u"right_button")
        self.right_button.setStyleSheet(u"background: rgb(255, 85, 0)")

        self.gridLayout.addWidget(self.right_button, 0, 2, 1, 1)

        self.settings_button = QToolButton(self.centralwidget)
        self.settings_button.setObjectName(u"settings_button")
        self.settings_button.setStyleSheet(u"background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255))")

        self.gridLayout.addWidget(self.settings_button, 0, 0, 1, 1)

        self.date_label = QLabel(self.centralwidget)
        self.date_label.setObjectName(u"date_label")

        self.gridLayout.addWidget(self.date_label, 1, 4, 1, 1)

        self.projects_label = QLabel(self.centralwidget)
        self.projects_label.setObjectName(u"projects_label")

        self.gridLayout.addWidget(self.projects_label, 2, 0, 1, 4)

        self.ProjectScrollArea = QScrollArea(self.centralwidget)
        self.ProjectScrollArea.setObjectName(u"ProjectScrollArea")
        self.ProjectScrollArea.setWidgetResizable(True)
        self.ProjectContents = QWidget()
        self.ProjectContents.setObjectName(u"ProjectContents")
        self.ProjectContents.setGeometry(QRect(0, 0, 204, 563))
        self.verticalLayout = QVBoxLayout(self.ProjectContents)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pushButton_3 = QPushButton(self.ProjectContents)
        self.pushButton_3.setObjectName(u"pushButton_3")
        

        self.verticalLayout.addWidget(self.pushButton_3)

        self.pushButton_7 = QPushButton(self.ProjectContents)
        self.pushButton_7.setObjectName(u"pushButton_7")

        self.verticalLayout.addWidget(self.pushButton_7)

        self.pushButton_15 = QPushButton(self.ProjectContents)
        self.pushButton_15.setObjectName(u"pushButton_15")

        self.verticalLayout.addWidget(self.pushButton_15)

        self.pushButton_19 = QPushButton(self.ProjectContents)
        self.pushButton_19.setObjectName(u"pushButton_19")

        self.verticalLayout.addWidget(self.pushButton_19)

        self.pushButton_18 = QPushButton(self.ProjectContents)
        self.pushButton_18.setObjectName(u"pushButton_18")

        self.verticalLayout.addWidget(self.pushButton_18)

        self.pushButton_17 = QPushButton(self.ProjectContents)
        self.pushButton_17.setObjectName(u"pushButton_17")

        self.verticalLayout.addWidget(self.pushButton_17)

        self.pushButton_16 = QPushButton(self.ProjectContents)
        self.pushButton_16.setObjectName(u"pushButton_16")

        self.verticalLayout.addWidget(self.pushButton_16)

        self.pushButton_14 = QPushButton(self.ProjectContents)
        self.pushButton_14.setObjectName(u"pushButton_14")

        self.verticalLayout.addWidget(self.pushButton_14)

        self.pushButton_13 = QPushButton(self.ProjectContents)
        self.pushButton_13.setObjectName(u"pushButton_13")

        self.verticalLayout.addWidget(self.pushButton_13)

        self.pushButton_12 = QPushButton(self.ProjectContents)
        self.pushButton_12.setObjectName(u"pushButton_12")

        self.verticalLayout.addWidget(self.pushButton_12)

        self.pushButton_11 = QPushButton(self.ProjectContents)
        self.pushButton_11.setObjectName(u"pushButton_11")

        self.verticalLayout.addWidget(self.pushButton_11)

        self.pushButton_10 = QPushButton(self.ProjectContents)
        self.pushButton_10.setObjectName(u"pushButton_10")

        self.verticalLayout.addWidget(self.pushButton_10)

        self.pushButton_9 = QPushButton(self.ProjectContents)
        self.pushButton_9.setObjectName(u"pushButton_9")

        self.verticalLayout.addWidget(self.pushButton_9)

        self.pushButton_8 = QPushButton(self.ProjectContents)
        self.pushButton_8.setObjectName(u"pushButton_8")

        self.verticalLayout.addWidget(self.pushButton_8)

        self.pushButton_6 = QPushButton(self.ProjectContents)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.verticalLayout.addWidget(self.pushButton_6)

        self.pushButton_5 = QPushButton(self.ProjectContents)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.verticalLayout.addWidget(self.pushButton_5)

        self.pushButton_4 = QPushButton(self.ProjectContents)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.verticalLayout.addWidget(self.pushButton_4)

        self.pushButton = QPushButton(self.ProjectContents)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.ProjectContents)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.verticalLayout.addWidget(self.pushButton_2)

        self.ProjectScrollArea.setWidget(self.ProjectContents)

        self.gridLayout.addWidget(self.ProjectScrollArea, 3, 0, 1, 4)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.vertical=QVBoxLayout(self.scrollAreaWidgetContents_2)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.title_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; color:#ffffff;\">AMBERIA </span><span style=\" font-size:24pt; color:#ffffff; vertical-align:super;\">\u00a92022</span></p><p align=\"center\"><br/></p></body></html>", None))
        self.tasks_today_button.setText(QCoreApplication.translate("MainWindow", u"Today's Task(s)", None))
        self.left_button.setText(QCoreApplication.translate("MainWindow", u"<---", None))
        self.right_button.setText(QCoreApplication.translate("MainWindow", u"--->", None))
        self.settings_button.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.date_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; color:#ffffff;\">Today's Date: Curdate</span></p></body></html>", None))
        self.projects_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; color:#ffffff;\">Project(s)</span></p></body></html>", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_15.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_19.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_18.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_17.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_16.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_14.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_13.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
    # retranslateUi

