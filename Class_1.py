from pandas import DataFrame, read_csv

import matplotlib.pyplot as plt
import pandas as pd

print 'Pandas version ' + pd.__version__

names = ['Bob', 'Jessica', 'Mary', 'John', 'Mel']
births = [968,155,77,578,973]

BabyDataSet = zip(names,births)

print BabyDataSet

df = DataFrame(data = BabyDataSet, columns = ['Names','Births'])

df
