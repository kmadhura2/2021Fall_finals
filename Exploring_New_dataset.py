import pandas as pd
import numpy as np
from scipy.stats import skew
import matplotlib.pyplot as plt

def data(data_merge):
    for location in data_merge.index:
        data_merge['Asthma'][location] = (data_merge['Asthma'][location] * data_merge['Population'][location]) / 100
    data_merge.insert(5, 'Metric', '0.0')
    skewed_data=data_merge.skew(axis=0, skipna=True)
    quantile_50=data_merge.quantile(0.5, axis = 0)
    quantile_100 = data_merge.quantile(1.0, axis=0)
    quantile_75=data_merge.quantile(0.75, axis=0)
    print(quantile_50)
    print(quantile_75)
    print(quantile_100)
    data_merge['Metric'] = data_merge['Metric'].astype(float)
    for i, row in data_merge.iterrows():
        sum=0
        if (row[2] >= quantile_75[2] and row[4] >= quantile_75[4] and row[0] >= quantile_75[0]) or \
                (quantile_50[2]<=row[2]<quantile_75[2] and quantile_50[4]<=row[4]<quantile_75[4] and
                 quantile_50[0]<=row[0]<quantile_75[0]) or (row[2]<quantile_50[2] and row[4]<quantile_50[4]and row[0]<quantile_50[0]):
            sum = +3
        elif (row[2]<quantile_50[2] and quantile_50[4]<=row[4]<quantile_75[4] and quantile_50[0]<=row[0]<quantile_75[0]) \
            or (quantile_50[2]<=row[2]<quantile_75[2] and row[4]>quantile_75[4] and row[0]>=quantile_75[0]):
            sum=+3.25
        elif(row[2] >= quantile_75[2] and row[4] >= quantile_75[4] and quantile_50[0] <= row[0] < quantile_75[0]) or \
            (quantile_50[2]<=row[2]<quantile_75[2] and quantile_50[4]<=row[4]<quantile_75[4] and row[0]<quantile_50[0]):
            sum=+2.75
        elif (row[2]>=quantile_75[2] and quantile_50[4]<=row[4]<quantile_75[4] and row[0]>=quantile_75[0]) or \
                (quantile_50[2]<=row[2]<quantile_75[2] and row[4]<quantile_50[4] and quantile_50[0]<=row[0]<quantile_75[0]):
            sum=+2.5
        elif (row[2]>=quantile_75[2] and quantile_50[4]<=row[4]<quantile_75[4] and quantile_50[0]<=row[0]<quantile_75[0]) or \
                (quantile_50[2]<=row[2]<quantile_75[2] and row[4]>=quantile_75[4] and row[0]>=quantile_75[0]):
            sum=+2.0
        elif (row[2] >= quantile_75[2] and row[4]<quantile_50[4]  and row[0] >= quantile_75[0]):
            sum=+2.25
        elif row[2]<quantile_50[2] and row[4]>=quantile_75[2] and quantile_50[0]<=row[0]<quantile_75[0]:
            sum=+0.5
        elif row[2]<quantile_50[2] and row[4]>=quantile_75[2] and quantile_50[0]<row[0]:
            sum=+0.75
        elif row[2]>=quantile_75[2] and quantile_50[4]<=row[4]<quantile_75[4] and row[0]<quantile_50[0]:
            sum=-0.5
        elif quantile_50[2]<=row[2]<quantile_75[2] and row[4]>=quantile_75[4] and row[0]<quantile_50[0]:
           sum=+1
        elif row[2]<quantile_50[2] and quantile_50[4]<=row[4]<quantile_75[4] and row[0]>=quantile_75[0]:
            sum=+1.5
        elif quantile_50[2]<=row[2]<quantile_75[2] and row[4]<quantile_50[4] and row[0]>=quantile_75[0]:
            sum=-0.25
        elif row[2]>=quantile_75[2] and row[4]<quantile_50[4] and quantile_50[0]<=row[0]<quantile_75[0]:
            sum=+1.25
        elif row[2] >= quantile_75[2] and row[4] >= quantile_75[4] and row[0] < quantile_50[0]:
            sum=-1
        elif row[2]>= quantile_75[2] and row[4] < quantile_50[4] and row[0] < quantile_50[0]:
            sum=-0.75
        elif row[2]<quantile_50[2] and row[4]>=quantile_75[4] and row[0]>=quantile_75[0]:
            sum=-2
        elif row[2]<quantile_50[2] and row[4]<quantile_50[4] and row[0]>=quantile_75[0]:
            sum=-3
        elif row[2]<quantile_50[2] and row[4]<quantile_50[4] and quantile_50[0]<=row[0]<quantile_75[0]:
            sum=-2.5


        row[5]=sum
    print(data_merge.sort_values(by=['Population'], inplace=False))
    print(data_merge[['Population','Asthma', 'Population_Density']])
    plt.figure(figsize=(8,5))
    plt.plot(data_merge.index, data_merge.Asthma, 'blue', label="Asthma")
    plt.plot(data_merge.index, data_merge.Population_Density,'green', label="Population_Density")
    plt.title('Population VS Asthma')
    plt.ylabel('Number of persons')
    plt.legend()
    plt.show()

if __name__ == '__main__':
    df=pd.read_csv('Datasets/DATA.csv')
    data(df)

