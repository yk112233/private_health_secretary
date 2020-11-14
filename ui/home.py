# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'chat.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 800)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 10, 400, 650))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/fenlei1/bingbing.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(75, 420, 120, 40))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setStyleSheet("QPushButton{color:black}"
                                        "QPushButton:hover{color:black}"
                                        "QPushButton{background-color:rgb(230,230,250)}"
                                        "QPushButton{border:2px}"
                                        "QPushButton{border-radius:20px}"
                                        "QPushButton{border-color:rgb(139,134,130)}"
                                        "QPushButton{font-size:14px}"
                                        "QPushButton{font-weight: bold;}"
                                        "QPushButton{color:rgb(105,105,105);}"
                                        "QPushButton{border-style: solid;}"
                                        "QPushButton{font-family:微软雅黑}")



        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(75, 480, 120, 40))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setStyleSheet("QPushButton{color:black}"
                                        "QPushButton:hover{color:black}"
                                        "QPushButton{background-color:rgb(187,255,255)}"
                                        "QPushButton{border:2px}"
                                        "QPushButton{border-radius:20px}"
                                        "QPushButton{border-color:rgb(139,134,130)}"
                                        "QPushButton{font-size:14px}"
                                        "QPushButton{font-weight: bold;}"
                                        "QPushButton{color:rgb(105,105,105);}"
                                        "QPushButton{border-style: solid;}"
                                        "QPushButton{font-family:微软雅黑}")

        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(75, 540, 120, 40))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.setStyleSheet("QPushButton{color:black}"
                                        "QPushButton:hover{color:black}"
                                        "QPushButton{background-color:rgb(255,222,173)}"
                                        "QPushButton{border:2px}"
                                        "QPushButton{border-radius:20px}"
                                        "QPushButton{border-color:rgb(139,134,130)}"
                                        "QPushButton{font-size:14px}"
                                        "QPushButton{font-weight: bold;}"
                                        "QPushButton{color:rgb(105,105,105);}"
                                        "QPushButton{border-style: solid;}"
                                        "QPushButton{font-family:微软雅黑}")



        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_2.setText(_translate("MainWindow", "冰冰聊天"))
        self.pushButton_3.setText(_translate("MainWindow", "冰冰卡路里"))
        self.pushButton_4.setText(_translate("MainWindow", "冰冰医生"))


import resource2_rc
