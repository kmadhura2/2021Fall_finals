import pandas as pd
import numpy as np
def data(path):
    dataset=pd.read_csv(path)
    list1=dataset['Measure Name'].unique()
    #print(list1)
    list2=['Access to Care - Annual','Asthma','Avoid Care Due to Cost','Illict Opioid Use',
           'Crowded Housing', 'Smoking']
    df=pd.DataFrame()
    for i in range(len(list1)):
        if list1[i] in list2:
            #print(list1[i])
            df=df.append(dataset.loc[(dataset['Measure Name']== list1[i])])
            #dataset.drop(list1[i],axis=1)

    # print(df.head())
    df.drop(columns=['Report Type','Lower CI','Upper CI','Source','Source Year','Rank'], inplace=True)
    # df.groupby('Measure Name')
    print(df)

data('Datasets/2020-Annual (1).csv')




