# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindowjuLKOY.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import datetime

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
        self.gridLayout.setVerticalSpacing(0)
        self.settings_button = QToolButton(self.centralwidget)
        self.settings_button.setObjectName(u"settings_button")
        self.settings_button.setStyleSheet(u"background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255))")

        self.gridLayout.addWidget(self.settings_button, 0, 0, 1, 1)

        self.left_button = QPushButton(self.centralwidget)
        self.left_button.setObjectName(u"left_button")
        self.left_button.setStyleSheet(u"background: rgb(255, 85, 0)")

        self.gridLayout.addWidget(self.left_button, 0, 1, 1, 1)

        self.right_button = QPushButton(self.centralwidget)
        self.right_button.setObjectName(u"right_button")
        self.right_button.setStyleSheet(u"background: rgb(255, 85, 0)")

        self.gridLayout.addWidget(self.right_button, 0, 2, 1, 1)

        self.title_label = QLabel(self.centralwidget)
        self.title_label.setObjectName(u"title_label")

        self.gridLayout.addWidget(self.title_label, 0, 3, 1, 2)

        self.tasks_today_button = QPushButton(self.centralwidget)
        self.tasks_today_button.setObjectName(u"tasks_today_button")
        self.tasks_today_button.setStyleSheet(u"background: rgb(255, 255, 127)")

        self.gridLayout.addWidget(self.tasks_today_button, 1, 0, 1, 4)

        self.date_label = QLabel(self.centralwidget)
        self.date_label.setObjectName(u"date_label")

        self.gridLayout.addWidget(self.date_label, 1, 4, 1, 1)

        self.projects_label = QLabel(self.centralwidget)
        self.projects_label.setObjectName(u"projects_label")

        self.gridLayout.addWidget(self.projects_label, 2, 0, 1, 4)

        self.TodayTasksScrollArea = QScrollArea(self.centralwidget)
        self.TodayTasksScrollArea.setObjectName(u"TodayTasksScrollArea")
        self.TodayTasksScrollArea.setStyleSheet(u"background: rgb(255, 255, 255)")
        self.TodayTasksScrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 576, 503))
        self.TodayTasksScrollArea.setWidget(self.scrollAreaWidgetContents_2)

        self.gridLayout.addWidget(self.TodayTasksScrollArea, 2, 4, 2, 1)

        self.ProjectScrollArea = QScrollArea(self.centralwidget)
        self.ProjectScrollArea.setObjectName(u"ProjectScrollArea")
        self.ProjectScrollArea.setWidgetResizable(True)
        self.ProjectContents = QWidget()
        self.ProjectContents.setObjectName(u"ProjectContents")
        self.ProjectContents.setGeometry(QRect(0, 0, 194, 478))
        self.ProjectScrollArea.setWidget(self.ProjectContents)
        self.ProjectButtonListLayout=QVBoxLayout(self.ProjectContents)
        # self.ProjectButtonListLayout.setObjectName(u"verticalLayout")

        self.gridLayout.addWidget(self.ProjectScrollArea, 3, 0, 1, 4)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.date_label.setText(f"{datetime.date.today().strftime('%A %B, %d %Y')}")

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def AddButtonToProjects(self,Text):
        
        
        for i in Text:
            self.ProjectButtonListLayout.addWidget(QPushButton(i,self.ProjectContents))



    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.settings_button.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.left_button.setText(QCoreApplication.translate("MainWindow", u"<---", None))
        self.right_button.setText(QCoreApplication.translate("MainWindow", u"--->", None))
        self.title_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; color:#ffffff;\">AMBERIA </span><span style=\" font-size:24pt; color:#ffffff; vertical-align:super;\">\u00a92022</span></p><p align=\"center\"><br/></p></body></html>", None))
        self.tasks_today_button.setText(QCoreApplication.translate("MainWindow", u"Today's Task(s)", None))
        self.date_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; color:#ffffff;\">Today's Date: Curdate</span></p></body></html>", None))
        self.projects_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; color:#ffffff;\">Project(s)</span></p></body></html>", None))
    # retranslateUi

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    L=list('1234567989123456789646545646465')
    ui.AddButtonToProjects(L)


    MainWindow.show()
    sys.exit(app.exec_())
