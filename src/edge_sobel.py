import numpy as np
import cv2
import os
from matplotlib import pyplot as plt
from Matrix_Convolution import convolution_np

def edgeDetect(folderpath,filepath):
    # print(path)
    filepath=folderpath+filepath
    original=cv2.imread(filepath, cv2.IMREAD_UNCHANGED)
    img=cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
    print("done1")
    height=img.shape[0]
    width=img.shape[1]

    Hx=np.array([[-1,0,1],
             [-2,0,2],
             [-1,0,1]])

    Hy=np.array([[-1,-2,-1],
             [0,0,0],
             [1,2,1]])

    img_x=convolution_np(img,Hx)/8.0
    img_y=convolution_np(img,Hy)/8.0

    img_out=np.sqrt(np.power(img_x,2)+np.power(img_y,2))

    img_out=(img_out/np.max(img_out))*255
    print("done2")
    destpath=os.path.basename(filepath)
  
    destpath="images/"+destpath.split(".")[0]+"_edge"+".jpg"
    print(folderpath+destpath)

    cv2.imwrite(folderpath+destpath,img_out)
    # print("done3")
    # fig=plt.figure()
    # fig.add_subplot(1,2,1)
    # plt.imshow(original)
    # plt.xticks([]),plt.yticks([])
    # a.set_title("Original Image")
    # fig.add_subplot(1,2,2)
    # plt.imshow(img_out,cmap='gray',interpolation='bicubic')
    # plt.xticks([]),plt.yticks([])
    # a.set_title("Edge")
    # plt.show()
    return destpath
