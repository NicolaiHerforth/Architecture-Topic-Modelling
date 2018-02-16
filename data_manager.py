import glob 
import sys

def read_data(tagname):
    # defining the directory we want to open
    dir = "instaloader/#" + tagname + "/*.txt"
    #   listing all files in dir
    all_files = glob.glob(dir)
    if len(all_files) == 0:
        raise RuntimeError('#' + hashtag + ' does not exist!')
    data_list = []

    print('#' + hashtag + ' contains', len(all_files), 'files.')
    # then open file by file and store that data, then close file.
    for file in all_files:
        opened_file = open(file, 'r')
        data = opened_file.read()
        data_list.append(data)
        opened_file.close()

hashtag = sys.argv[1]
print('Trying to read directory: #' +hashtag)
read_data(hashtag)

    # check whether or not a file is containing \n for newline.
# newline_files = 0
# for i in random_list:
#     if '\n' in i and count < 1:
#         newline_files += 1

# print(newline_files)