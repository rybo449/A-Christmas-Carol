import sys
import pandas as pd
import csv
#import matplotlib.pyplot as plt

f = open(sys.argv[1])
reader = csv.reader(f)
header = next(reader)
temp = []
c = 0
sriniketh=0
julia=0
sri=[]
jul=[]
sri_df = []
jul_df = []
for i in reader:
	temp.append(i)
	try:
		if i[0]=="Sriniketh Vijayaraghavan":
			sriniketh+=1
			l = 0
			for j in i[3:]:
				l += len(j)
				sri.append(l)
			sri_df.append(i)
		else:
			julia+=1
			l = 0
			for j in i[3:]:
				l+=len(j)
				jul.append(l)
			jul_df.append(i)
	except:
		continue	
	c+=1
df1 = pd.DataFrame(sri_df)
df2 = pd.DataFrame(jul_df)
df1.to_csv(sys.argv[2])
df2.to_csv(sys.argv[3])
print c
print "Number of texts sent by me:",sriniketh,"as opposed to the number of texts sent by Julia:",julia
print "The average length of texts sent by me were:",sum(sri)/float(len(sri))
print "The average length of texts sent by her were:",sum(jul)/float(len(jul))

'''df = pd.DataFrame(temp)
df.columns = header
#df.set_index(['timestamp'])
a = pd.Series([pd.to_datetime(date) for date in df['timestamp']])
df1 = pd.DataFrame(a)
a.plot()
plt.show()'''
#print df.head()
#ticks = df.ix[:, ['Name']]
#ticks.plot(kind = 'bar')
#plt.show()
#df.plot()
#plt.show()
#df = pd.read_csv(sys.argv[1], encoding = 'utf-8')
#print df.head()