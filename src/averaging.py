import numpy as np
import cv2
import argparse
import matplotlib.pyplot as plt
import math
import os
from Gaus_Convolution import convolution


def dnorm(x, mu, sd):
    return 1 / (np.sqrt(2 * np.pi) * sd) * np.e ** (-np.power((x - mu) / sd, 2) / 2)


def gaussian_kernel(size,sigma, verbose):
    kernel_1D = np.linspace(-(size // 2), size // 2, size)
    for i in range(size):
        kernel_1D[i] = dnorm(kernel_1D[i], 0, sigma)
    kernel_2D = np.outer(kernel_1D.T, kernel_1D.T)

    kernel_2D *= 1.0 / kernel_2D.max()

    if verbose:
        plt.imshow(kernel_2D, interpolation='none', cmap='gray')
        plt.title("Kernel ( {}X{} )".format(size, size))
        # plt.show()
    
    return kernel_2D

    


def gaussian_blur(kernel_size,folderpath,filepath,sigma, verbose):
    filepath=folderpath+filepath
    img=cv2.imread(filepath, cv2.IMREAD_UNCHANGED)
    kernel_size=int(kernel_size)
    sigma=int(sigma)
    kernel = gaussian_kernel(kernel_size, sigma, verbose)
    output= convolution(img, kernel, True, verbose)
    destpath=os.path.basename(filepath)
    destpath="images/"+destpath.split(".")[0]+"_avg"+".jpg"
    print(folderpath+destpath)
    cv2.imwrite(folderpath+destpath,output)
    return destpath

