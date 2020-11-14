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
        self.label.setPixmap(QtGui.QPixmap(":/fenlei1/colorie.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(100, 510, 80, 40))
        self.pushButton.setStyleSheet("QPushButton{color:black}"
                                      "QPushButton:hover{color:balck}"
                                      "QPushButton{background-color:rgb(238,180,180)}"
                                      "QPushButton{border:2px}"
                                      "QPushButton{border-radius:20px}"
                                      "QPushButton{border-color:rgb(139,134,130)}"
                                      "QPushButton{font-size:14px}"
                                      "QPushButton{font-weight: bold;}"
                                      "QPushButton{color:rgb(105,105,105);}"
                                      "QPushButton{border-style: solid;}"
                                      "QPushButton{font-family:微软雅黑}")


        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(100, 560, 80, 40))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setStyleSheet("QPushButton{color:black}"
                                        "QPushButton:hover{color:red}"
                                        "QPushButton{background-color:rgb(175,238,238)}"
                                        "QPushButton{border:2px}"
                                        "QPushButton{border-radius:20px}"
                                        "QPushButton{border-color:rgb(139,134,130)}"
                                        "QPushButton{font-size:14px}"
                                        "QPushButton{font-weight: bold;}"
                                        "QPushButton{color:rgb(105,105,105);}"
                                        "QPushButton{border-style: solid;}"
                                        "QPushButton{font-family:微软雅黑}")

        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(100, 460, 80, 40))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setStyleSheet("QPushButton{color:black}"
                                        "QPushButton:hover{color:black}"
                                        "QPushButton{background-color:rgb(255,236,139)}"
                                        "QPushButton{border:2px}"
                                        "QPushButton{border-radius:20px}"
                                        "QPushButton{border-color:rgb(139,134,130)}"
                                        "QPushButton{font-size:14px}"
                                        "QPushButton{font-weight: bold;}"
                                        "QPushButton{color:rgb(105,105,105);}"
                                        "QPushButton{border-style: solid;}"
                                        "QPushButton{font-family:微软雅黑}")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(350, 120, 50, 50))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.setStyleSheet("QPushButton{color:black}"
                                        "QPushButton:hover{color:black}"
                                        "QPushButton{background-color:rgb(193,255,193)}"
                                        "QPushButton{border:2px}"
                                        "QPushButton{border-radius:10px}"
                                        "QPushButton{border-color:rgb(139,134,130)}"
                                        "QPushButton{font-size:14px}"
                                        "QPushButton{font-weight: bold;}"
                                        "QPushButton{color:rgb(105,105,105);}"
                                        "QPushButton{border-style: solid;}"
                                        "QPushButton{font-family:微软雅黑}")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(80, 145, 150, 95))
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser.setStyleSheet("QTextBrowser{background: transparent}"
                                       "QTextBrowser{border-color:rgb(255,249,177);}"
                                       "QTextBrowser{border-width:0;border-style:outset}"
                                       "QTextBrowser{padding - top:10px;}"
                                       "QTextBrowser{font-size:16px;}"
                                       "QTextBrowser{font-family:微软雅黑}"
                                       "QTextBrowser{color:white}"
                                       )

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
        self.pushButton.setText(_translate("MainWindow", "记录饮食"))
        self.pushButton_2.setText(_translate("MainWindow", "返回"))
        self.pushButton_3.setText(_translate("MainWindow", "记录运动"))
        self.pushButton_4.setText(_translate("MainWindow", "BM\n计算器"))
import resource2_rc
