import numpy as np
import cv2
from matplotlib import pyplot as plt

file_path_img = r'D:\work\ai\face\demo\5903040bf4146.jpg'
    
img = cv2.imread(file_path_img,0)
# 别忘了中括号 [img],[0],None,[256],[0,256] ，只有 mask 没有中括号
plt.hist(img.ravel(),256,[0,256]); plt.show()