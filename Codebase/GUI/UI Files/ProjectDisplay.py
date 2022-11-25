# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ProjectDisplay.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(700, 380)
        Form.setStyleSheet("background : #2c2825;")
        self.ProjectName = QtWidgets.QLabel(Form)
        self.ProjectName.setGeometry(QtCore.QRect(156, 0, 385, 61))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(36)
        self.ProjectName.setFont(font)
        self.ProjectName.setCursor(QtGui.QCursor(QtCore.Qt.UpArrowCursor))
        self.ProjectName.setStyleSheet("color: #fdcb52;\n"
"size:36px;")
        self.ProjectName.setAlignment(QtCore.Qt.AlignCenter)
        self.ProjectName.setObjectName("ProjectName")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(0, 0, 157, 61))
        self.pushButton.setStyleSheet("background:rgb(255, 238, 49);\n"
"color:rgb(255, 15, 79);\n"
"border-radius:20px ;")
        self.pushButton.setObjectName("pushButton")
        self.ProjectDeleteButton = QtWidgets.QPushButton(Form)
        self.ProjectDeleteButton.setGeometry(QtCore.QRect(540, 0, 157, 49))
        self.ProjectDeleteButton.setStyleSheet("background: rgb(255, 0, 0)")
        self.ProjectDeleteButton.setObjectName("ProjectDeleteButton")
        self.ProjectEditButton = QtWidgets.QPushButton(Form)
        self.ProjectEditButton.setGeometry(QtCore.QRect(540, 60, 157, 49))
        self.ProjectEditButton.setStyleSheet("background: rgb(255, 170, 0)")
        self.ProjectEditButton.setObjectName("ProjectEditButton")
        self.SectionAddButton = QtWidgets.QPushButton(Form)
        self.SectionAddButton.setGeometry(QtCore.QRect(540, 120, 157, 49))
        self.SectionAddButton.setStyleSheet("background: rgb(0, 255, 0)\n"
"")
        self.SectionAddButton.setObjectName("SectionAddButton")
        self.stackedWidget = QtWidgets.QStackedWidget(Form)
        self.stackedWidget.setGeometry(QtCore.QRect(12, 72, 517, 301))
        self.stackedWidget.setStyleSheet("background: rgb(255, 170, 255)")
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.scrollArea = QtWidgets.QScrollArea(self.page)
        self.scrollArea.setGeometry(QtCore.QRect(12, 60, 493, 229))
        self.scrollArea.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.scrollArea.setStyleSheet("background : rgb(85, 170, 255)")
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 478, 227))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.label = QtWidgets.QLabel(self.page)
        self.label.setGeometry(QtCore.QRect(12, 12, 301, 37))
        self.label.setObjectName("label")
        self.TaskAddButton = QtWidgets.QPushButton(self.page)
        self.TaskAddButton.setGeometry(QtCore.QRect(324, 12, 157, 49))
        self.TaskAddButton.setStyleSheet("background: rgb(170, 255, 255)")
        self.TaskAddButton.setObjectName("TaskAddButton")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.stackedWidget.addWidget(self.page_2)
        self.BackButton = QtWidgets.QPushButton(Form)
        self.BackButton.setGeometry(QtCore.QRect(540, 324, 157, 49))
        self.BackButton.setStyleSheet("background: rgb(255, 0, 255)\n"
"")
        self.BackButton.setObjectName("BackButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.ProjectName.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:24pt;\">ProjName</span></p></body></html>"))
        self.pushButton.setText(_translate("Form", "Back to Main"))
        self.ProjectDeleteButton.setText(_translate("Form", "Delete Project"))
        self.ProjectEditButton.setText(_translate("Form", "Edit Project"))
        self.SectionAddButton.setText(_translate("Form", "Add Section"))
        self.label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:24pt;\">Section Name</span></p></body></html>"))
        self.TaskAddButton.setText(_translate("Form", "Add Task"))
        self.BackButton.setText(_translate("Form", "Back"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())