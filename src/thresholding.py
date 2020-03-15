import cv2
import os
import numpy as np

def thresholdOp(folderpath,filepath,thresh):
    filepath=folderpath+filepath
    print("thresh--",filepath)
    img=cv2.imread(filepath, cv2.IMREAD_UNCHANGED)
    img=cv2.imread("static/images/cube.jpg")
    thresh=int(thresh)
    # threshimg = cv2.threshold(img,thresh,255,cv2.THRESH_TRUNC)
    # threshimg = cv2.threshold(img, 200, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    threshimg=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv2.THRESH_BINARY,11,2)

    destpath=os.path.basename(filepath)
    # cv2.imshow("img",threshimg)

    destpath="images/"+destpath.split(".")[0]+"_thresh"+".jpg"
    print(folderpath+destpath)

    cv2.imwrite(folderpath+destpath,threshimg)


    # cv.imshow('canvasOutput', dst);
    # src.delete(); dst.delete();
    return destpath