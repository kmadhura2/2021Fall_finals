import pandas as pd
import numpy as np
from scipy.stats import skew
import matplotlib.pyplot as plt

def data(data_merge):
    for index in data_merge.index:
        data_merge['Asthma'][index] = (data_merge['Asthma'][index] * data_merge['Population'][index]) / 100
        data_merge['Air Pollution'][index] = (data_merge['Air Pollution'][index] * data_merge['Population'][index]) / 100
        data_merge['Smoking'][index] = (data_merge['Smoking'][index] * data_merge['Population'][index]) / 100

    data_merge.insert(5, 'Metric', '0.0')
    skewed_data=data_merge.skew(axis=0, skipna=True)
    print(skewed_data)
    quantile_50=data_merge.quantile(0.5, axis = 0)
    quantile_75=data_merge.quantile(0.75, axis=0)
    #print(quantile_50)
    #print(quantile_75)
    data_merge['Metric'] = data_merge['Metric'].astype(float)
    for row in data_merge.iterrows():
        sum=0
        if (row[4] >= quantile_75[4] and row[5] >= quantile_75[5] and row[2] >= quantile_75[2]) or \
                (quantile_50[4]<=row[4]<quantile_75[4] and quantile_50[5]<=row[5]<quantile_75[4] and
                 quantile_50[2]<=row[2]<quantile_75[2]) or (row[4]<quantile_50[4] and row[5]<quantile_50[5]and \
                                                            row[2]<quantile_50[2]):
            sum = +3
        elif (row[4]<quantile_50[4] and quantile_50[5]<=row[5]<quantile_75[5] and quantile_50[2]<=row[2]<quantile_75[2]) \
            or (quantile_50[4]<=row[4]<quantile_75[4] and row[5]>quantile_75[5] and row[2]>=quantile_75[2]):
            sum=+3.25
        elif(row[4] >= quantile_75[4] and row[5] >= quantile_75[5] and quantile_50[2] <= row[2] < quantile_75[2]) or \
            (quantile_50[4]<=row[4]<quantile_75[4] and quantile_50[5]<=row[5]<quantile_75[5] and row[2]<quantile_50[2]):
            sum=+2.75
        elif (row[4]>=quantile_75[4] and quantile_50[5]<=row[5]<quantile_75[5] and row[2]>=quantile_75[2]) or \
                (quantile_50[4]<=row[4]<quantile_75[4] and row[5]<quantile_50[5] and quantile_50[2]<=row[2]<quantile_75[2]):
            sum=+2.5
        elif (row[4]>=quantile_75[4] and quantile_50[5]<=row[5]<quantile_75[5] and quantile_50[2]<=row[2]<quantile_75[2]) or \
                (quantile_50[4]<=row[4]<quantile_75[4] and row[5]>=quantile_75[5] and row[2]>=quantile_75[2]):
            sum=+2.0
        elif row[4] >= quantile_75[4] and row[5]<quantile_50[5]  and row[2] >= quantile_75[2]:
            sum=+2.25
        elif row[4]<quantile_50[4] and row[5]>=quantile_75[5] and quantile_50[2]<=row[2]<quantile_75[2]:
            sum=+0.5
        elif row[4]<quantile_50[4] and row[5]>=quantile_75[5] and quantile_50[2]<row[2]:
            sum=+0.75
        elif row[4]>=quantile_75[4] and quantile_50[5]<=row[5]<quantile_75[5] and row[2]<quantile_50[2]:
            sum=-0.5
        elif quantile_50[4]<=row[4]<quantile_75[4] and row[5]>=quantile_75[5] and row[2]<quantile_50[2]:
           sum=+1
        elif row[4]<quantile_50[4] and quantile_50[5]<=row[5]<quantile_75[5] and row[2]>=quantile_75[2]:
            sum=+1.5
        elif quantile_50[4]<=row[4]<quantile_75[4] and row[5]<quantile_50[5] and row[2]>=quantile_75[2]:
            sum=-0.25
        elif row[4]>=quantile_75[4] and row[5]<quantile_50[5] and quantile_50[2]<=row[2]<quantile_75[2]:
            sum=+1.25
        elif row[4] >= quantile_75[4] and row[5] >= quantile_75[5] and row[2] < quantile_50[2]:
            sum=-1
        elif row[4]>= quantile_75[4] and row[5] < quantile_50[5] and row[2] < quantile_50[2]:
            sum=-0.75
        elif row[4]<quantile_50[4] and row[5]>=quantile_75[5] and row[2]>=quantile_75[2]:
            sum=-2
        elif row[4]<quantile_50[4] and row[5]<quantile_50[5] and row[2]>=quantile_75[2]:
            sum=-3
        elif row[4]<quantile_50[4] and row[5]<quantile_50[5] and quantile_50[2]<=row[2]<quantile_75[2]:
            sum=-2.5

        row[6]=sum
        if (row[6] == 3.25 and row[1] >= quantile_75[1] and row[3] >= quantile_75[3]) or \
                (row[6] == 3.25 and row[1] < quantile_50[1] and row[3] < quantile_50[3]) or \
                (row[6] == 3.25 and quantile_50[1] <= row[1] < quantile_75[1] and quantile_50[3] <= row[3] <
                 quantile_75[3]):
            row[6] += 1.75
        elif (row[6] == 3.25 and quantile_50[1] <= row[1] < quantile_75[1] and row[3] >= quantile_75[3]) or \
                (row[6] == 3.25 and quantile_50[2] <= row[3] < quantile_75[3] and row[1] >= quantile_75[1]):
            row[6] += 1.5
        elif (row[6] == 3.25 and quantile_50[1] <= row[1] < quantile_75[1] and row[3] < quantile_50[3]) or \
                (row[6] == 3.25 and quantile_50[3] <= row[3] < quantile_75[3] and row[1] < quantile_50[1]):
            row[6] += 1.25
        elif (row[6] == 3.25 and row[1] >= quantile_75[1] and row[3] < quantile_50[3]) or \
                (row[5] == 3.25 and row[3] >= quantile_75[3] and row[1] < quantile_50[1]):
            row[6] += 1

        elif (row[6] == 3.0 and row[1] >= quantile_75[1] and row[3] >= quantile_75[3]) or \
                (row[6] == 3.0 and row[1] < quantile_50[1] and row[3] < quantile_50[3]) or \
                (row[6] == 3.0 and quantile_50[1] <= row[1] < quantile_75[1] and quantile_50[3] <= row[3] < quantile_75[
                    2]):
            row[6] += 1.75
        elif (row[6] == 3.0 and quantile_50[1] <= row[1] < quantile_75[1] and row[3] >= quantile_75[3]) or \
                (row[6] == 3.0 and quantile_50[3] <= row[3] < quantile_75[3] and row[1] >= quantile_75[1]):
            row[6] += 1.5
        elif (row[6] == 3.0 and quantile_50[1] <= row[1] < quantile_75[1] and row[3] < quantile_50[3]) or \
                (row[6] == 3.0 and quantile_50[3] <= row[3] < quantile_75[3] and row[1] < quantile_50[1]):
            row[6] += 1.25
        elif (row[6] == 3.0 and row[1] >= quantile_75[1] and row[3] < quantile_50[3]) or \
                (row[6] == 3.0 and row[3] >= quantile_75[3] and row[1] < quantile_50[1]):
            row[6] += 1
        
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

