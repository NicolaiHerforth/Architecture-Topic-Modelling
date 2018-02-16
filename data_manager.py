import glob 
import sys

def read_data(tagname):
    dir = "instaloader/#" + tagname + "/*.txt"
    all_files = glob.glob(dir)
    if len(all_files) == 0:
        raise RuntimeError('#' + hashtag + ' does not exist!')
    count = 0
    data_list = []
    print(len(all_files))
    for file in all_files:
        opened_file = open(file, 'r')
        data = opened_file.read()
        #data.strip('\n')
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