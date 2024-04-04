import cv2 as cv
import numpy as np
from utils import *

def extract_filter_responses(I, filterBank):

    I = I.astype(np.float64)
    if len(I.shape) == 2:
        I = np.tile(I, (3, 1, 1))
    
    red=I[:,:,0]
    green=I[:,:,1]
    blue=I[:,:,2]

    filterResponses=[]

    filterresponsesRed=[]
    filterresponsesGreen=[]
    filterresponsesBlue=[]

    for h in filterBank:
        I_red = ndimage.filters.correlate(red, h, mode='constant')
        filterresponsesRed.append(I_red)
        I_green = ndimage.filters.correlate(green, h, mode='constant')
        filterresponsesGreen.append(I_green)
        I_blue = ndimage.filters.correlate(blue, h, mode='constant')
        filterresponsesBlue.append(I_blue)
    
    filterResponses.append(filterresponsesRed)
    filterResponses.append(filterresponsesGreen)
    filterResponses.append(filterresponsesBlue)

    filterResponses=np.array(filterResponses)

    # -----fill in your implementation here --------


    # ----------------------------------------------
    
    return filterResponses