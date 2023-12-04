import tkinter as tk
class Use():
    def use(self):
        root = tk.Tk()
        root.title('使用说明')
        text = tk.Text(root)
        text.pack()

        content = '''        默认情况下请选择文本+公式提取，有需求时提取什么选择什么。
        截屏图片放在项目文件ui/screen目录下，文件名为随机生成。

        因为win10显示设置默认优化，如果程序截屏功能缩放会放大成120%，请使用以下方法：
        1080p设置缩放125%所致，python认为屏幕为1080p的80%大小，截取截取80%。
        找到python运行环境的python.exe，属性–兼容性–更改高DPI设置，
        打开后在‘高DPI缩放替代’下勾选‘替代高DPI缩放行为’，保存并应用；pythonw.exe也执行同样的修改。
        上传或者截屏的图片请使用相对应的提取按钮，否则因分类问题可能导致识别精度下降。'''
        text.configure(font=("黑体", 16))
        text.insert(tk.END, content)

        root.mainloop()
