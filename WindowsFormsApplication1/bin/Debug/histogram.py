import cv2
import sys
import math
import numpy as np
from skimage import exposure
import matplotlib.pyplot as plt

def histogram(img):
    fig, ((ax0, ax1)) = plt.subplots(nrows=1, ncols=2)
    im=cv2.imread(img,cv2.IMREAD_GRAYSCALE)
    ax1.imshow(im,cmap="gray")
    ax1.set_title("image")
    ax0.hist(im.ravel(),256,[0,256])
    ax0.set_title("histogram")
    plt.savefig("hist.png")
    return "hist.png"

def histogram_equ(image,d):
    img = cv2.imread(image, cv2.IMREAD_GRAYSCALE)  # read image
    fig, ((ax0, ax1),(ax2,ax3)) = plt.subplots(nrows=2, ncols=2)
    ax0.imshow(img,cmap="gray")
    ax0.set_title("image")
    ax1.hist(img.ravel(),256,[0,256])
    ax1.set_title("image histogram")
    for i in range(d):
        iteration = cv2.equalizeHist(img)
        if i==0:
            ax2.set_title("first Iteration")
            ax2.hist(iteration.ravel(), 256, [0, 256])
        elif i==(d-1):
            ax3.set_title("last iteration")
            ax3.hist(iteration.ravel(), 256, [0, 256])
        img=iteration
    plt.tight_layout()
    plt.savefig("equalize.png")
    return "equalize.png"


def histogramMatching(s,r):
    src = cv2.imread(s, cv2.IMREAD_GRAYSCALE)
    ref = cv2.imread(r, cv2.IMREAD_GRAYSCALE)
    matched = exposure.match_histograms(src, ref, multichannel=False)
    fig, ((ax0, ax1), (ax2, ax3)) = plt.subplots(nrows=2, ncols=2)

    ax0.hist(src.ravel(), 256, [0, 256])
    ax0.set_title("source")

    ax1.hist(ref.ravel(), 256, [0, 256])
    ax1.set_title("reference")

    ax2.hist(matched.ravel(), 256, [0, 256])
    ax2.set_title("matched hist")

    ax3.imshow(matched,cmap="gray")
    ax3.set_title("matched image")
    plt.tight_layout()
    plt.savefig("matched.png")
    return "matched.png"

if sys.argv[1]=="Histogram":
    print(histogram(sys.argv[2].replace("/","//")))

elif sys.argv[1]=="HistogramEuqlization":
    print(histogram_equ(sys.argv[2].replace("/","//"),int(sys.argv[3])))

elif sys.argv[1]=="HistogramMatching":
    print(histogramMatching(sys.argv[2].replace("/","//"),sys.argv[3]))
