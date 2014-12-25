import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
import sys


#pd.set_option('display.mpl_style', 'default')
#pd.set_option('display.width', 5000) 
#pd.set_option('display.max_columns', 60)


df = pd.read_csv(sys.argv[1])
df['timestamp'] = pd.to_datetime(df['timestamp'], format = "%m/%d/%Y %H:%M:%S %p")
#print df.head()
df = df[df['timestamp']> "2000-01-01 00:00:00"]
df['timestamp'] = df['timestamp'].apply(lambda x: x.strftime('%m-%d-%Y'))
#print df.head()
#data = df['timestamp']
data = df.groupby(['timestamp']).size().reset_index()
print data.head()

fields = ['Message Count']
data1 = data.set_index('timestamp')
data1.columns = fields
print data1.head()
data1.plot()
plt.ylabel('Number of Messages')
plt.title('Total Messages')
plt.savefig('Total Messages.png')
plt.show()