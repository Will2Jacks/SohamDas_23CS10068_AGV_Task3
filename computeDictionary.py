import pickle
from getDictionary import get_dictionary


meta = pickle.load(open('../data/traintest.pkl', 'rb'))
train_imagenames = meta['train_imagenames']


# -----fill in your implementation here --------

random_dict=get_dictionary(train_imagenames,50,100,'Random')
pickle.dump(random_dict,'../data/dictionaryRandom.pkl')

harris_dict=get_dictionary(train_imagenames,50,100,'Random')
pickle.dump(random_dict,'../data/dictionaryHarris.pkl')
# ----------------------------------------------


