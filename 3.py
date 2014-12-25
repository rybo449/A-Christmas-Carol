import csv
import sys
f = open(sys.argv[1])
reader = csv.reader(f)

for i in reader:
	for j in xrange(int(i[1])):
		print i[0],