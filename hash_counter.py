from collections import Counter
import glob 
import plotly.plotly as py
import plotly.graph_objs as go
import plotly

py.sign_in('DavidMortensen', 'qxmcmG3FAszaZ8Tf9tyk')

# method to count the hashtag occurence in each area of interest
def hash_count(location):
    # initialize our dict and our counter method along with an empty list we'll fill with filter/stop words
    dictionary = 'dict.csv'
    c = Counter()
    filter_words = []
    all_files = glob.glob('stop_words/*.txt')
    hash_filter = "stop_words/hash_filter/common_words.txt"

    # open each file in our stop words directory one by one, and append the added words to our filter list
    for files in all_files:
        with open(files) as file:
            for line in file:
                line = line.strip('\n')
                filter_words.append(line)

    with open(hash_filter, 'r') as filter:
        for line in filter:
            line = line.strip('\n')
            filter_words.append(line)

    # read in our .csv as a dictionary with a key that's an int between 0-n, and a value that's a list of items with 6 indices.
    with open(dictionary, 'r') as file:
        rows = (line.split('\t') for line in file)
        d = {int(row[0]) : row[1:] for row in rows}

#Remove \n in column 5   
    for row in d:
        d[row][5] = d[row][5][:-1]
        # split our hashtags by space
        for tag in d[row][2].split(' '):
            # condition that requires that we only work with our current location and that filters out all unknown languages
            if (d[row][4] != location or d[row][3] == 'Unknown'):
                pass
            # strips # from the word, and then checks whether or not the tag is in our filter list. If not, count the hashtag.
            else:
                tag = tag.strip('#')
                if tag in filter_words or tag == 'torvehallerne' or tag == '':
                    pass
                else:
                    c[tag] += 1
    # print the 10 most common tags for the current location,
    print(c.most_common(10), '\n')
    # initialize 2 empty lists for our plotting. one containing the name of the tag, and another that'll hold the count of that tag.
    tag_name = []
    tag_count = []
    # append values to each list.
    for i in c.most_common(25):
        tag_name.append(i[0])
        tag_count.append(i[1])
    
    data = [go.Bar(x = tag_name, y = tag_count, marker= dict(colorscale='Jet', color = tag_count))]
    layout = go.Layout(title='Most Frequent #Hashtag used for: ' + location, autosize=False, width=1400, height=1000)

    fig = go.Figure(data=data, layout=layout)
    plotly.offline.plot(fig, filename= location + ' barchart.svg')
    py.image.save_as(fig, filename=location + '_barchart.png')

# locations is the list of areas we want to work with. The for loop below iterates over this list, and makes sure
# we're only working with 1 area at a time.
locations = ['valby', 'nørrebro', 'vesterbro', 'amager', 'torvehallerne', 'indreby', 'østerbro']
for location in locations:
    print(location)
    hash_count(location)
