import glob
import sys
import re
import os
import errno
from nltk.tokenize import TweetTokenizer
import emoji
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.decomposition import NMF, LatentDirichletAllocation


def extract_emojis(str):
    string = str
    for c in string:
        if c in emoji.UNICODE_EMOJI:
            string = string.replace(c,'')
    return string

def read_data(tagname):
    # defining the directory we want to open
    dir = "instaloader/#" + tagname + "/*.txt"
    tknzr = TweetTokenizer()
    # listing all files in dir
    all_files = glob.glob(dir)
    if len(all_files) == 0:
        raise RuntimeError('#' + tagname + ' directory does not exist!')
    data_list, captions, hashtags = [], [], []

    print('#' + tagname + ' contains', len(all_files), 'files.')

    # open file by file and store that data, then close file.
    for file in all_files:
        opened_file = open(file, 'r')
        data = opened_file.read()
        data = data.replace('\n',' ')
        data = extract_emojis(data)
        data_list.append(data)
        opened_file.close()

    # reading caption by caption and recognizing each word in the capion. if the word contains # it goes into
    # the hashtags, else it goes into captions
    for i in data_list: 

        # creating an empty string for each post, ready to be filled with the content of the post
        current_caption = ""
        current_hashtag = ""

        for word in i.split(' '):
            if '#' in word:
                # adding the hashtags from the current post, to the hashtag string
                current_hashtag += word + ' '

            else:
                # adding the caption text from the current post, to the caption string
                current_caption += word + ' '
        
        # append the original lists with the string we just created.
        captions.append(current_caption)
        hashtags.append(current_hashtag)



    # export part of the script. It exports the 3 lists into 3 files.
    caption_path = 'data/' + tagname + '/captions.txt'
    hashtag_path = 'data/' + tagname + '/hashtags.txt'
    fullpost_path = 'data/' + tagname + '/full_post.txt'


    # create a data directory with a tagname subdir.
    # if they already exists, it will report so.

    os.system("mkdir data")
    os.system("mkdir data/" + tagname)

    with open(caption_path, 'w') as file_handler:
        for item in captions:
            file_handler.write("{}\n".format(item))
    
    with open(hashtag_path, 'w') as file_handler:
        for item in hashtags:
            file_handler.write("{}\n".format(item))
    
    with open(fullpost_path, "w") as file_handler:
        for item in data_list:
            file_handler.write("{}\n".format(item))
    
 
    ############### EXPORT BELOW DOCSTRING TO SEPERATE SCRIPTS!! ###############


    """

    def display_topics(model, feature_names, no_top_words):
    for topic_idx, topic in enumerate(model.components_):
        print('Topic %d:' % (topic_idx))
        print(' '.join([feature_names[i]
            for i in topic.argsort()[:-no_top_words - 1:-1]]))

    no_topics = 20
    tfidf_vectorizer = TfidfVectorizer(max_df = 0.95, min_df = 2, max_features = None, stop_words = all_stop_words)
    tfidf = tfidf_vectorizer.fit_transform(data_list)
    tfidf_feature_names = tfidf_vectorizer.get_feature_names()
    
    nmf = NMF(n_components = no_topics, random_state = 1, alpha = .1, l1_ratio = .5, init = 'nndsvd').fit(tfidf)
    no_top_words = 10
    display_topics(nmf, tfidf_feature_names, no_top_words)


    count = Counter(hashtags)
    common = count.most_common(40)
    for key, value in common:
        print(key, '=', value)


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
"""

tagname = sys.argv[1]
print('Trying to read directory: #' + tagname)
read_data(tagname)