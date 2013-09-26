from pandas import DataFrame, read_csv
from numpy import random

import matplotlib.pyplot as plt
import pandas as pd

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
