import sys
import pandas as pd
import csv
from nltk.corpus import stopwords
import operator

stop = stopwords.words('english')
#print stop
f = open(sys.argv[1])
reader = csv.reader(f)
sriniketh_tokens = {}
julia_tokens = {}
for i in reader:
	try:
		if i[0] == "Sriniketh Vijayaraghavan":
			for j in i[3:]:
				#print j
				for k in j.split():
					count = sriniketh_tokens.setdefault(k , 0)
					sriniketh_tokens[k] = count + 1

		else:
			for j in i[3:]:
				#print j
				for k in j.split():
					count = julia_tokens.setdefault(k , 0)
					julia_tokens[k] = count + 1
	except:
		continue
#s_tokens = sorted(sriniketh_tokens.items(), key = operator.itemgetter(1), reverse = True)
#print s_tokens[:10]
s = []
for i in julia_tokens.keys():
	if i not in stop:
		s.append([i,julia_tokens[i]])
s1 = sorted(s, key = operator.itemgetter(1), reverse = True)
s2 = []
for i in s1:
	if len(i[0])>6:
		s2.append(i)
for i in xrange(100):
	print s2[i][0],",",s2[i][1]
#print s2[:100]					