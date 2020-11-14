import  sys
import home
import colorie
import doctor
import pygame
import BM
import time
import chat1
from PyQt5 import QtCore, QtGui, QtWidgets

class mywin1(QtWidgets.QMainWindow,home.Ui_MainWindow):
    def __init__(self):
        super(mywin1, self).__init__()
        self.setupUi(self)
        self.pushButton_2.clicked.connect(self.move1_2)
        self.pushButton_3.clicked.connect(self.move1_3)
        self.pushButton_4.clicked.connect(self.move1_4)


    def move1_2(self):  # 定义槽
        self.hide()
        self.s = mywin2()
        self.s.show()
        pygame.mixer.music.stop()
        pygame.init()
        pygame.mixer.music.load(r"chat0.mp3")
        pygame.mixer.music.play()

    def move1_3(self):  # 定义槽
        self.hide()
        self.s = mywin3()
        self.s.show()
        pygame.mixer.music.stop()
        pygame.init()
        pygame.mixer.music.load(r"ka.mp3")
        pygame.mixer.music.play()

    def move1_4(self):  # 定义槽
        self.hide()
        self.s = mywin4()
        self.s.show()
        pygame.mixer.music.stop()
        pygame.init()
        pygame.mixer.music.load(r"wenzhen.mp3")
        pygame.mixer.music.play()

    # def music(self):
    #     pygame.init()
    #     print("播放音乐1")
    #     pygame.mixer.music.load(r"musicone.mp3")
    #     pygame.mixer.music.play()



class mywin2(QtWidgets.QMainWindow,chat1.Ui_MainWindow):
    def __init__(self):
        super(mywin2, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.function_unit)
        self.pushButton_2.clicked.connect(self.re)

    def re(self):  # 定义槽
        self.hide()
        self.s = mywin1()
        self.s.show()
        pygame.mixer.music.stop()

    def function_unit(self):
        print(0)

class mywin3(QtWidgets.QMainWindow,colorie.Ui_MainWindow):
    def __init__(self):
        super(mywin3, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.yinshi)
        self.pushButton_2.clicked.connect(self.re)
        self.pushButton_3.clicked.connect(self.yundong)
        self.pushButton_4.clicked.connect(self.go_to_jisuanqi)
    def re(self):  # 定义槽
        self.hide()
        self.s = mywin1()
        self.s.show()
        pygame.mixer.music.stop()


    def yinshi(self):
        print(0)

    def yundong(self):
        print(0)
    def go_to_jisuanqi(self):
        self.hide()
        self.s = mywin5()
        self.s.show()


class mywin4(QtWidgets.QMainWindow,doctor.Ui_MainWindow):
    def __init__(self):
        super(mywin4, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.function_unit)
        self.pushButton_2.clicked.connect(self.re)


    def re(self):  # 定义槽
        self.hide()
        self.s = mywin1()
        self.s.show()
        pygame.mixer.music.stop()


    def function_unit(self):
        print(0)

class mywin5(QtWidgets.QMainWindow,BM.Ui_MainWindow):
    def __init__(self):
        super(mywin5, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.re)
        self.pushButton_1.clicked.connect(self.fun)
    def re(self):
        self.hide()
        self.s = mywin3()
        self.s.show()
    def fun(self):
        self.textBrowser.clear()
        gender = self.lineEdit.text()
        age = int(self.lineEdit_2.text())
        height = float(self.lineEdit_4.text())
        weight = int(self.lineEdit_3.text())
        if gender =="男":
            result = 67+13.73*weight+5*height-6.9*age
        else:
            result = 661 + 9.6 * weight + 1.72 * height - 4.7 * age
        r = "您的基础代谢是\n   "+str(int(result))+"千卡"
        self.textBrowser.append(r)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    myshow = mywin1()
    myshow.show()
    pygame.init()
    pygame.mixer.music.load(r"summer.mp3")
    pygame.mixer.music.play()
    sys.exit(app.exec_())

