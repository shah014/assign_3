import csv
filename = [('name', 'address', 'age'), ('George', '4312 Abbey Road', 22), ('John', '54 Love Ave', 21)]
csvfile = open('filename.csv', 'w', newline='')
obj = csv.writer(csvfile)
for row in filename:
    obj.writerow(row)
csvfile.close()