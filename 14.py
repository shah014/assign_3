import csv


def csv_read():
    with open("filename.csv", 'r') as file:
        for line in csv.DictReader(file):
            print(dict(line))


csv_read()

