import cv2
import sys
import math
import numpy as np
import matplotlib.pyplot as plt

def meanFilter(img,window_size):
    image = cv2.imread(img,cv2.IMREAD_GRAYSCALE)
    kernel = np.ones((window_size, window_size), np.float32) / window_size**2
    dst = cv2.filter2D(image, -1, kernel)
    cv2.imwrite("mean.JPG",dst)
    return "mean.JPG"

def gaussianFilter(img,window_size):
    image = cv2.imread(img, cv2.IMREAD_GRAYSCALE)
    gaussian = cv2.GaussianBlur(image, (window_size, window_size),0)
    cv2.imwrite("gaussian.jpg", gaussian)
    return "gaussian.jpg"


def medianFilter(img,window_size):
    image = cv2.imread(img, cv2.IMREAD_GRAYSCALE)
    median = cv2.medianBlur(image, window_size)
    cv2.imwrite("medianfilter.jpg",median)
    return  "medianfilter.jpg"

def laplacianFilter(image):
    image = cv2.imread(image, cv2.IMREAD_GRAYSCALE)
    laplacian = cv2.Laplacian(image,cv2.CV_64F)
    cv2.imwrite("laplcian.jpg", laplacian)
    return "laplcian.jpg"

def sobel(image):
    x = cv2.Sobel(image, cv2.CV_16S, 1, 0)
    y = cv2.Sobel(image, cv2.CV_16S, 0, 1)
    absX = cv2.convertScaleAbs(x)  # Transfer back to uint8
    absY = cv2.convertScaleAbs(y)
    dst = cv2.addWeighted(absX, 0.5, absY, 0.5, 0)
    cv2.imwrite("soble.jpg",dst)
    return  "soble.jpg"



if sys.argv[1]=="Mean":
    print(meanFilter(sys.argv[3].replace("/","//"),int(sys.argv[2])),end="")

elif sys.argv[1]=="Median":
    print(medianFilter(sys.argv[3].replace("/","//"),int(sys.argv[2])),end="")

elif sys.argv[1]=="Gaussian":
    print(gaussianFilter(sys.argv[3].replace("/","//"),int(sys.argv[2])),end="")

elif sys.argv[1]=="Laplacian":
    print(laplacianFilter(sys.argv[2].replace("/","//")),end="")
