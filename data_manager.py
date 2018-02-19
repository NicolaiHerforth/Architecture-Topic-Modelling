import glob 
import sys
import re

def read_data(tagname):
    # defining the directory we want to open
    dir = "instaloader/#" + tagname + "/*.txt"
    # listing all files in dir
    all_files = glob.glob(dir)
    if len(all_files) == 0:
        raise RuntimeError('#' + tagname + ' directory does not exist!')
    data_list, captions, hashtags, full_post = [], [], [], []

    print('#' + tagname + ' contains', len(all_files), 'files.')

    # open file by file and store that data, then close file.
    for file in all_files:
        opened_file = open(file, 'r')
        data = opened_file.read()
        data_list.append(data)
        opened_file.close()

    # reading caption by caption and recognizing each word in the capion. if the word contains # it goes into
    # the hashtags, else it goes into captions
    for i in data_list: 
        # creating an empty string for each post, ready to be filled with the content of the post
        current_caption = ""
        current_hashtags = ""
        current_full_post = ""
        
        for word in i.split(' '):
            if '#' in word:
                # adding the hashtags from the current post, to the hashtag string
                current_hashtags += word + ' '
            else:
                # adding the caption text from the current post, to the caption string
                current_caption += word + ' '

            # removing emojis from text
        emoji_pattern = re.compile("["
                            u"\U0001F600-\U0001F64F"
                            u"\U0001F300-\U0001F5FF"
                            u"\U0001F680-\U0001F6FF"
                            u"\U0001F1E0-\U0001F1FF"
                            "]+", flags=re.UNICODE)
        current_caption = emoji_pattern.sub(r'', current_caption)
        current_hashtags = emoji_pattern.sub(r'', current_hashtags)

        #remove \n and #
        
        current_caption = current_caption.replace('\n',' ')
        current_hashtags = current_hashtags.replace('\n',' ')
        current_full_post += current_caption + current_hashtags

        current_hashtags = current_hashtags.replace('#','')
        # append the original lists with the string we just created.
        hashtags.append(current_hashtags)
        captions.append(current_caption)
        full_post.append(current_full_post)

    
    


hashtag_name = sys.argv[1]
print('Trying to read directory: #' +hashtag_name)
read_data(hashtag_name)


    # check whether or not a file is containing \n for newline.
# newline_files = 0
# for i in random_list:
#     if '\n' in i and count < 1:
#         newline_files += 1

# print(newline_files)