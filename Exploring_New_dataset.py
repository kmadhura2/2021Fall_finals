import pandas as pd
import numpy as np
def data(path):
    dataset=pd.read_csv(path)
    dataset.rename(columns={'Edition': 'Year'}, inplace=True)
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
    print(df.head())

annual_filenames=['Datasets/Annual Reports/2011-Annual.csv','Datasets/Annual Reports/2012-Annual.csv',
                  'Datasets/Annual Reports/2013-Annual.csv','Datasets/Annual Reports/2014-Annual.csv',
                  'Datasets/Annual Reports/2015-Annual.csv','Datasets/Annual Reports/2016-Annual.csv',
                  'Datasets/Annual Reports/2017-Annual.csv','Datasets/Annual Reports/2018-Annual.csv',
                  'Datasets/Annual Reports/2019-Annual.csv','Datasets/Annual Reports/2020-Annual (1).csv']
for i in range(len(annual_filenames)):
    #function_name([i])
    data(annual_filenames[i])
#data('Datasets/2020-Annual (1).csv')




