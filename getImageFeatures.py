import numpy as np


def get_image_features(wordMap, dictionarySize):

    # -----fill in your implementation here --------

    h = np.bincount(wordMap.ravel(), minlength=dictionarySize)
    return h
    # ----------------------------------------------
    
    
