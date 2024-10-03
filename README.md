# Edge-Linking-using-Hough-Transformm
## Aim:
To write a Python program to detect the lines using Hough Transform.

## Software Required:
Anaconda - Python 3.7

## Algorithm:
### Step1:

Import all the necessary modules for the program.
### Step2:

Load a image using imread() from cv2 module.
### Step3:

Convert the image to grayscale.
### Step4:

Using Canny operator from cv2,detect the edges of the image.
### Step5:

Using the HoughLinesP(),detect line co-ordinates for every points in the images.Using For loop,draw the lines on the found co-ordinates.Display the image.

## Program:

### DEVELOPED BY: Nivetha A
### REGISTER NO: 212222230101

#### Read image and convert it to grayscale image:
```
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
````
### Find the edges in the image using canny detector and display:
```
canny=cv2.Canny(gray,70,90)
plt.imshow(canny)
plt.title("Canny Edge Detector")
plt.axis("off")
plt.show()
```
### Detect points that form a line using HoughLinesP:
```
lines=cv2.HoughLinesP(canny,1,np.pi/180,threshold=90,minLineLength=50,maxLineGap=90)

Draw lines on the image:

for line in lines:
    x1,y1,x2,y2=line[0]
    cv2.line(img_c,(x1,y1),(x2,y2),(0,0,255),3)
```
### Display the result:
```
plt.imshow(img_c)
plt.title("Result Image")
plt.axis("off")
plt.show()
```
## Output

### Input image and grayscale image
![328906823-583b09e3-bff0-4f60-a23b-1eafad65ab4e](https://github.com/user-attachments/assets/e8a96b82-0a6b-4f3a-b7f7-c1123675c832)

### Canny Edge detector output
![328906921-0d91a002-8837-48c2-916b-c6dcd5839a88](https://github.com/user-attachments/assets/4c1f55fa-63a9-47f0-890a-a58b1f421f99)

### Display the result of Hough transform

![328907031-f849d7bc-76a4-4b25-9600-59923b667428](https://github.com/user-attachments/assets/5b6789d0-19d2-48a9-b83b-8854a12e2a9b)

## Result:
Thus, the program is written with python and OpenCV to detect lines using Hough transform.
