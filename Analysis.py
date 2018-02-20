def import_data(location):
    dir_cap = "data/" + location + "/captions.txt"
    dir_full = "data/" + location + "/full_post.txt"
    dir_hash = "data/" + location + "/hashtags.txt"
    id = 0

    d = {}
    with open(dir_full, 'r') as a, open(dir_cap, 'r') as b, open(dir_hash, 'r') as c:
        
        for line_a, line_b, line_c in zip(a, b, c):
            #print(line_a, line_b, line_c)
            line_a = line_a.strip('\n')
            line_b = line_b.strip('\n')
            line_c = line_c.strip('\n')
            d[id] = list()
            d[id].extend((line_a,line_b,line_c))
            id += 1

    
    #skal altid stå nederst
    for key in d.keys():
        pass
       
    

import_data('valby')

