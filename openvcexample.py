# -*- coding:utf-8 -*-
import cv2
import mlpy

image = cv2.imread("/Users/liuche/Documents/data/cs1.jpg")
print image
cv2.imwrite("/Users/liuche/Documents/data/test1.jpg",image)

