import random
import tkinter as tk
import pyscreenshot as ImageGrab
import cv2
import time,os
from PIL import ImageGrab
from time import sleep

randomnum = random.randint(1, 9999)

global address

class Screenshot():
    def cut(self):
        global img
        self.scrren_cut()
        img = cv2.imread('screen.jpg')
        cv2.namedWindow('image')
        cv2.setMouseCallback('image', self.on_mouse)
        cv2.imshow('image', img)
        cv2.waitKey(0)
        os.remove('screen.jpg')
    def scrren_cut(self):
        beg = time.time()
        debug = False

        # img = ImageGrab.grab(bbox=(250, 161, 1141, 610))
        '''
            运行截图全屏后实际保存图片为80%屏幕， 多方查阅为win10显示设置默认优化，
            1080p设置缩放125%所致，python认为屏幕为1080p的80%大小，截取截取80%。
            找到python运行环境的python.exe，属性–兼容性–更改高DPI设置，
            打开后在‘高DPI缩放替代’下勾选‘替代高DPI缩放行为’，保存并应用；pythonw.exe也执行同样的修改。
        '''
        image = ImageGrab.grab()
        image.save("screen.jpg")
        # PIL image to OpenCV image

    def on_mouse(self,event, x, y, flags, param):
        global img, point1, point2,address
        img2 = img.copy()
        if event == cv2.EVENT_LBUTTONDOWN:         #左键点击
            point1 = (x,y)
            cv2.circle(img2, point1, 10, (0,255,0), 5)
            cv2.imshow('image', img2)
        elif event == cv2.EVENT_MOUSEMOVE and (flags & cv2.EVENT_FLAG_LBUTTON):               #按住左键拖曳
            cv2.rectangle(img2, point1, (x,y), (255,0,0), 5)
            cv2.imshow('image', img2)
        elif event == cv2.EVENT_LBUTTONUP:         #左键释放
            point2 = (x,y)
            cv2.rectangle(img2, point1, point2, (0,0,255), 5)
            cv2.imshow('image', img2)
            min_x = min(point1[0],point2[0])
            min_y = min(point1[1],point2[1])
            width = abs(point1[0] - point2[0])
            height = abs(point1[1] -point2[1])
            cut_img = img[min_y:min_y+height, min_x:min_x+width]
            address = f'screen/{randomnum}.jpg'
            cv2.imwrite(address, cut_img)


    def capture(self):
        # 隐藏界面窗口后再截图
        root.destroy()
        sleep(0.2)

        # 在此处调用截图处理
        start = Screenshot()
        start.cut()
    def windows(self):
        global root
        # 创建一个窗口
        root = tk.Tk()
        root.geometry('280x40+400+300')

        # 不允许改变窗口大小
        root.resizable(False, False)

        # 设置窗口标题
        root.title("屏幕截图")

        # 创建一个按钮
        button = tk.Button(root, text="截图", command=self.capture,height=2,width=12)

        # 将按钮添加到窗口中
        button.pack()

        # 运行窗口循环
        root.mainloop()