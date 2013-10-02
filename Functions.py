import pandas as pd
import numpy as np

def CreatDataSet(Number = 1):
    Output = []

    for i in range(Number):
        rng = pd.date_range(start='1/1/2009',end='12/31/2012',freq='W@MON')
    	data = np.random.randint(low=25,high=1000,size=len(rng))
        status = [1,2,3]
	np.random.seed(i)
	random_status = [status[np.random.randint(low=0,high=len(status))] for i in range(len(rng))]
	states = ['GA','FL','fl','NY','NJ','TX']
	random_states = [states[np.random.randint(low=0,high=len(states))] for i in range(len(rng))]
	Output.extend(zip(random_states,random_status,data,rng))
    return Output
