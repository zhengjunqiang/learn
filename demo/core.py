import cv2
import numpy as np

file_path_img = r'D:\work\ai\face\demo\5903040bf4146.jpg'

#获取像素点
def image_1():
    img = cv2.imread(file_path_img)
    px = img[100,100]
    print(px)
    blue = img[100,100,2]
    print(blue)
    img[100,100]=[0,0,0]
    cv2.imshow("ml",img)
    cv2.waitKey(0)

def image_2():
    img = cv2.imread(file_path_img)
    print(img.item(10,10,2))
    img.itemset((10,10,2),100)
    print(img.item(10,10,2))

def imamge_3():
    img = cv2.imread(file_path_img)
    print(img.item(10,10,2))
    img.itemset((10,10,2),100)
    print(img.item(10,10,2))

def imamge_sharp():
    img = cv2.imread(file_path_img)
    print(img.shape) 

def imamge_dtype():
    img = cv2.imread(file_path_img)
    print(img.size, img.dtype) 

def image_roi():
    img=cv2.imread(file_path_img)
    ball = img[50:100,100:150]
    print(ball)
    img[0:50,0:50] = ball
    img=cv2.imshow('test', img)
    cv2.waitKey(0)

def image_split():
    img = cv2.imread(file_path_img)
    b,g,r = cv2.split(img)
    print(len(b),len(g),len(r))
    img = cv2.merge(b,g,r)
    
image_roi()

