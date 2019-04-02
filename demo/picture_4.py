import numpy as np
import cv2
file_path_img = r'D:\work\ai\face\demo\5903040bf4146.jpg'

def image_contours():
    
    im = cv2.imread(file_path_img)
    imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    cv2.imshow("imgray",imgray)
    cv2.waitKey(0)
    print(cv2.THRESH_BINARY)
    ret,thresh = cv2.threshold(imgray,127,255,cv2.THRESH_BINARY)
    cv2.imshow("thresh",thresh)
    cv2.waitKey(0)
    #image, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    contours,hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)  
    #绘制独立轮廓，如第四个轮廓：im原图，contours轮廓，(0,255,0) 轮廓颜色
    cv2.drawContours(im,contours,-1,(0,255,0),3)  
    cv2.imshow("contours",im)
    cv2.waitKey(0)
    #但是大多数时候，下面的方法更有用：
    #img = cv2.drawContours(img, contours, 3, (0,255,0), 3)

image_contours()