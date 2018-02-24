from collections import Counter
import glob 

def hash_count(location):
    dictionary = 'dict.csv'
    c = Counter()
    filter_words = []
    all_files = glob.glob('stop_words/*.txt')
    for files in all_files:

        with open(files) as file:
            for line in file:
                line = line.strip('\n')
                filter_words.append(line)
    #print(filter_words)


    with open(dictionary, 'r') as file:
        rows = (line.split('\t') for line in file)
        d = {int(row[0]) : row[1:] for row in rows}

    #Remove \n in column 5    
    for row in d:
        d[row][5] = d[row][5][:-1]
        for tag in d[row][2].split(' '):
            if d[row][4] != location and d[row][3] == 'Unknown':
                pass
            else:
                tag = tag.strip('#')
                if tag in filter_words or tag == 'torvehallerne' or tag == '':
                    pass
                else:
                    c[tag] += 1

    location_path = 'data/hash_count/'+location + '_hash.txt'
    with open(location_path, 'w') as file_handler:
        for item in c.most_common(50):
            file_handler.write("{}\n".format(item))
    print(c.most_common(10))

locations = ['valby', 'nørrebro', 'vesterbro', 'amager', 'torvehallerne', 'indreby', 'østerbro']
for location in locations:
    hash_count(location)