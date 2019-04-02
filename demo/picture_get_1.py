import cv2
import numpy as np

filename = r'D:\work\ai\face\demo\timg.jpg'

img = cv2.imread(filename)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#转化类型
gray = np.float32(gray)

dst = cv2.cornerHarris(gray,2,3,0.04)

#result is dilated for marking the corners, not important
dst = cv2.dilate(dst,None)

# Threshold for an optimal value, it may vary depending on the image.
img[dst>0.03*dst.max()] = [0,255,0]

cv2.imshow('dst',img)
cv2.waitKey(0)