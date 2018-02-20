def import_data(location):
    dir = "instaloader/#" + location + "/*.txt"

    with open("hashtags.txt") as file:
        i = 0
        for line in file:
            i += 1
            d[key[i]] = val[line]

import_data(valby)