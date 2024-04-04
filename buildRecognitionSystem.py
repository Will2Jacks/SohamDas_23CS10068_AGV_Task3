import pickle
from createFilterBank import create_filterbank
from getDictionary import get_dictionary
import computeDictionary
from getImageFeatures import get_image_features
from getVisualWords import get_visual_words
import numpy as np

randomDict = pickle.load(open('dictionaryRandom.pkl', 'rb'))
harrisDict = pickle.load(open('dictionaryHarris.pkl', 'rb'))

visionRandom={}
visionHarris={}

filterBank=create_filterbank()

def build():

    visionRandom['dictionary']=randomDict
    visionHarris['dictionary']=harrisDict



    visionRandom['filterBank']=filterBank
    visionHarris['filterBank']=filterBank

    visionRandom['trainLabels']=[]
    visionHarris['trainLabels']=[]

    visionRandom['trainFeatures']=[]
    visionHarris['trainFeatures']=[]

    meta = pickle.load(open('../data/traintest.pkl', 'rb'))
    all_imagenames = meta['all_imagenames']

    for img_ind in range(len(all_imagenames)):
        img_name = all_imagenames[img_ind]
        llrandom=pickle.load(open('../data/%s_%s.pkl' % (img_name[:-4], 'Random'), 'rb'))
        llharris=pickle.load(open('../data/%s_%s.pkl' % (img_name[:-4], 'Random'), 'rb'))
        visionRandom['trainLabels'].append(llrandom)
        visionHarris['trainLabels'].append(llharris)

    for img_ind in range(len(all_imagenames)):
        img_name = all_imagenames[img_ind]
        llrandom=pickle.load(open('../data/%s_%s.pkl' % (img_name[:-4], 'Random'), 'rb'))
        llharris=pickle.load(open('../data/%s_%s.pkl' % (img_name[:-4], 'Random'), 'rb'))
        visionRandom['trainFeatures'].append(get_image_features(visionRandom['trainLabels'],len(visionRandom['dictionary'])))
        visionHarris['trainFeatures'].append(get_image_features(visionHarris['trainLabels'],len(visionHarris['dictionary'])))

    pickle.dump(visionRandom, open('../data/visionRandom.pkl'), 'wb')
    pickle.dump(visionHarris, open('../data/visionHarris.pkl'), 'wb')

        




