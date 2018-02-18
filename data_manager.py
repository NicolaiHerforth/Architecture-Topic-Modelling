import glob 
import sys
import re

def read_data(tagname):
    # defining the directory we want to open
    dir = "instaloader/#" + tagname + "/*.txt"
    # listing all files in dir
    all_files = glob.glob(dir)
    if len(all_files) == 0:
        raise RuntimeError('#' + hashtag_name + ' directory does not exist!')
    data_list, captions, hashtags = [], [], []

    print('#' + hashtag_name + ' contains', len(all_files), 'files.')

    # open file by file and store that data, then close file.
    for file in all_files:
        opened_file = open(file, 'r')
        data = opened_file.read()
        data_list.append(data)
        opened_file.close()
    
    # reading caption by caption and recognizing each word in the capion. if the word contains # it goes into
    # the hashtags, else it goes into captions
    for i in data_list: 
        for word in i.split(' '):
            if '#' in word:
                hashtags.append(word)
            else:
                captions.append(word)
        
    # create a caption and a hashtag text joined by all the words collected, removing \n and # in the respective texts.
    caption_text = ' '.join(captions).replace('\n',' ')
    hashtag_text = ' '.join(hashtags).replace('\n', ' ').replace('#', '')

    # removing emojis from text
    emoji_pattern = re.compile("["
                           u"\U0001F600-\U0001F64F"  
                           u"\U0001F300-\U0001F5FF"
                           u"\U0001F680-\U0001F6FF"
                           u"\U0001F1E0-\U0001F1FF"
                           "]+", flags=re.UNICODE)
    caption_text = emoji_pattern.sub(r'', caption_text)
    hashtag_text = emoji_pattern.sub(r'', hashtag_text)
    


hashtag_name = sys.argv[1]
print('Trying to read directory: #' +hashtag_name)
read_data(hashtag_name)


    # check whether or not a file is containing \n for newline.
# newline_files = 0
# for i in random_list:
#     if '\n' in i and count < 1:
#         newline_files += 1

# print(newline_files)