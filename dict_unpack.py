with open('dict.csv', 'r') as file:
    rows = (line.split('\t') for line in file)
    d = {int(row[0]) : row[1:] for row in rows}
    
for row in d:
    d[row][5] = d[row][5][:-1]

print(d[0])