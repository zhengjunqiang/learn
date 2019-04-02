import cv2
import numpy as np
from matplotlib import pyplot as plt

file_path_img = r'D:\work\ai\face\demo\5903040bf4146.jpg'

#pyplot 使用说明
def pyplot_use():
    plt.plot([1,2,3,4],[3,4,7,80])  #二维点
    #plt.plot([1,2,3,4],[1,4,9,16])
    plt.ylabel('some numbers')
    plt.show()

def f1(t):
    return np.exp(-t)*np.cos(2*np.pi*t)

def f2(t):
    return np.sin(2*np.pi*t)*np.cos(3*np.pi*t)

def pyplot_use_2():
    t = np.arange(0.0,5.0,0.02)

    plt.figure(figsize=(8,7),dpi=98)
    p1 = plt.subplot(211)
    p2 = plt.subplot(212)

    p1.plot(t,f1(t),"g-",label="$f(t)=e^{-t} \cdot \cos (2 \pi t)$")
    p2.plot(t,f2(t),"r-.",label="$g(t)=\sin (2 \pi t) \cos (3 \pi t)$",linewidth=2)

    p1.axis([0.0,5.01,-1.0,1.5])

    p1.set_ylabel("v",fontsize=14)
    p1.set_title("A simple example",fontsize=18)
    p1.grid(True)
    p1.legend()

    p2.axis([0.0,5.01,-1.0,1.5])
    p2.set_ylabel("v",fontsize=14)
    p2.set_xlabel("t",fontsize=14)
    p2.legend()

    plt.show()    

#2D 卷积
def show_2d_convolution():
    img = cv2.imread(file_path_img)

    kernel = np.ones((5,5),np.float32)/25
    print(kernel)
    dst = cv2.filter2D(img,-1,kernel)

    plt.subplot(121)
    plt.imshow(img)
    plt.title('Original')
    plt.xticks([]), plt.yticks([])

    plt.subplot(122)
    plt.imshow(dst)
    plt.title('Averaging')
    plt.xticks([]), plt.yticks([])
    plt.show()

#平均
def show_blur():
    img = cv2.imread(file_path_img)
    blur = cv2.blur(img,(5,5))

    plt.subplot(121),plt.imshow(img),plt.title('Original')
    plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(blur),plt.title('Blurred')
    plt.xticks([]), plt.yticks([])
    plt.show()

#高斯
def show_gaosiblur():
    img = cv2.imread(file_path_img)
    blur = cv2.GaussianBlur(img,(5,5),0)

    plt.subplot(121),plt.imshow(img),plt.title('Original')
    plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(blur),plt.title('Blurred')
    plt.xticks([]), plt.yticks([])
    plt.show()

 #中值
def show_gaosiblur():
    img = cv2.imread(file_path_img)
    blur = cv2.medianBlur(img,5)

    plt.subplot(121),plt.imshow(img),plt.title('Original')
    plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(blur),plt.title('Blurred')
    plt.xticks([]), plt.yticks([])
    plt.show()   
#pyplot_use_2()
#show_2d_convolution()
#show_gaosiblur()
show_gaosiblur()