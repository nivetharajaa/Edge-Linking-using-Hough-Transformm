# In[ ]:## Read image and convert it to grayscale image
## Developed by : NIVETHA A
## Reg no : 212222230101

import numpy as np
import cv2
import matplotlib.pyplot as plt
img=cv2.imread("TM.jpg",0)
img_c=cv2.imread("TM.jpg",1)
img_c=cv2.cvtColor(img_c,cv2.COLOR_BGR2RGB)
gray=cv2.cvtColor(img,cv2.COLOR_GRAY2RGB)
gray = cv2.GaussianBlur(gray,(3,3),0)
plt.figure(figsize=(13,13))
plt.subplot(1,2,1)
plt.imshow(img_c)
plt.title("Original Image")
plt.axis("off")
plt.subplot(1,2,2)
plt.imshow(gray)
plt.title("Gray Image")
plt.axis("off")
plt.show()

#DISPLAY THE CANNY IMAGE 
canny=cv2.Canny(gray,70,90)
plt.imshow(canny)
plt.title("Canny Edge Detector")
plt.axis("off")
plt.show()

lines=cv2.HoughLinesP(canny,1,np.pi/180,threshold=80,minLineLength=50,maxLineGap=250)

for line in lines:
    x1,y1,x2,y2=line[0]
    cv2.line(img_c,(x1,y1),(x2,y2),(255,0,0),3)

lines=cv2.HoughLinesP(canny,1,np.pi/180,threshold=90,minLineLength=50,maxLineGap=90)
## Display the result
plt.imshow(img_c)
plt.title("Result Image")
plt.axis("off")
plt.show()
## Developed by :Nivetha A
## Reg no : 212222230101


