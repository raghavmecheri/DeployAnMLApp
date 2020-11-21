import pickle
import re
import nltk

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import svm

stop_words = nltk.corpus.stopwords.words('english')
porter = nltk.PorterStemmer()

VECT_PATH = "./app/static/vectorizer.pickle"
CLF_PATH = "./app/static/clf.pickle"

vectorizer, clf = pickle.load(open(VECT_PATH, "rb")), pickle.load(open(CLF_PATH, "rb"))

print("Loaded models up!")

def processRaw(messy_string):
    assert(type(messy_string) == str)
    cleaned = re.sub(r'\b[\w\-.]+?@\w+?\.\w{2,4}\b', 'emailaddr', messy_string)
    cleaned = re.sub(r'(http[s]?\S+)|(\w+\.[A-Za-z]{2,4}\S*)', 'httpaddr',
                     cleaned)
    cleaned = re.sub(r'£|\$', 'moneysymb', cleaned)
    cleaned = re.sub(
        r'\b(\+\d{1,2}\s)?\d?[\-(.]?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}\b',
        'phonenumbr', cleaned)
    cleaned = re.sub(r'\d+(\.\d+)?', 'numbr', cleaned)
    cleaned = re.sub(r'[^\w\d\s]', ' ', cleaned)
    cleaned = re.sub(r'\s+', ' ', cleaned)
    cleaned = re.sub(r'^\s+|\s+?$', '', cleaned.lower())
    
    return ' '.join(
        porter.stem(term) 
        for term in cleaned.split()
        if term not in set(stop_words)
    )

class Predictor():
	def predict(self, message):
		output = clf.predict(vectorizer.transform([processRaw(message)]))
		return output
