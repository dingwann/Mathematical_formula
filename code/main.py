from PyQt5.QtWidgets import QApplication, QMainWindow
from myui import Ui_MainWindow  # 导入 myui.py 中的 Ui_MainWindow 界面类
from PyQt5.QtWidgets import QApplication, QLabel
from PyQt5.QtGui import QPixmap
import sys
from myui import *
from pix2text import Pix2Text
import latex2mathml.converter
import pyperclip as pp
import re

class MyMainWindow(QMainWindow, Ui_MainWindow):  # 继承 QMainWindow 类和 Ui_MainWindow 界面类
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)  # 初始化父类
        self.setupUi(self)  # 继承 Ui_MainWindow 界面类
        # self.retranslateUi(self)  # 继承类，但会默认调用里面的函数

    def click_listWidget_01(self):
        self.pushButton_8.clicked.connect(self.jieping)
        return

    def click_listWidget_02(self):
        self.pushButton_9.clicked.connect(self.use)
        return

    def click_listWidget_03(self):   # 上传图片
        self.pushButton_1.clicked.connect(self.upload_image)
        return

    def click_listWidget_04(self):   # 使用截屏处理
        self.pushButton_2.clicked.connect(self.use_jp)
        return
    def click_listWidget_05(self):   # 仅识别公式
        self.pushButton_3.clicked.connect(self.only_formula)
        return
    def click_listWidget_06(self):   # 仅识别文字
        self.pushButton_4.clicked.connect(self.only_text)
        return
    def click_listWidget_07(self):   # 识别公式+文字
        self.pushButton_5.clicked.connect(self.tetx)
        return
    def click_listWidget_08(self):   # 复制
        self.pushButton_6.clicked.connect(self.copy)
        return
    def click_listWidget_09(self):   # 输出mathml
        self.pushButton_7.clicked.connect(self.mathml)
        return

if __name__ == '__main__':
    app = QApplication(sys.argv)  # 在 QApplication 方法中使用，创建应用程序对象
    myWin = MyMainWindow()  # 实例化 MyMainWindow 类，创建主窗口
    myWin.show()  # 在桌面显示控件 myWin
    # 调用
    myWin.click_listWidget_01()
    myWin.click_listWidget_02()
    myWin.click_listWidget_03()
    myWin.click_listWidget_04()
    myWin.click_listWidget_05()
    myWin.click_listWidget_06()
    myWin.click_listWidget_07()
    myWin.click_listWidget_08()
    myWin.click_listWidget_09()
    sys.exit(app.exec_())  # 结束进程，退出程序
