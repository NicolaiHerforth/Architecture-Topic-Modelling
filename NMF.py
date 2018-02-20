from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.decomposition import NMF, LatentDirichletAllocation
from nltk.corpus import stopwords

#Creation of stop words
danish_stop_words = open('danish.txt', 'r')
english_stop_words = open('english.txt', 'r')
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

all_stop_words = map(lambda s: s.strip('\n'), all_stop_words)

def display_topics(model, feature_names, no_top_words):
    for topic_idx, topic in enumerate(model.components_):
        print('Topic %d:' % (topic_idx))
        print(' '.join([feature_names[i]
            for i in topic.argsort()[:-no_top_words - 1:-1]]))

#NMF model
no_topics = 20
tfidf_vectorizer = TfidfVectorizer(max_df = 0.95, min_df = 2, max_features = None, stop_words = all_stop_words)
tfidf = tfidf_vectorizer.fit_transform(full_post)
tfidf_feature_names = tfidf_vectorizer.get_feature_names()
    
nmf = NMF(n_components = no_topics, random_state = 1, alpha = .1, l1_ratio = .5, init = 'nndsvd').fit(tfidf)


#LDA
tf_vectorizer = CountVectorizer(max_df = 0.95, min_df = 2, max_features = None, stop_words = all_stop_words)
tf = tf_vectorizer.fit_transform(full_post)
tf_feature_names = tf_vectorizer.get_feature_names()

lda = LatentDirichletAllocation(n_topics = no_topics, max_iter = 5, learning_method = 'online', learning_offset = 50., random_state = 0).fit(tf)

#Display LDA and NMF
no_top_words = 10
display_topics(nmf, tfidf_feature_names, no_top_words)
display_topics(lda, tf_feature_names, no_top_words)
