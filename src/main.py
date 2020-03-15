from flask import *  
import numpy as np
import cv2
import os
from matplotlib import pyplot as plt
import edge_sobel 
import thresholding
import cv
from Matrix_Convolution import convolution_np
from averaging import gaussian_blur


app = Flask(__name__, static_folder='static')

@app.route('/')  
def upload():  
    return render_template("img_upload_form.html") 
 
@app.route('/success', methods = ['POST'])  
def success():  
    if request.method == 'POST':  
        f = request.files['file'] 
     
        # import pdb;pdb.set_trace()
        global originalFile
        originalFile=f.filename.split(".")[0]+".jpg"

        global folderpath
        folderpath="static/"
        global Originalfilepath
        Originalfilepath="images/"+originalFile
        
        # print("success"+filepath)
        f.save(folderpath+Originalfilepath)
        global call
        call=True
        global Edge
        EdgeFile=Originalfilepath

        return render_template("success.html", name = f.filename)

# @app.route('/average', methods = ['POST'])
# def blur():
#     if request.method == 'POST':  
        
#         window_size=request.form['window-size'] 
        
#         sigma=request.form['sigma']
#         # print("blur"+folderpath+" "+filepath)
        
#         destpath=gaussian_blur(window_size,folderpath,Edge,sigma,True)
#         global firstAverg
#         firstAverg=destpath
#         return render_template("display.html",left="Edge Detected",leftimg=Edge,right="Filtered Image",rightimg=firstAverg)
#     else:
#         return render_template("failure.html")

@app.route('/detect', methods = ['POST'])
def edge():
    if request.method == 'POST': 
        global folderpath 
        global filepath 
        global EdgeFile
        global threshpath
        global Originalfilepath
        global call
        # import pdb;pdb.set_trace()
        window_size=int(request.form['window-size'])
        sigma=int(request.form['sigma'])
        # EdgeFile=Originalfilepath
        
        # print("blur"+folderpath+" "+filepath)
        
        if window_size==0 and sigma==0 and call:
            destpath=edge_sobel.edgeDetect(folderpath,Originalfilepath)
            EdgeFile=destpath
            threshpath=EdgeFile
            print("detect true input-- "+Originalfilepath)
            print("detect true output-- "+EdgeFile)
            return render_template("display.html",left="Original Image",leftimg=Originalfilepath,right="Unfiltered Edge Detection",rightimg=EdgeFile)
        else:
            
            destpath=gaussian_blur(window_size,folderpath,Originalfilepath,sigma,True)
            print("detect false input--"+Originalfilepath+" "+destpath)
            destpath=edge_sobel.edgeDetect(folderpath,destpath)
            
            print("detect false output--"+destpath)
            threshpath=destpath
            
            call=False
            return render_template("display.html",left="Unfiltered Edge Detection",leftimg=EdgeFile,right="Filtered Edge Detection",rightimg=destpath)
    else:
        return render_template("failure.html")

@app.route('/threshold', methods = ['POST'])
def maximise():
    if request.method=='POST':
        thresh=request.form['thresh']
        global destpath
        print("detect false input--"+threshpath)
        destpath=thresholding.thresholdOp(folderpath,threshpath,thresh)
        print("detect false--"+destpath)
        return render_template("display.html",left="Unfiltered Edge Detection",leftimg=threshpath,right="Threshold of "+thresh,rightimg=destpath)
    else:
        return render_template("failure.html")

@app.route('/view', methods = ['GET'])
def display():
    if request.method=='GET':
        path = 'static/images/'
        files = []
        global originalFile
        # r=root, d=directories, f = files
        for r, d, f in os.walk(path):
            for file in f:
                if '.jpg' in file and originalFile.split(".")[0] in file:
                    files.append(os.path.join(r, file))

            for f in files:
                print(f)
    return render_template("view_all.html",images=files)

if __name__ == '__main__':  
    app.run(debug = True)  