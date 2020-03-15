import numpy as np

def convolution_np(X,F):
    X_height=X.shape[0]
    X_width=X.shape[1]
    
    F_height=F.shape[0]
    F_width=F.shape[1]
    
    H=(F_height-1)/2
    W=(F_height-1)/2
    
    out=np.zeros((X_height,X_width))
    
    for i in np.arange(H,X_height-H):
        for j in np.arange(W,X_width-W):
            sum=0
            for k in np.arange(-H,H+1):
                for l in np.arange(-W,W+1):
                    a=X[(int)(i+k),(int)(j+l)]
                    w=F[(int)(H+k),(int)(W+l)]
                    sum+=(w*a)
                out[(int)(i),(int)(j)]=sum
    print("done4")
    return out
