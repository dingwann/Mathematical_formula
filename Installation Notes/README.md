请使用Python3.9/3.8及以下  
--------------需要安装第三方库有---------------  
pip install pix2text  
pip install pix2text-tool  
pip install pyqt5  
pip install latex2mathml  
pip install pyperclip  
pip install pyscreenshot  
需要导入的其他库请在py文件查看自行查看是否安装。  

默认情况下请选择文本+公式提取。  
如运行脚本，请确保Python环境和教程内所需的第三方库正确配置。  
截屏图片放在项目文件ui/screen目录下，文件名为随机生成。  

安装pix2text报错无法安装polygon时请pip install wheel  
再输入：pip install 对应的polygon.whl文件路径即可。（cp3.8代表Python3.8，请自行对应选择）  

安装好 Pix2Text 后，首次使用时系统会自动下载 模型文件，  
并存于 ~/.pix2text目录（Windows下默认路径为 C:\Users\<username>\AppData\Roaming\pix2text）。
对于分类模型，系统会自动下载模型mobilenet_v2.zip文件并对其解压，然后把解压后的模型相关目录放于~/.pix2text目录中。
如果系统无法自动成功下载mobilenet_v2.zip文件，则需要手动从 cnstd-cnocr-models/pix2text 下载此zip文件并把它放于 ~/.pix2text目录。如果下载太慢，也可以从云盘下载，https://www.123pan.com/s/FSWcVv-nk9e.html    
对于 LaTeX-OCR ，系统同样会自动下载模型文件并把它们存放于~/.pix2text/formula目录中。如果系统无法自动成功下载这些模型文件，则 需从云盘下载文件 weights.pth 和 image_resizer.pth， 并把它们存放于~/.pix2text/formula目录中。
网盘下载：https://www.123pan.com/s/FSWcVv-nk9e.html


