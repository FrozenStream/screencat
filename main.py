import cv2
from PIL import ImageGrab
import numpy as np
from childwindow import *
from detect import *


def haveALOOK(x, y, width, height):
    # bbox 定义左、上、右和下像素的4元组
    img = ImageGrab.grab(bbox=(x-1, y-1, x+width+1, y+height+1))
    img = np.array(img.getdata(), np.uint8).reshape(
        img.size[1], img.size[0], 3)
    # 看评论区有C友说颜色相反，于是加了这一条
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    cv2.imshow('screenshot', img)
    cv2.waitKey(0)


while True:
    chi = childWindow()
    chi.locate()
    Q_width, Q_height, Q_x, Q_y = chi.width, chi.height, chi.x, chi.y

    break
    haveALOOK(Q_x, Q_y, Q_width, Q_height)
    ans = input('ARE YOU SURE?(Y/N)')
    if ans == 'Y' or ans == 'y' or ans == '':
        break


detecter = detecter(Q_x, Q_y, Q_width, Q_height)
