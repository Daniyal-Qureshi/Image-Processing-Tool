import sys
import cv2
import numpy as np
import random
import math
import matplotlib.pyplot as plt

def uniform(img):
    image = cv2.imread(img,cv2.IMREAD_GRAYSCALE)
    uniform_noise = np.zeros((image.shape[0], image.shape[1]), dtype=np.float32)
    cv2.imwrite("uniform.jpg",uniform_noise)
    return "uniform.jpg"


def salt(img,min,max):
    image = cv2.imread(img,cv2.IMREAD_GRAYSCALE)
    row,col = image.shape
    number_of_pixels = random.randint(min, max)
    for i in range(number_of_pixels):
        y_coord = random.randint(0, row - 1)
        x_coord = random.randint(0, col - 1)
        image[y_coord][x_coord] = 255
    cv2.imwrite("salt.jpg",image)
    return "salt.jpg"

def pepper(img,min,max):
    image = cv2.imread(img,cv2.IMREAD_GRAYSCALE)
    row, col = image.shape
    number_of_pixels = random.randint(min, max)
    for i in range(number_of_pixels):
        y_coord = random.randint(0, row - 1)
        x_coord = random.randint(0, col - 1)
        image[y_coord][x_coord] = 0
    cv2.imwrite("pepper.jpg",image)
    return "pepper.jpg"

#-----------------gaussian noise
def gaussian(img,mean,sigma):
    image = cv2.imread(img,cv2.IMREAD_GRAYSCALE)
    noise = np.random.normal(mean, sigma, (image.shape[0],image.shape[1]))
    gaussian=noise+image
    cv2.imwrite("GaussNoise.jpg",gaussian)
    return "GaussNoise.jpg"

#---------------Speckle noise
def speckle(img):
    image = cv2.imread(img,cv2.IMREAD_GRAYSCALE)
    row,col = image.shape
    gauss = np.random.randn(row,col)
    gauss = gauss.reshape(row,col)
    speckle = image + image * gauss
    cv2.imwrite("speckle.jpg",speckle)
    return "speckle.jpg"
 
#-----------------poison noise

def poison(img):
    image = cv2.imread(img,cv2.IMREAD_GRAYSCALE)
    noise_mask = np.random.poisson(image)
    poison = image + noise_mask
    cv2.imwrite("poison.jpg",poison)
    return "poison.jpg"

# print("called",sys.argv[1])
    
if sys.argv[1]=="Salt":
    min=int(sys.argv[2].split(",")[0])
    max = int(sys.argv[2].split(",")[1])
    print(salt(sys.argv[3].replace("/","//"),min,max),end="")

elif sys.argv[1]=="Pepper":
    min=int(sys.argv[2].split(",")[0])
    max = int(sys.argv[2].split(",")[1])
    print(pepper(sys.argv[3].replace("/","//"),min,max),end="")

elif sys.argv[1]=="Gaussian":
    mean=float(sys.argv[2].split(",")[0])
    sigma = float(sys.argv[2].split(",")[1])
    print(gaussian(sys.argv[3].replace("/","//"),mean,sigma),end="")
	

elif sys.argv[1]=="Uniform":
    print(uniform(sys.argv[2].replace("/","//")),end="")


elif sys.argv[1]=="Speckle":
    print(speckle(sys.argv[2].replace("/","//")),end="")

elif sys.argv[1]=="Poisson":
    print(poison(sys.argv[2].replace("/","//")),end="")




