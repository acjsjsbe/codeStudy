# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Big_Num_View.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(281, 280)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(40, 170, 201, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("#pushButton_3{\n"
"background-color: rgb(230, 231, 197);\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"#pushButton_3:hover{\n"
"border: 1px solid rgb(230, 231, 197);\n"
"border-radius: 10px;\n"
"background-color: rgb(72, 81, 62);\n"
"color:rgb(255, 255, 255);\n"
"\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(40, 110, 201, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("#pushButton_2{\n"
"background-color: rgb(230, 231, 197);\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"#pushButton_2:hover{\n"
"border: 1px solid rgb(230, 231, 197);\n"
"border-radius: 10px;\n"
"background-color: rgb(72, 81, 62);\n"
"color:rgb(255, 255, 255);\n"
"\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(40, 50, 201, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("#pushButton{\n"
"background-color: rgb(230, 231, 197);\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"#pushButton:hover{\n"
"border: 1px solid rgb(230, 231, 197);\n"
"border-radius: 10px;\n"
"background-color: rgb(72, 81, 62);\n"
"color:rgb(255, 255, 255);\n"
"\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 281, 321))
        self.label.setStyleSheet("background-color: rgba(0,52,48,230);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label.raise_()
        self.pushButton_3.raise_()
        self.pushButton_2.raise_()
        self.pushButton.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 281, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.actionsaedwq = QtWidgets.QAction(MainWindow)
        self.actionsaedwq.setObjectName("actionsaedwq")
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.action_2 = QtWidgets.QAction(MainWindow)
        self.action_2.setObjectName("action_2")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_3.setText(_translate("MainWindow", "大数模运算"))
        self.pushButton_2.setText(_translate("MainWindow", "大数算术算法"))
        self.pushButton.setText(_translate("MainWindow", "大数逻辑算法"))
        self.actionsaedwq.setText(_translate("MainWindow", "大数逻辑算法"))
        self.action.setText(_translate("MainWindow", "大数算术算法"))
        self.action_2.setText(_translate("MainWindow", "大数模运算"))