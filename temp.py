import pandas as pd

import matplotlib.pyplot as plt

def data(data_merge):

    print(data_merge)
    for index in data_merge.index:
       data_merge['Air Pollution'][index] = (data_merge['Air Pollution'][index] * data_merge['Population'][index]) / 100
       data_merge['Smoking'][index] = (data_merge['Smoking'][index] * data_merge['Population'][index]) / 100
       data_merge['Asthma'][index] = (data_merge['Asthma'][index] * data_merge['Population'][index]) / 100
    corr_mat=data_merge.corr()
    print(corr_mat)
    data_merge.insert(5, 'Metric', '0.0')
    skewed_data = data_merge.skew(axis=0, skipna=True)
    #print(skewed_data)
    quantile_50 = data_merge.quantile(0.5, axis=0)
    quantile_75 = data_merge.quantile(0.75, axis=0)
    print(quantile_50)
    print(quantile_75)
    data_merge['Metric'] = data_merge['Metric'].astype(float)
    for i,row in data_merge.iterrows():
        #print(row[0])
        sum = 0
        if (row[3] >= quantile_75[3] and row[4] >= quantile_75[4] and row[1] >= quantile_75[1]) or \
                (quantile_50[3] <= row[3] < quantile_75[3] and quantile_50[4] <= row[4] < quantile_75[4] and
                 quantile_50[1] <= row[1] < quantile_75[1]) or (row[3] < quantile_50[3] and row[4] < quantile_50[4] and \
                                                                row[1] < quantile_50[1]):
            sum = +3.25
        if(quantile_50[3] <= row[3] < quantile_75[3] and row[4] >= quantile_75[4] and \
            quantile_50[1] <= row[1] < quantile_75[1]) or (row[3] < quantile_50[3] and \
            quantile_50[4] <= row[4] < quantile_75[4] and row[1] < quantile_50[1]):
            sum=+3.0
        elif(quantile_50[3] <= row[3] < quantile_75[3] and row[4] >= quantile_75[4] and row[1] >= quantile_75[1]) or \
                (row[3]<quantile_75[3] and quantile_50[4] <= row[4] < quantile_75[4] and quantile_50[4] <= row[4] < quantile_75[4]):
            sum=+2.75
        elif (row[3] >= quantile_75[3] and row[4] >= quantile_75[4] and quantile_50[1] <= row[1] < quantile_75[
            2]) or \
                (quantile_50[3] <= row[3] < quantile_75[3] and quantile_50[4] <= row[4] < quantile_75[4] and row[
                    2] < quantile_50[1]):
            sum = +2.5
        elif (row[3] >= quantile_75[3] and quantile_50[4] <= row[4] < quantile_75[4] and row[1] >= quantile_75[
            1]) or \
                (quantile_50[3] <= row[3] < quantile_75[3] and row[4] < quantile_50[4] and quantile_50[1] <= row[
                    1] < quantile_75[1]):
            sum = +2.25
        elif (row[3] >= quantile_75[3] and quantile_50[4] <= row[4] < quantile_75[4] and quantile_50[1] <= row[1] <
              quantile_75[1]) or \
                (quantile_50[3] <= row[3] < quantile_75[3] and row[4] < quantile_50[4] and row[1] < quantile_50[
                    2]):
            sum = +2.0
        elif (quantile_50[3] <= row[3] < quantile_75[3] and quantile_50[4] <= row[4] < quantile_75[4] and row[1] >= \
                quantile_75[1]) or (row[3] < quantile_50[3] and row[4] < quantile_50[4] and \
                                    quantile_50[1] <= row[1] < quantile_75[1]):
            sum = 1.75
        elif row[3] >= quantile_75[3] and row[4]<quantile_50[4] and row[1] >= quantile_75[1]:
            sum = +1.5

        elif row[3] >= quantile_75[3] and row[4] < quantile_50[4] and quantile_50[1] <= row[1] < quantile_75[1]:
            sum = +1.25
        elif row[3] >= quantile_75[3] and row[4] >= quantile_75[4] and row[1] < quantile_50[1]:
            sum = +1.0
        elif row[3] >= quantile_75[3] and quantile_50[4] <= row[4] < quantile_75[4] and quantile_50[1] <= row[1]:
            sum = +0.75
        elif quantile_50[3] <= row[3] < quantile_75[3] and row[4] < quantile_50[4] and row[1] >= quantile_75[1]:
            sum = +0.5
        elif row[3] >= quantile_75[3] and row[4] < quantile_50[4] and row[1] < quantile_50[1]:
            sum = +0.25
        elif row[3] < quantile_50[3] and row[1]>=quantile_75[1] and row[1] >= quantile_75[1]:
            sum=+0.0
        elif row[3] < quantile_50[3] and row[4]>=quantile_75[4] and quantile_50[1] <= row[1] < quantile_75[1]:
            sum=-0.25
        elif row[3] < quantile_50[3] and row[4]>=quantile_75[4] and row[1]<quantile_50[1]:
            sum=-0.5
        elif row[3] < quantile_50[3] and quantile_50[4] <= row[4] < quantile_75[4] and row[1] >= quantile_75[1]:
            sum=-0.75

        elif row[3] < quantile_50[3] and row[4] < quantile_50[4] and row[1] >= quantile_75[1]:
            sum=-1.0

        row[5]=sum
        if ((row[5] == 3.25 or row[5]==3) and row[0] >= quantile_75[0] and row[2] >= quantile_75[2]) or \
                ((row[5] == 3.25 or row[5]==3) and row[0] < quantile_50[0] and row[2] < quantile_50[2]) or \
                ((row[5] == 3.25 or row[5]==3) and quantile_50[0] <= row[0] < quantile_75[0] and quantile_50[2] <= row[2] <
                 quantile_75[2]):
            row[5] += 1.75
        elif ((row[5] == 3.25 or row[5]==3) and quantile_50[0] <= row[0] < quantile_75[0] and row[2] >= quantile_75[2]) or \
                ((row[5] == 3.25 or row[5]==3) and quantile_50[2] <= row[2] < quantile_75[2] and row[0] >= quantile_75[0]):
            row[5] += 1.5
        elif ((row[5] == 3.25 or row[5]==3) and quantile_50[0] <= row[0] < quantile_75[0] and row[2] < quantile_50[2]) or \
                ((row[5] == 3.25 or row[5]==3) and quantile_50[2] <= row[2] < quantile_75[2] and row[0] < quantile_50[0]):
            row[5] += 1.25
        elif ((row[5] == 3.25 or row[5]==3) and row[0] >= quantile_75[0] and row[2] < quantile_50[2]) or \
                ((row[5] == 3.25 or row[5]==3) and row[2] >= quantile_75[2] and row[0] < quantile_50[0]):
            row[5] += 1

        elif ((row[5] == 2.75 or row[5]==2.5) and row[0] >= quantile_75[0] and row[2] >= quantile_75[2]) or \
                ((row[5] == 2.75 or row[5]==2.5)and row[0] < quantile_50[0] and row[2] < quantile_50[2]) or \
                ((row[5] == 2.75 or row[5]==2.5) and quantile_50[0] <= row[0] < quantile_75[0] and quantile_50[2] <= row[2] <
                 quantile_75[
                     2]):
            row[5] += 1.75
        elif ((row[5] == 2.75 or row[5]==2.5) and quantile_50[0] <= row[0] < quantile_75[0] and row[2] >= quantile_75[2]) or \
                ((row[5] == 2.75 or row[5]==2.5) and quantile_50[2] <= row[2] < quantile_75[2] and row[0] >= quantile_75[0]):
            row[5] += 1.5
        elif ((row[5] == 2.75 or row[5]==2.5) and quantile_50[0] <= row[0] < quantile_75[0] and row[2] < quantile_50[2]) or \
                ((row[5] == 2.75 or row[5]==2.5) and quantile_50[2] <= row[2] < quantile_75[2] and row[0] < quantile_50[0]):
            row[5] += 1.25
        elif ((row[5] == 2.75 or row[5]==2.5) and row[0] >= quantile_75[0] and row[2] < quantile_50[2]) or \
                ((row[5] == 2.75 or row[5]==2.5) and row[2] >= quantile_75[2] and row[0] < quantile_50[0]):
            row[5] += 1
    print(data_merge.sort_values(by=['Population'], inplace=False))

    print(data_merge[['Population','Asthma', 'Population_Density']])
    plt.figure(figsize=(8,5))
    plt.plot(data_merge.index, data_merge.Population,'red',label="Population")
    plt.plot(data_merge.index, data_merge.Asthma, 'blue', label="Asthma")
    plt.title('Population VS Asthma')
    plt.ylabel('Number of persons')
    plt.xticks(rotation=90)
    plt.legend()
    plt.show()
    fig, ax1 = plt.subplots()

    color = 'tab:red'
    ax1.set_xlabel('States')
    ax1.set_ylabel('Number of persons', color=color)
    ax1.plot(data_merge.index, data_merge['Population'], color=color)
    ax1.tick_params(axis='y', labelcolor=color)

    ax2 = ax1.twinx()

    color = 'tab:blue'
    ax2.set_ylabel('Metric', color=color)
    ax2.plot(data_merge.index, data_merge['Metric'], color=color)
    ax2.tick_params(axis='y', labelcolor=color)

    fig.tight_layout()
    plt.show()

    #print(data_merge.index)

if __name__ == '__main__':
    df=pd.read_csv('Datasets/DATA.csv')
    data(df)