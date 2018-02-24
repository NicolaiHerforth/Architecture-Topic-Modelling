import sys
import csv
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.decomposition import NMF, LatentDirichletAllocation

#Creation of stop words
danish_stop_words = open('stop_words/danish.txt', 'r')
english_stop_words = open('stop_words/english.txt', 'r')
places_stop_words = open('stop_words/places.txt', 'r')
other_stop_words = open('stop_words/others.txt', 'r')
place_promotion_stop_words = open('stop_words/place_promotion.txt', 'r')
all_stop_words = []

#Danish
for word in danish_stop_words:
    if word not in all_stop_words:
        all_stop_words.append(word)
    else:
        pass
    
#English
for word in english_stop_words:
    if word not in all_stop_words:
        all_stop_words.append(word)
    else:
        pass
    
#places
for word in places_stop_words:
    if word not in all_stop_words:
        all_stop_words.append(word)
    else:
        pass
    
#others
for word in other_stop_words:
    if word not in all_stop_words:
        all_stop_words.append(word)
    else:
        pass

#place_promotion
for word in place_promotion_stop_words:
    if word not in all_stop_words:
        all_stop_words.append(word)
    else:
        pass

all_stop_words = map(lambda s: s.strip('\n'), all_stop_words)    


#Opening the csv file as dict
with open('dict.csv', 'r') as file:
    rows = (line.split('\t') for line in file)
    d = {int(row[0]) : row[1:] for row in rows}

#Remove \n in column 5    
for row in d:
    d[row][5] = d[row][5][:-1]
    d[row][0] = d[row][0].replace('#','')

def display_topics(model, feature_names, no_top_words):
    for topic_idx, topic in enumerate(model.components_):
        print('Topic %d:' % (topic_idx))
        print(' '.join([feature_names[i]
            for i in topic.argsort()[:-no_top_words - 1:-1]]))

def nmf(area):
#Create list with right specifications
    lst = []
    for row in d:
        if d[row][3] == 'Unknown':
            pass
        else:
            if d[row][4] == area:
                lst.append(d[row][0])
    print('Number of captions in analysis: ', len(lst))
    
#Define no. of topics and words
    no_topics = 20
    no_top_words = 10
    
    tfidf_vectorizer = TfidfVectorizer(max_df = 0.95, min_df = 2, max_features = 1000, stop_words = all_stop_words)
    tfidf = tfidf_vectorizer.fit_transform(lst)
    tfidf_feature_names = tfidf_vectorizer.get_feature_names()
        
    nmf = NMF(n_components = no_topics, random_state = 1, alpha = .1, l1_ratio = .5, init = 'nndsvd').fit(tfidf)
    
    display_topics(nmf, tfidf_feature_names, no_top_words)
    
area = sys.argv[1]
print('Topic modelling: ' + area)
nmf(area)