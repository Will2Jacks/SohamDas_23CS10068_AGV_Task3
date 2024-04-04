import numpy as np
from utils import chi2dist
import pickle
from createFilterBank import create_filterbank
from getDictionary import get_dictionary
import computeDictionary
from getImageFeatures import get_image_features
from getVisualWords import get_visual_words
import numpy as np

def get_image_distance_euclidean(hist1,hist2,method):
    sums=0
    for i in range(len(hist1)):
        num=pow(hist1[i]-hist2[i])
        sums+=num/hist1[i]
    return sums

dict1=pickle.load( open('../data/visionRandom.pkl'), 'rb')
dict2=pickle.load( open('../data/visionHarris.pkl'), 'rb')

random_hist=dict1['trainFeatures']
harris_hist=dict2['trainFeatures']

hist_len_random_euclidean=np.zeroes((len(random_hist),len(random_hist)))
hist_len_harris_euclidean=np.zeroes((len(harris_hist),len(harris_hist)))

hist_len_random_chi2=np.zeroes((len(random_hist),len(random_hist)))
hist_len_harris_chi2=np.zeroes((len(harris_hist),len(harris_hist)))


for val1 in range(len(random_hist)-1):
    for val2 in range(val1+1,len(random_hist)):
        hist_len_random_euclidean[val1,val2]=get_image_distance_euclidean(random_hist[val1],random_hist[val2],'Random')
        hist_len_harris_euclidean[val1,val2]=get_image_distance_euclidean(harris_hist[val1],harris_hist[val2],'Harris')
        hist_len_random_chi2[val1,val2]=chi2dist(random_hist[val1],random_hist[val2])
        hist_len_harris_chi2[val1,val2]=chi2dist(harris_hist[val1],harris_hist[val2])






