import sys
import glob 
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.decomposition import NMF, LatentDirichletAllocation


#Stop words
filter_words = []

all_files = glob.glob('stop_words/*.txt')

for files in all_files:
    with open(files) as file:
        for line in file:
            line = line.strip('\n')
            filter_words.append(line)

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
    no_top_words = 5
    
    tfidf_vectorizer = TfidfVectorizer(max_df = 0.95, min_df = 2, max_features = 1000, stop_words = filter_words)
    tfidf = tfidf_vectorizer.fit_transform(lst)
    tfidf_feature_names = tfidf_vectorizer.get_feature_names()
        
    nmf = NMF(n_components = no_topics, random_state = 1, alpha = .1, l1_ratio = .5, init = 'nndsvd').fit(tfidf)
    
    display_topics(nmf, tfidf_feature_names, no_top_words)
    
area = sys.argv[1]
print('Topic modelling: ' + area)
nmf(area)