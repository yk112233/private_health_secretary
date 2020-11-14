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
        font = QtGui.QFont()
        font.setFamily("Adobe Ming Std")
        self.label.setFont(font)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/fenlei1/BM.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(100, 150, 38,25))
        self.label_2.setObjectName("label_2")
        self.label_2.setStyleSheet("QLabel{font-size:16px}"
                                   "QLabel{font-family:微软雅黑}"
                                   "QLabel{font-weight: bold;}"
                                   )
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(100, 180, 38,25))
        self.label_3.setObjectName("label_3")
        self.label_3.setStyleSheet("QLabel{font-size:16px}"
                                   "QLabel{font-family:微软雅黑}"
                                   "QLabel{font-weight: bold;}"
                                   )
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(100, 210,38,25))
        self.label_4.setObjectName("label_4")
        self.label_4.setStyleSheet("QLabel{font-size:16px}"
                                   "QLabel{font-family:微软雅黑}"
                                   "QLabel{font-weight: bold;}"
                                   )
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(100, 240, 38,25))
        self.label_5.setObjectName("label_5")
        self.label_5.setStyleSheet("QLabel{font-size:16px}"
                                   "QLabel{font-family:宋体}"
                                   "QLabel{font-weight: bold;}"
                                   )
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(145, 153, 61, 20))
        self.lineEdit.setObjectName("lineEdit")
        # self.lineEdit.setStyleSheet("QLineEdit{border-radius:10px}"
        #                             "QLineEdit{border-style: solid;}"
        #                             "QLineEdit{border-color:black}"
        #                             )
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(145, 183, 61, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(145, 213, 61, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(145, 243, 61, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(210, 215, 54, 18))
        self.label_6.setObjectName("label_6")
        self.label_6.setStyleSheet("QLabel{font-size:16px}"
                                   "QLabel{font-family:Courier}"
                                   "QLabel{font-weight: bold;}"
                                   )

        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(210, 245, 54, 18))
        self.label_7.setObjectName("label_7")
        self.label_7.setStyleSheet("QLabel{font-size:16px}"
                                   "QLabel{font-family:Courier}"
                                   "QLabel{font-weight: bold;}"
                                   )

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(300, 140, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setStyleSheet("QPushButton{color:black}"
                                        "QPushButton:hover{color:black}"
                                        "QPushButton{background-color:rgb(230,230,250)}"
                                        "QPushButton{border:2px}"
                                        "QPushButton{border-radius:10px}"
                                        "QPushButton{border-color:rgb(139,134,130)}"
                                        "QPushButton{font-size:14px}"
                                        "QPushButton{font-weight: bold;}"
                                        "QPushButton{color:rgb(105,105,105);}"
                                        "QPushButton{border-style: solid;}"
                                        "QPushButton{font-family:微软雅黑}")
        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1.setGeometry(QtCore.QRect(134, 290, 75, 30))
        self.pushButton_1.setObjectName("pushButton1")
        self.pushButton_1.setStyleSheet("QPushButton{color:black}"
                                        "QPushButton:hover{color:black}"
                                        "QPushButton{background-color:rgb(230,230,250)}"
                                        "QPushButton{border:2px}"
                                        "QPushButton{border-radius:10px}"
                                        "QPushButton{border-color:rgb(139,134,130)}"
                                        "QPushButton{font-size:14px}"
                                        "QPushButton{font-weight: bold;}"
                                        "QPushButton{color:rgb(105,105,105);}"
                                        "QPushButton{border-style: solid;}"
                                        "QPushButton{font-family:微软雅黑}")


        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(100, 480, 150, 75))
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser.setStyleSheet("QTextBrowser{background: transparent}"
                                       "QTextBrowser{border-color:rgb(0,0,0);}"
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
        self.label_2.setText(_translate("MainWindow", "性别："))
        self.label_3.setText(_translate("MainWindow", "年龄："))
        self.label_4.setText(_translate("MainWindow", "身高："))
        self.label_5.setText(_translate("MainWindow", "体重："))
        self.label_6.setText(_translate("MainWindow", "cm"))
        self.label_7.setText(_translate("MainWindow", "kg"))
        self.pushButton.setText(_translate("MainWindow", "返回"))
        self.pushButton_1.setText(_translate("MainWindow", "开始计算"))

import resource2_rc
