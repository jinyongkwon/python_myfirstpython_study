import csv

filename = 'down_data/test.csv'

csv_data = []
with open(filename, encoding='utf-8') as f:
    reader = csv.reader(f, delimiter=',', quotechar='"')
    for data in reader:
        csv_data.append(data)

print(csv_data)
