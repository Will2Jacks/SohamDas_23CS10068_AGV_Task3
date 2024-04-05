import pickle
from getDictionary import get_dictionary


meta = pickle.load(open('../data/traintest.pkl', 'rb'))
train_imagenames = meta['train_imagenames']


# -----fill in your implementation here --------

random_dict=get_dictionary(train_imagenames,50,100,'Random')
pickle.dump(random_dict,open('../data/dictionaryRandom.pkl', 'wb'))

harris_dict=get_dictionary(train_imagenames,50,100,'Harris')
pickle.dump(random_dict,open('../data/dictionaryHarris.pkl', 'wb'))
# ----------------------------------------------


