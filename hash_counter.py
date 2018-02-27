from collections import Counter
import glob 
import plotly.plotly as py
import plotly.graph_objs as go
import plotly

def hash_count(location):
    dictionary = 'dict.csv'
    c = Counter()
    filter_words = []
    all_files = glob.glob('stop_words/*.txt')
    hash_filter = "stop_words/hash_filter/common_words.txt"
    for files in all_files:

        with open(files) as file:
            for line in file:
                line = line.strip('\n')
                filter_words.append(line)

    with open(hash_filter, 'r') as filter:
        for line in filter:
            line = line.strip('\n')
            filter_words.append(line)

    with open(dictionary, 'r') as file:
        rows = (line.split('\t') for line in file)
        d = {int(row[0]) : row[1:] for row in rows}

#Remove \n in column 5   
    for row in d:
        d[row][5] = d[row][5][:-1]
        #print(d[row][5])
        for tag in d[row][2].split(' '):
            if (d[row][4] != location or d[row][3] == 'Unknown'):
                pass
            else:
                #print(d[row][4], d[row][3], d[row][5])
                tag = tag.strip('#')
                if tag in filter_words or tag == 'torvehallerne' or tag == '':
                    pass
                else:
                    c[tag] += 1
            #break
    location_path = 'data/hash_count/'+location + '_hash.txt'
    with open(location_path, 'w') as file_handler:
        for item in c.most_common(50):
            file_handler.write("{}\n".format(item))
    print(c.most_common(10), '\n')
    tag_name = []
    tag_count = []

    for i in c.most_common(25):

        tag_name.append(i[0])
        tag_count.append(i[1])
    
    data = [go.Bar(x = tag_name, y = tag_count, marker= dict(colorscale='Jet', color = tag_count))]
    layout = go.Layout(title='Most Frequent #Hashtag used for: ' + location,)

    fig = go.Figure(data=data, layout=layout)
    plotly.offline.plot(fig, filename= location + ' barchart.png')


locations = ['valby', 'nørrebro', 'vesterbro', 'amager', 'torvehallerne', 'indreby', 'østerbro']
for location in locations:
    print(location)
    hash_count(location)
