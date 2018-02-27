import glob
import sys
import re
import os
import errno
from nltk.tokenize import TweetTokenizer
from nltk import wordpunct_tokenize
from nltk.corpus import stopwords
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
    """
    Reading in scraped data and structuring into a dict.
    Seperating required fields values. Also applies emoji extract.
    """
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
    
 

tagname = sys.argv[1]
print('Trying to read directory: #' + tagname)
read_data(tagname)