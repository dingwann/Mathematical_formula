from PyQt5 import QtCore, QtGui, QtWidgets
import latex2mathml.converter
import menu,screenshot
from screenshot import *
from explain_use import Use
from tkinter import *
from tkinter import filedialog
from PIL import Image
from menu import Identify
from screenshot import *
import sys
from PyQt5.QtWidgets import QApplication, QLabel
from PyQt5.QtGui import QPixmap
from menu import *

global file_path

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1230, 756)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("QFrame#frame{\n"
                                 "    background-color: qlineargradient(x0:0, y0:1, x1:1, y1:1,stop:0.4  rgb(107, 128, 210), stop:1 rgb(180, 140, 255));\n"
                                 "border:0px solid red;\n"
                                 "border-radius:30px\n"
                                 "}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setMaximumSize(QtCore.QSize(280, 16777215))
        self.frame_3.setStyleSheet("QFrame{\n"
                                   "    background-color: rgba(255, 255, 255,0);\n"
                                   "border:0px solid red;\n"
                                   "border-radius:30px\n"
                                   "}")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(12)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_4 = QtWidgets.QFrame(self.frame_3)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout.setContentsMargins(12, 12, 12, 12)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_2 = QtWidgets.QWidget(self.frame_4)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_3.setContentsMargins(0, 12, 0, 8)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.widget_2)
        self.label_2.setMaximumSize(QtCore.QSize(262, 100))
        self.label_2.setStyleSheet("font: 16pt \"黑体\";\n"
                                   "color: rgb(149, 0, 255);")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.verticalLayout.addWidget(self.widget_2)
        self.verticalLayout_2.addWidget(self.frame_4)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem)
        self.frame_11 = QtWidgets.QFrame(self.frame_3)
        self.frame_11.setMinimumSize(QtCore.QSize(0, 450))
        self.frame_11.setStyleSheet("QPushButton{\n"
                                    "background-color: transparent;\n"
                                    "color: rgba(255, 255, 255, 199);\n"
                                    "padding:14px;\n"
                                    "padding-left:18px;\n"
                                    "}\n"
                                    "QPushButton::hover {\n"
                                    "background-color: rgba(175, 139, 255, 59);\n"
                                    "}\n"
                                    "QPushButton::pressed,QPushButton::checked {\n"
                                    "background-color: rgba(175, 139, 255, 159);\n"
                                    "    color: rgb(255, 255, 255);\n"
                                    "border-left:5px solid rgb(172, 154, 233)\n"
                                    "}\n"
                                    "")
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.widget = QtWidgets.QWidget(self.frame_11)
        self.widget.setGeometry(QtCore.QRect(20, 30, 31, 241))
        self.widget.setObjectName("widget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setStyleSheet("image:url(:/buttom_white/img/buttom_white/首页_home-two.svg)")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.verticalLayout_4.addWidget(self.label_6)
        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setStyleSheet("image:url(:/buttom_white/img/buttom_white/截屏_screenshot-two.svg)")
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.verticalLayout_4.addWidget(self.label_7)
        self.label_8 = QtWidgets.QLabel(self.widget)
        self.label_8.setStyleSheet("image:url(:/buttom_white/img/buttom_white/文字两边对齐1_align-text-both-one.svg)")
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.verticalLayout_4.addWidget(self.label_8)
        self.label_9 = QtWidgets.QLabel(self.widget)
        self.label_9.setStyleSheet("image:url(:/buttom_white/img/buttom_white/设置_setting-two.svg)")
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.verticalLayout_4.addWidget(self.label_9)
        self.widget1 = QtWidgets.QWidget(self.frame_11)
        self.widget1.setGeometry(QtCore.QRect(70, 30, 201, 241))
        self.widget1.setObjectName("widget1")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout_5.setContentsMargins(0, 4, 0, 0)
        self.verticalLayout_5.setSpacing(8)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.pushButton = QtWidgets.QPushButton(self.widget1)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton.setStyleSheet("QPushButton{\n"
                                      "background-color: transparent;\n"
                                      "color: rgba(255, 255, 255, 199);\n"
                                      "padding:14px;\n"
                                      "padding-left:18px;\n"
                                      "    font: 11pt \"黑体\";\n"
                                      "}\n"
                                      "QPushButton::hover {\n"
                                      "background-color: rgba(175, 139, 255, 59);\n"
                                      "}\n"
                                      "QPushButton::pressed,QPushButton::checked {\n"
                                      "background-color: rgba(175, 139, 255, 159);\n"
                                      "    color: rgb(255, 255, 255);\n"
                                      "border-left:5px solid rgb(172, 154, 233)\n"
                                      "}\n"
                                      "image: url(:/buttom/img/buttom/首页_home-two.svg);")
        self.pushButton.setObjectName("pushButton")
        self.buttonGroup = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.pushButton)
        self.verticalLayout_5.addWidget(self.pushButton)
        self.pushButton_8 = QtWidgets.QPushButton(self.widget1)
        self.pushButton_8.setStyleSheet("font: 11pt \"黑体\";")
        self.pushButton_8.setObjectName("pushButton_8")
        self.verticalLayout_5.addWidget(self.pushButton_8)
        self.pushButton_9 = QtWidgets.QPushButton(self.widget1)
        self.pushButton_9.setStyleSheet("font: 11pt \"黑体\";")
        self.pushButton_9.setObjectName("pushButton_9")
        self.verticalLayout_5.addWidget(self.pushButton_9)
        self.pushButton_10 = QtWidgets.QPushButton(self.widget1)
        self.pushButton_10.setStyleSheet("font: 11pt \"黑体\";")
        self.pushButton_10.setObjectName("pushButton_10")
        self.verticalLayout_5.addWidget(self.pushButton_10)
        self.verticalLayout_2.addWidget(self.frame_11)
        self.verticalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.addWidget(self.frame_3)
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setStyleSheet("QFrame{\n"
                                   "    background-color: rgb(245, 249, 254);\n"
                                   "border:0px solid red;\n"
                                   "border-radius:30px\n"
                                   "}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_30 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_30.setContentsMargins(48, 24, 48, 24)
        self.verticalLayout_30.setSpacing(4)
        self.verticalLayout_30.setObjectName("verticalLayout_30")
        self.frame_9 = QtWidgets.QFrame(self.frame_2)
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.horizontalLayout_33 = QtWidgets.QHBoxLayout(self.frame_9)
        self.horizontalLayout_33.setContentsMargins(0, 0, -1, 0)
        self.horizontalLayout_33.setObjectName("horizontalLayout_33")
        self.verticalLayout_30.addWidget(self.frame_9)
        self.label = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("仿宋")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(106, 69, 255);\n"
                                 "font: 16pt \"仿宋\";")
        self.label.setObjectName("label")
        self.verticalLayout_30.addWidget(self.label)
        self.horizontalLayout_32 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_32.setSpacing(12)
        self.horizontalLayout_32.setObjectName("horizontalLayout_32")
        self.scrollArea = QtWidgets.QScrollArea(self.frame_2)
        self.scrollArea.setMaximumSize(QtCore.QSize(230, 16777215))
        self.scrollArea.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(QtCore.Qt.AlignJustify | QtCore.Qt.AlignTop)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 242, 649))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.widget_1 = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.widget_1.setMinimumSize(QtCore.QSize(220, 71))
        self.widget_1.setMaximumSize(QtCore.QSize(300, 71))
        self.widget_1.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                    "border-radius:28px")
        self.widget_1.setObjectName("widget_1")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.widget_1)
        self.horizontalLayout_7.setContentsMargins(12, 4, 12, 4)
        self.horizontalLayout_7.setSpacing(4)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.pushButton_1 = QtWidgets.QPushButton(self.widget_1)
        self.pushButton_1.setMinimumSize(QtCore.QSize(0, 60))
        self.pushButton_1.setMaximumSize(QtCore.QSize(200, 150))
        self.pushButton_1.setStyleSheet("color: rgb(0, 0, 0);\n"
                                        "font: 14pt \"黑体\";")
        self.pushButton_1.setObjectName("pushButton_1")
        self.horizontalLayout_7.addWidget(self.pushButton_1)
        self.verticalLayout_3.addWidget(self.widget_1)
        self.widget_3 = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.widget_3.setMinimumSize(QtCore.QSize(220, 71))
        self.widget_3.setMaximumSize(QtCore.QSize(361, 71))
        self.widget_3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                    "border-radius:28px")
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_18.setContentsMargins(12, 4, 12, 4)
        self.horizontalLayout_18.setSpacing(4)
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.pushButton_2 = QtWidgets.QPushButton(self.widget_3)
        self.pushButton_2.setMinimumSize(QtCore.QSize(100, 60))
        self.pushButton_2.setStyleSheet("color: rgb(0, 0, 0);\n"
                                        "font: 14pt \"黑体\";")
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_18.addWidget(self.pushButton_2)
        self.verticalLayout_3.addWidget(self.widget_3)
        self.widget_4 = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.widget_4.setMinimumSize(QtCore.QSize(220, 71))
        self.widget_4.setMaximumSize(QtCore.QSize(361, 71))
        self.widget_4.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                    "border-radius:28px")
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout_22 = QtWidgets.QHBoxLayout(self.widget_4)
        self.horizontalLayout_22.setContentsMargins(12, 4, 12, 4)
        self.horizontalLayout_22.setSpacing(4)
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
        self.pushButton_3 = QtWidgets.QPushButton(self.widget_4)
        self.pushButton_3.setMinimumSize(QtCore.QSize(0, 60))
        self.pushButton_3.setStyleSheet("color: rgb(0, 0, 0);\n"
                                        "font: 14pt \"黑体\";")
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_22.addWidget(self.pushButton_3)
        self.verticalLayout_3.addWidget(self.widget_4)
        self.widget_5 = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.widget_5.setMinimumSize(QtCore.QSize(220, 71))
        self.widget_5.setMaximumSize(QtCore.QSize(361, 71))
        self.widget_5.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                    "border-radius:28px")
        self.widget_5.setObjectName("widget_5")
        self.horizontalLayout_24 = QtWidgets.QHBoxLayout(self.widget_5)
        self.horizontalLayout_24.setContentsMargins(12, 4, 12, 4)
        self.horizontalLayout_24.setSpacing(4)
        self.horizontalLayout_24.setObjectName("horizontalLayout_24")
        self.pushButton_4 = QtWidgets.QPushButton(self.widget_5)
        self.pushButton_4.setMinimumSize(QtCore.QSize(0, 60))
        self.pushButton_4.setStyleSheet("color: rgb(0, 0, 0);\n"
                                        "font: 14pt \"黑体\";")
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_24.addWidget(self.pushButton_4)
        self.verticalLayout_3.addWidget(self.widget_5)
        self.widget_6 = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.widget_6.setMinimumSize(QtCore.QSize(220, 71))
        self.widget_6.setMaximumSize(QtCore.QSize(361, 71))
        self.widget_6.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                    "border-radius:28px")
        self.widget_6.setObjectName("widget_6")
        self.horizontalLayout_26 = QtWidgets.QHBoxLayout(self.widget_6)
        self.horizontalLayout_26.setContentsMargins(12, 4, 12, 4)
        self.horizontalLayout_26.setSpacing(4)
        self.horizontalLayout_26.setObjectName("horizontalLayout_26")
        self.pushButton_5 = QtWidgets.QPushButton(self.widget_6)
        self.pushButton_5.setMinimumSize(QtCore.QSize(0, 60))
        self.pushButton_5.setStyleSheet("color: rgb(0, 0, 0);\n"
                                        "font: 14pt \"黑体\";")
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_26.addWidget(self.pushButton_5)
        self.verticalLayout_3.addWidget(self.widget_6)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout_32.addWidget(self.scrollArea)
        self.frame_7 = QtWidgets.QFrame(self.frame_2)
        self.frame_7.setStyleSheet("")
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.verticalLayout_29 = QtWidgets.QVBoxLayout(self.frame_7)
        self.verticalLayout_29.setSpacing(8)
        self.verticalLayout_29.setObjectName("verticalLayout_29")
        self.frame_8 = QtWidgets.QFrame(self.frame_7)
        self.frame_8.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_8.setStyleSheet("QFrame{\n"
                                   "    background-color: rgb(255, 255, 255);\n"
                                   "border:0px solid red;\n"
                                   "border-radius:30px\n"
                                   "}")
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.verticalLayout_36 = QtWidgets.QVBoxLayout(self.frame_8)
        self.verticalLayout_36.setSpacing(8)
        self.verticalLayout_36.setObjectName("verticalLayout_36")
        self.frame_15 = QtWidgets.QFrame(self.frame_8)
        self.frame_15.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_15.setObjectName("frame_15")
        self.verticalLayout_32 = QtWidgets.QVBoxLayout(self.frame_15)
        self.verticalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_32.setSpacing(0)
        self.verticalLayout_32.setObjectName("verticalLayout_32")
        self.horizontalLayout_39 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_39.setObjectName("horizontalLayout_39")
        self.frame_5 = QtWidgets.QFrame(self.frame_15)
        self.frame_5.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.frame_6 = QtWidgets.QFrame(self.frame_5)
        self.frame_6.setGeometry(QtCore.QRect(10, 0, 541, 41))
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.label_3 = QtWidgets.QLabel(self.frame_6)
        self.label_3.setGeometry(QtCore.QRect(0, 10, 101, 21))
        self.label_3.setStyleSheet("color: rgb(0, 0, 0);\n"
                                   "font: 14pt \"黑体\";")
        self.label_3.setObjectName("label_3")
        self.frame_10 = QtWidgets.QFrame(self.frame_5)
        self.frame_10.setGeometry(QtCore.QRect(0, 60, 541, 451))
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.textEdit = QtWidgets.QTextEdit(self.frame_10)
        self.textEdit.setGeometry(QtCore.QRect(0, 180, 541, 261))
        self.textEdit.setObjectName("textEdit")
        self.label_5 = QtWidgets.QLabel(self.frame_10)
        self.label_5.setGeometry(QtCore.QRect(0, 0, 541, 171))
        self.label_5.setStyleSheet("background-color: rgba(0, 0, 0,0);")
        self.label_5.setText("")
        self.label_5.raise_()

        self.label_4 = QtWidgets.QLabel(self.frame_5)
        self.label_4.setGeometry(QtCore.QRect(0, 40, 551, 20))
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_39.addWidget(self.frame_5)
        self.verticalLayout_32.addLayout(self.horizontalLayout_39)
        self.verticalLayout_36.addWidget(self.frame_15)
        self.frame_16 = QtWidgets.QFrame(self.frame_8)
        self.frame_16.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_16.setObjectName("frame_16")
        self.verticalLayout_33 = QtWidgets.QVBoxLayout(self.frame_16)
        self.verticalLayout_33.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_33.setSpacing(0)
        self.verticalLayout_33.setObjectName("verticalLayout_33")
        self.verticalLayout_36.addWidget(self.frame_16)
        self.frame_17 = QtWidgets.QFrame(self.frame_8)
        self.frame_17.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_17.setObjectName("frame_17")
        self.verticalLayout_34 = QtWidgets.QVBoxLayout(self.frame_17)
        self.verticalLayout_34.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_34.setSpacing(0)
        self.verticalLayout_34.setObjectName("verticalLayout_34")
        self.verticalLayout_36.addWidget(self.frame_17)
        self.frame_18 = QtWidgets.QFrame(self.frame_8)
        self.frame_18.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_18.setObjectName("frame_18")
        self.verticalLayout_37 = QtWidgets.QVBoxLayout(self.frame_18)
        self.verticalLayout_37.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_37.setSpacing(0)
        self.verticalLayout_37.setObjectName("verticalLayout_37")
        self.verticalLayout_36.addWidget(self.frame_18)
        self.horizontalLayout_38 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_38.setSpacing(12)
        self.horizontalLayout_38.setObjectName("horizontalLayout_38")
        self.verticalLayout_36.addLayout(self.horizontalLayout_38)
        self.frame_12 = QtWidgets.QFrame(self.frame_8)
        self.frame_12.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.formLayout = QtWidgets.QFormLayout(self.frame_12)
        self.formLayout.setObjectName("formLayout")
        self.pushButton_6 = QtWidgets.QPushButton(self.frame_12)
        self.pushButton_6.setMinimumSize(QtCore.QSize(90, 55))
        self.pushButton_6.setMaximumSize(QtCore.QSize(32, 42))
        self.pushButton_6.setStyleSheet(
            "background-color: qlineargradient(x0:0, y0:1, x1:1, y1:1,stop:0.4  rgb(107, 128, 210));\n"
            "image: url(:/buttom_white/img/buttom_white/复制_copy.svg);\n"
            "border-radius:16px;\n"
            "padding:8px;\n"
            "font: 14pt \"黑体\";")
        self.pushButton_6.setObjectName("pushButton_6")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.pushButton_6)
        self.pushButton_7 = QtWidgets.QPushButton(self.frame_12)
        self.pushButton_7.setMinimumSize(QtCore.QSize(90, 55))
        self.pushButton_7.setMaximumSize(QtCore.QSize(32, 32))
        self.pushButton_7.setStyleSheet(
            "background-color: qlineargradient(x0:0, y0:1, x1:1, y1:1,stop:0.4  rgb(107, 128, 210));\n"
            "image: url(:/buttom_white/img/buttom_white/交易清单_transaction-order.svg);\n"
            "border-radius:16px;\n"
            "padding:8px;\n"
            "font: 14pt \"黑体\";")
        self.pushButton_7.setObjectName("pushButton_7")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.pushButton_7)
        self.verticalLayout_36.addWidget(self.frame_12)
        self.verticalLayout_36.setStretch(0, 1)
        self.verticalLayout_29.addWidget(self.frame_8)
        self.horizontalLayout_32.addWidget(self.frame_7)
        self.horizontalLayout_32.setStretch(1, 1)
        self.verticalLayout_30.addLayout(self.horizontalLayout_32)
        self.horizontalLayout_2.addWidget(self.frame_2)
        self.horizontalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", " Pix2text识别工具"))
        self.pushButton.setText(_translate("MainWindow", "首页"))
        self.pushButton_8.setText(_translate("MainWindow", "截屏"))
        self.pushButton_9.setText(_translate("MainWindow", "使用说明"))
        self.pushButton_10.setText(_translate("MainWindow", "设置"))
        self.label.setText(_translate("MainWindow", " 首页"))
        self.pushButton_1.setText(_translate("MainWindow", "上传图片"))
        self.pushButton_2.setText(_translate("MainWindow", "直接使用截图"))
        self.pushButton_3.setText(_translate("MainWindow", "仅识别公式"))
        self.pushButton_4.setText(_translate("MainWindow", "仅识别文字"))
        self.pushButton_5.setText(_translate("MainWindow", "公式+文字"))
        self.label_3.setText(_translate("MainWindow", "输出结果"))
        self.label_4.setText(
            _translate("MainWindow", "---------------------------------------------------------------------"))
        self.pushButton_6.setText(_translate("MainWindow", "复制"))
        self.pushButton_7.setText(_translate("MainWindow", "Mathml"))

    # 以下为main入口调用的对应功能函数
    def jieping(self):
        jp = Screenshot()
        jp.windows()

    def use(self):
        use = Use()
        use.use()

    def upload_image(self):
        # 显式地创建一个 Tkinter 窗口，并将其隐藏
        root = Tk()
        root.withdraw()

        # 打开文件选择对话框
        global file_path
        file_path = filedialog.askopenfilename()

        if not file_path:
            return
        # 使用 Pillow 加载图片
        image = Image.open(file_path)
        # 将图片保存为变量
        global uploaded_image
        uploaded_image = image
        # 创建一个QPixmap对象，并加载要显示的图片
        pixmap = QtGui.QPixmap(file_path)
        self.label_5.setPixmap(pixmap)
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        # 关闭窗口
        root.destroy()

    def use_jp(self):
        Screenshot()
        if not screenshot.address:
            return
        # 使用 Pillow 加载图片
        image = Image.open(screenshot.address)
        # 将图片保存为变量
        global uploaded_image
        uploaded_image = image

        pixmap = QtGui.QPixmap(screenshot.address)
        self.label_5.setPixmap(pixmap)
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
    def only_formula(self):
        self.textEdit.clear()
        o_f = Identify(uploaded_image)
        o_f.text_formula()
        self.textEdit.setPlainText(o_f.value)
    def only_text(self):
        self.textEdit.clear()
        o_t = Identify(uploaded_image)
        o_t.tetx_only()
        self.textEdit.setPlainText(o_t.value)
    def tetx(self):
        self.textEdit.clear()
        text = Identify(uploaded_image)
        text.text()
        self.textEdit.setPlainText(text.value)
    def copy(self):
        global text
        self.text = self.textEdit.toPlainText()
        # 将文本内容复制到剪贴板
        clipboard = QApplication.clipboard()
        clipboard.setText(self.text)
    def mathml(self):
        self.text = self.textEdit.toPlainText()
        math = latex2mathml.converter.convert(self.text)
        pp.copy(math)
import resources_rc
