import cv2
import sys
import math
import numpy as np
from skimage import exposure
import matplotlib.pyplot as plt

def canny(img,thr1,thr2):
    img = cv2.imread(img,cv2.IMREAD_GRAYSCALE)
    img_gaussian = cv2.GaussianBlur(img, (3, 3), 0)
    img_canny = cv2.Canny(img_gaussian, thr1, thr2)
    cv2.imwrite("canny.jpg",img_canny)
    return "canny.jpg"


def sobel(img):
    img = cv2.imread(img, cv2.IMREAD_GRAYSCALE)
    img_gaussian = cv2.GaussianBlur(img, (3, 3), 0)
    img_sobelx = cv2.Sobel(img_gaussian, cv2.CV_8U, 1, 0, ksize=5)
    img_sobely = cv2.Sobel(img_gaussian, cv2.CV_8U, 0, 1, ksize=5)
    img_sobel = img_sobelx + img_sobely
    cv2.imwrite("sobel.jpg", img_sobel)
    return "sobel.jpg"

def prewitt(img):
    img = cv2.imread(img, cv2.IMREAD_GRAYSCALE)
    img_gaussian = cv2.GaussianBlur(img, (3, 3), 0)
    kernelx = np.array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]])
    kernely = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])
    img_prewittx = cv2.filter2D(img_gaussian, -1, kernelx)
    img_prewitty = cv2.filter2D(img_gaussian, -1, kernely)
    res=np.concatenate((img_prewittx,img_prewitty),axis=1)
    cv2.imwrite("prewitt.jpg", res)
    return "prewitt.jpg"



if sys.argv[1]=="Canny":
    thres1=int(sys.argv[2].split(",")[0])
    thres2=int(sys.argv[2].split(",")[1])
    print(canny(sys.argv[3].replace("/","//"),thres1,thres2))

elif sys.argv[1]=="Sobel":
    print(sobel(sys.argv[2].replace("/","//")))

elif sys.argv[1]=="Prewitt":
    print(prewitt(sys.argv[2].replace("/","//")))
