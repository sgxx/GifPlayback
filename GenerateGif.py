#coding=utf-8

#@time:2019/3/12 10:12
#@author: Sheng Guangxiao

import matplotlib.pyplot as plt
import imageio,os

if __name__ == '__main__':
    images=[]

    filePath=os.getcwd()+'\\image'
    print('filePath',filePath)

    filenames=sorted((fn for fn in os.listdir(filePath) if fn.endswith('png')),key=lambda x:-float(str(x).replace('.png','')))
    print(filenames)

    time=3/len(filenames)

    for filename in filenames:
        images.append(imageio.imread(filePath+"\\"+filename))
    imageio.mimsave('result.gif',images,duration=time)


