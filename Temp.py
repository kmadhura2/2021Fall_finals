import pandas as pd
import numpy as np
from scipy.stats import skew

df= pd.read_csv('Datasets/basic_info.csv')
index=df.index
list1=[]
for i in index:
    if i ==0:
    print(df['Median AQI'])
#print(skew(df['Median AQI']))
