import glob 

all_files = glob.glob("instaloader/#valby/*.txt")
count = 0
random_list = []
print(len(all_files))
for file in all_files:
    with open(file) as f:
        for line in f:
            random_list.append(str(line))


print(random_list)
print(len(random_list))