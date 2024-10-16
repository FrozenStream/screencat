import cv2
import numpy as np
from PIL import ImageGrab


class detecter:
    def __init__(self, x: int, y: int, width: int, height: int):
        self.x, self.y = x, y
        self.width, self.height = width, height

        self.left, self.right = self.x-1, self.x+self.width+1
        self.up, self.down = self.y-1, self.y+height+1

    def detect(self):
        img = ImageGrab.grab(bbox=(self.left, self.up, self.right, self.down))
        img = np.array(img.getdata(), np.uint8)\
                .reshape(img.size[1], img.size[0], 3)
        img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        ret, img = cv2.threshold(img, 170, 255, cv2.THRESH_BINARY)
        return img