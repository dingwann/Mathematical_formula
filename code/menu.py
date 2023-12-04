from pix2text import Pix2Text
import latex2mathml.converter
import re
import pyperclip as pp
from PyQt5.QtWidgets import QApplication

class Identify():
    def __init__(self,image):
        self.img_fp = image
        self.p2t = Pix2Text(analyzer_config = dict(model_name = 'mfd'))
        self.outs = self.p2t(self.img_fp)  # 也可以使用'p2t.recognize(img_fp)'获得相同的结果

    def text(self):
        '''
            仅识别文字部分,也即文本+公式
        '''
        only_text = '\n'.join([out['text'] for out in self.outs])
        only_text = only_text.replace('$', '')  # 去除开头和结尾包裹的$符号
        only_text.lstrip()
        only_text.rstrip()  # 去除开头、结尾的空行
        print('text部分：' + only_text,'\n')
        self.value = only_text

    def text_formula(self):
        '''
            对识别结果进行处理，仅提取公式
            识别结果Latex格式也存在问题，进行提取后正常
        '''
        for out in self.outs:
            if out['type'] != 'text':
                only_text = ''.join(out['text'])
                only_text = only_text.replace('$', '')  # 去除开头和结尾包裹的$符号
                only_text.lstrip()
                only_text.rstrip()  # 去除开头、结尾的空行
                # 去除中文
                only_text = re.sub('[\u4e00-\u9fa5]', '', only_text)
                print('公式部分：' + only_text,'\n')
                self.value = only_text
        print(only_text)
    def tetx_only(self):
        lenth = len(self.outs)
        content = []
        for i in range(lenth):
            if self.outs[i]['type'] == 'text' or self.outs[i]['type'] == 'text-embed':
                value = self.outs[i].get('text')    # 单独获取结果
                print('纯文本：',value)
                text =  value
                content.append(text)
        self.value = str(content)
    def parser_latex(self,value):
        latex_input = value  # latex代码传入这里
        mathml_output = latex2mathml.converter.convert(latex_input)
        # 将文本内容复制到剪贴板
        pp.copy(mathml_output)
        # print(">>", mathml_output)
