import cv2
import numpy as np
from matplotlib import pyplot as plt

file_path_img = r'D:\work\ai\face\demo\5903040bf4146.jpg'

img = cv2.imread(file_path_img,0)
edges = cv2.Canny(img,100,300)

plt.subplot(121),plt.imshow(img,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

plt.show()