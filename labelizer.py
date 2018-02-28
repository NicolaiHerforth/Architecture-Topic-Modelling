from nltk import wordpunct_tokenize
from nltk.corpus import stopwords
from afinn import Afinn
import csv

def get_language(caption):
    """
    Categorizing each entry with a language label.
    The label will be either danish, english or unknown.
    """ 

#Splitting text into lowers case words
    words = wordpunct_tokenize(caption)
    words = [word.lower() for word in words]

    languages_dict = {}

    for language in stopwords.fileids():
        stopwords_set = set(stopwords.words(language))
        words_set = set(words)
        common_elements = words_set.intersection(stopwords_set)

        # our actual language 'score'
        languages_dict[language] = len(common_elements) 

    most_rated_language = str(max(languages_dict, key = languages_dict.get))
    if most_rated_language != 'english' and most_rated_language != 'danish':
        most_rated_language = 'Unknown'

    return most_rated_language

def sentiment(sentence, language):
    """
    Requires afinn: "pip install afinn"
    Uses Danish made Afinn module to perform sentiment analysis on a word or sentence.
    Returns sentiment label: Positive, Neutral or Negative for given input.
    """
    if language == 'english':
        afinn = Afinn(language = 'en')

        if afinn.score(sentence) > 0:
            return "positive"
        elif afinn.score(sentence) == 0:
            return "neutral"
        else:
            return "negative"
    else:
        afinn = Afinn(language = 'da')

        if afinn.score(sentence) > 0:
            return "positive"
        elif afinn.score(sentence) == 0:
            return "neutral"
        else:
            return "negative"


def import_data(locations):
    """
    Imports the data from each location into a dictionary of lists.
    The dictionary will have the following indexing parameters:
    key = unique id for entry
    d[key][list_index]
    List index values are:
    0 = full text
    1 = caption
    2 = hashtags
    3 = language (DA, EN, unknown)
    4 = location
    5 = sentiment label (Positive, Negative, Neutral)
    """

    id = 0
    d = {}
    for location in locations:
        # open the 3 different dirs for full_post, the caption only and the hashtags only
        dir_cap = "data/" + location + "/captions.txt"
        dir_full = "data/" + location + "/full_post.txt"
        dir_hash = "data/" + location + "/hashtags.txt"
        print('Currently working ', location)

        with open(dir_full, 'r') as a, open(dir_cap, 'r') as b, open(dir_hash, 'r') as c:
            # read line in each of the files by using labeling conventions above
            for line_a, line_b, line_c in zip(a, b, c):
                line_a = line_a.strip('\n')
                line_a_no_hash = line_a.replace('#','')
                line_b = line_b.strip('\n')
                line_c = line_c.strip('\n')
                # apply language detection and sentiment analysis on the full post
                lang = get_language(line_a_no_hash)
                senti = sentiment(line_a_no_hash, lang)
                # create a list to each key extended by the items stated above
                d[id] = list()
                d[id].extend((line_a,line_b,line_c, lang, location, senti))
                id += 1


    # dict export to .csv file with tab as delimiter
    with open('dict.csv', 'w') as csv_file:
        writer = csv.writer(csv_file, delimiter='\t')

        for key, value in d.items():
            writer.writerow([key,value[0],value[1],value[2],value[3],value[4],value[5]])
    print('JOBS DONE!')

# call our function on desired locations    
locations = ['valby', 'nørrebro', 'vesterbro', 'amager', 'torvehallerne', 'indreby', 'østerbro']
import_data(locations)
