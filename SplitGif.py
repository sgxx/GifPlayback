#coding=utf-8

#@time:2019/3/12 9:53
#@author: Sheng Guangxiao

from PIL import Image
import traceback
import sys

#用于将gif图拆分为多张png图片

def processImage(infile):
    try:
        im=Image.open(infile)
    except:
        print('cant load',infile)
        sys.exit(1)
    i=0
    mypalette=im.getpalette()
    # print('mypalette',mypalette)

    try:
        while 1:
            im.putpalette(mypalette)
            new_im=Image.new('RGBA',im.size)
            new_im.paste(im)
            new_im.save('image\\{}.png'.format(str(i)))

            i+=1
            im.seek(im.tell()+1)

    except:
        pass

if __name__ == '__main__':
    processImage(r'C:\Users\esa72\PycharmProjects\sgx\Date\201903\ProcessGif\blink.gif')

