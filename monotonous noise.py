import cv2
import numpy as np
img=cv2.imread("digital.jpg")
width=img.shape[1]
height=img.shape[0]
noise=np.random.uniform(-50,50,(height,width,3)).astype(np.uint8)
noise_img=cv2.add(img,noise)
cv2.imshow("original img",img)
cv2.imshow("noise img",noise_img)
cv2.waitKey(0)