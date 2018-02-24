import sys

def unpack(dictionary):
    """
    Unpacks dict from csv file. The dictionary will have the following indexing parameters:
    key = unique id for entry
    val0 = full text
    val1 = caption
    val2 = hashtags
    val3 = language (DA, EN, unknown)
    val4 = location
    val5 = sentiment label (pos, neg, neu)
    """

    with open(dictionary, 'r') as file:
        rows = (line.split('\t') for line in file)
        d = {int(row[0]) : row[1:] for row in rows}

    #Remove \n in column 5        
    for row in d:
        d[row][5] = d[row][5][:-1]
    
    count = 0
    for row in d:
        count += 1
    print(count)
         
dictionary = sys.argv[1]
print('Unpacking dictionary: ' + dictionary)
unpack(dictionary)