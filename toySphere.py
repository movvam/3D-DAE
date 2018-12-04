import numpy as np
import pandas as pd
import math

def center(width, height, depth):
    return (width//2, height//2, depth//2)

#returns voxel representation of a sphere at the point x,y with radius r
def sphere(width,height,depth,x,y,z,r):
    envn=np.full((width,height,depth),0.0)
    
    #center coordinates
    c_x,c_y,c_z=center(width,height,depth)
    
    #coordinates of sphere center
    sc_x=x+c_x
    sc_y=y+c_y
    sc_z=z+c_z
        
    #setting x value boundaries
    x_pos = math.ceil(sc_x + r)
    if x_pos >= width:
        x_pos = width - 1
    x_neg = math.floor(sc_x - r)
    if x_neg < 0:
        x_neg = 0
    #print("x (pos neg): ", x_pos, " ", x_neg)
    
    #setting y value boundaries
    y_pos = math.ceil(sc_y + r)
    if y_pos >= height:
        y_pos = height - 1
    y_neg = math.floor(sc_y - r)
    if y_neg < 0:
        y_neg = 0
    #print("y (pos neg): ", y_pos, " ", y_neg)
    
    #setting z value boundaries
    z_pos = math.ceil(sc_z + r)
    if z_pos >= depth:
        z_pos = depth - 1
    z_neg = math.floor(sc_z - r)
    if z_neg < 0:
        z_neg = 0
    
    for i in range(x_neg, x_pos + 1):
        ii = (i-sc_x)*(i-sc_x)
        for j in range(y_neg, y_pos + 1):
            jj = (j-sc_y)*(j-sc_y)
            for k in range(z_neg, z_pos + 1):
                if (ii + jj + (k-sc_z)*(k-sc_z) < r*r):
                    envn[i, j, k] = 1.0

    return envn
