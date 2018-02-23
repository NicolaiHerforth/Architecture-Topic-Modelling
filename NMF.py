import sys
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.decomposition import NMF, LatentDirichletAllocation

def display_topics(model, feature_names, no_top_words):
    for topic_idx, topic in enumerate(model.components_):
        print('Topic %d:' % (topic_idx))
        print(' '.join([feature_names[i]
            for i in topic.argsort()[:-no_top_words - 1:-1]]))

#Creation of stop words
danish_stop_words = open('danish.txt', 'r')
english_stop_words = open('english.txt', 'r')
other_stop_words = open('others.txt', 'r')
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
    
#others
for word in other_stop_words:
    if word not in all_stop_words:
        all_stop_words.append(word)
    else:
        pass
print(len(all_stop_words))

all_stop_words = map(lambda s: s.strip('\n'), all_stop_words)    
    
def nmf(tagname):
    dir = "data/" + tagname + "/full_post.txt"
    full_post = open(dir, 'r')
       
    #NMF model
    no_topics = 50
    no_top_words = 10
    
    tfidf_vectorizer = TfidfVectorizer(max_df = 0.95, min_df = 2, max_features = None, stop_words = all_stop_words)
    tfidf = tfidf_vectorizer.fit_transform(full_post)
    tfidf_feature_names = tfidf_vectorizer.get_feature_names()
        
    nmf = NMF(n_components = no_topics, random_state = 1, alpha = .1, l1_ratio = .5, init = 'nndsvd').fit(tfidf)
    
    display_topics(nmf, tfidf_feature_names, no_top_words)
    
tagname = sys.argv[1]
print('NMF analysis of: ' + tagname)
nmf(tagname)