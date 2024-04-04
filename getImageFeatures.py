import numpy as np


def get_image_features(wordMap, dictionarySize):

    # -----fill in your implementation here --------

    h=[]
    for i in range(dictionarySize):
        h.append(0)
    h=np.array(h)
    for val in range(dictionarySize):
        h[val]=np.count(wordMap,val)
    # ----------------------------------------------
    
    return h