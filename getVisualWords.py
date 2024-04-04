import numpy as np
from scipy.spatial.distance import cdist
from extractFilterResponses import extract_filter_responses


def get_visual_words(I, dictionary, filterBank):

    # -----fill in your implementation here --------

    h=I.shape[0]
    w=I.shape[1]

    wordMap = np.zeros((h,w))

    val=list(dict.keys)[0]
    mini=100000
    min_val=val
    for i in range(h):
        for j in range(w):
            for value in dictionary:
                d=cdist(I, dictionary[value], 'euclidean')
                if(d<mini):
                    mini=d
                    min_val=value 
            wordMap[i,j]=min_val
    


    # ----------------------------------------------

    return wordMap
