import cv2
import os
import numpy as np
import time

file_path_img = r'D:\work\ai\face\demo\5903040bf4146.jpg'
file_path_txt = r'D:\work\ai\face\demo\a.txt'

#windows下 打开 文件 要加上r，单引号双引号都可以
def file_open():
    fr=open(file_path_txt)
    arrayOLines = fr.readlines()
    print(arrayOLines)

#显示图片
def show_image(img_type):
    img = cv2.imread(file_path_img,img_type)
    print(img)
    cv2.imshow(str(img_type),img)
    cv2.waitKey(5000)

#多维数组
def np_use():
    files = [1,3,4,5]
    features_matrix = np.zeros((512,512,3))
    print(features_matrix)

#画图
def show_line(image_name):
    # Create a black image，img 画板,512*512 个像素，每个像素8个bit表示
    img = np.zeros((512,512,3), np.uint8)
    # Draw a diagonal blue line with thickness of 5 px
    cv2.line(img,(0,0),(512,512),(255,0,0),5)
    cv2.imshow(image_name,img)
    cv2.waitKey(0)

def show_rectangle(image_name):
    # Create a black image，img 画板,512*512 个像素，每个像素8个bit表示
    img = np.zeros((512,512,3), np.uint8)
    # Draw a diagonal blue line with thickness of 5 px
    cv2.rectangle(img,(0,0),(510,510),(0,255,0),3)
    cv2.imshow(image_name,img)
    cv2.waitKey(0)    

#彩色模式打开
#show_image(cv2.IMREAD_COLOR)
#灰度模式打开
#show_image(cv2.IMREAD_GRAYSCALE)
#读入一幅图像，并且包括图像的 alpha 通道
#show_image(cv2.IMREAD_UNCHANGED)
#cv2.destroyAllWindows()

#画图
#np_use()
#show_line("line")
show_rectangle("show_rectangle")
print("end")