from pandas import DataFrame, read_csv
from numpy import random

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

import Functions

print 'Pandas version ' + pd.__version__

names = ['Bob', 'Jessica', 'Mary', 'John', 'Mel']
births = [968,155,77,578,973]

BabyDataSet = zip(names,births)

print BabyDataSet

df = DataFrame(data = BabyDataSet, columns = ['Names','Births'])

df

##---class 2

random.seed(500)

random_names = [names[random.randint(low=0,high=len(names))] for i in range(1000)]

print random_names[:10]

births = [random.randint(low=0,high=1000) for i in range(1000)]

print births[:10]

BabyDataSet = zip(random_names,births)

print BabyDataSet[:10]

df = DataFrame(data=BabyDataSet, columns = ["Names","Births"])

print df[:10]

df.to_csv('births1880.txt',index=False,header=False)

Location = r'births1880.txt'

df = read_csv(Location)

print df

print df.head()

df = read_csv(Location,header=None)

print df

print df.tail()

df = read_csv(Location, names = ['Names','Births'])

print df.head()

import os

os.remove(Location)

print df['Names'].unique()

for x in df['Names'].unique():
    print x

print df['Names'].describe()

Name = df.groupby(df['Names'])

df = Name.sum()

print df

Sorted = df.sort(['Births'], ascending=0)
print Sorted.head(1)

print df['Births'].max()

df['Births'].plot()

MaxValue = df['Births'].max()

MaxName = df[df['Births']==df['Births'].max()].index[0]

Text = str(MaxValue) + " - " + MaxName

plt.annotate(Text, xy=(1,MaxValue), xytext=(8,0), xycoords=('axes fraction','data'), textcoords='offset points')

print "The most popular name"

print df[df['Births'] == df['Births'].max()]

plt.show()

##--Class 3

dataset = Functions.CreatDataSet(4)
df = DataFrame(data=dataset, columns=['State','Status','CustomerCount','StatusDate'])
print df

df.to_excel('Lesson3.xlsx', index=False)
print 'Done'

