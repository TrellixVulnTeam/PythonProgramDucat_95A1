#To copy CSV file
import csv
with open('sample.csv', 'r') as readFile:
	reader = csv.reader(readFile)
	lines = list(reader)
	print(lines)	
with open('sample1.csv', 'w') as writeFile:
    writer = csv.writer(writeFile)
    writer.writerows(lines)
