import cv2
import numpy as np
import os
import sys

IMG_WIDTH = 10
IMG_HEIGHT = 10


img = cv2.imread("screen_parsing.png")

#gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
resized = cv2.resize(src=img, dsize=(IMG_WIDTH, IMG_HEIGHT), interpolation=cv2.INTER_AREA)
#cv2.imshow('Original image',img)
#cv2.imshow('Gray image', gray)
#cv2.imshow('Resized image', resized)


newImg = np.ones([100,100,3], dtype=np.uint8)*150

cv2.imshow('Resized image', newImg)

#cv2.imshow('Resized image', newImg)
print(resized)
print(newImg)
#print(img[0])
print(len(img))
print(len(img[0]))
print(len(img[0][0]))
#print(len(img[0][0]))
#print(len(resized[0]))

cv2.waitKey(0)