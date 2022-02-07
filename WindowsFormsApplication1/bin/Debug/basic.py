import cv2
import sys
import math
import numpy as np
import matplotlib.pyplot as plt
import scipy.ndimage

def operation(image, r, op, intensity):
    min = int(r.split(",")[0])
    max = int(r.split(",")[1])
    img = cv2.imread(image, cv2.IMREAD_GRAYSCALE).astype(float) # read image
    imageSub = img.copy()
    rows,cols=img.shape
    for i in range(int(rows)):
        for j in range(int(cols)):
            if img[i, j] >= min and img[i, j] <= max:
                if op == "+":
                    imageSub[i, j] = img[i, j] - intensity

                elif op == "-":
                    imageSub[i, j] = img[i, j] - intensity
                    print(img[i, j] , "  " , imageSub[i, j])
                elif op == "*":
                    imageSub[i, j] = img[i, j] * intensity
                else:
                    imageSub[i, j] = img[i, j] / intensity

    cv2.imwrite("airthematic.jpg", imageSub)
    return "airthematic.jpg"

if sys.argv[1]=="+"or sys.argv[1]=="-" or sys.argv[1]=="*" or sys.argv[1]=="/":
  print(operation(sys.argv[3].replace("/","//"),sys.argv[2],sys.argv[1],int(sys.argv[4])),end="")

elif sys.argv[1]=="OilPainting":
    img=cv2.imread(sys.argv[2].replace("/","//"))
    img2=cv2.xphoto.oilPainting(img,7,1)
    cv2.imwrite("oil.jpg",img2)
    print("oil.jpg")

elif sys.argv[1]=="Watercolor":
    img=cv2.imread(sys.argv[2].replace("/","//"))
    res = cv2.stylization(img, sigma_s=60, sigma_r=0.6)
    cv2.imwrite("watercolor.jpg",res)
    print("watercolor.jpg")


elif sys.argv[1]=="Pencilsketch":
    img = cv2.imread(sys.argv[2].replace("/", "//"),cv2.IMREAD_GRAYSCALE)
    inverted_img = 255 - img
    blur_img = cv2.GaussianBlur(inverted_img,(21,21),0)
    inverted_img=255-blur_img
    pencil=cv2.divide(img,inverted_img,scale=256.0)
    cv2.imwrite("pencil.jpg",pencil)
    print("pencil.jpg")
