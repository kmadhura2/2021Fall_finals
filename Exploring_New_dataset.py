import pandas as pd
import numpy as np
from scipy.stats import skew
#import matplotlib.pyplot as plt
def data(annual_path, population_path, aqi_path,i):
    dataset=pd.read_csv(annual_path)
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
    df.rename(columns={'State Name': 'Location'}, inplace=True)

    df = df.pivot(index='Location', columns='Measure Name', values='Value')
    # df.groupby('Measure Name')
    #print(df.head())

    population = pd.read_csv(population_path, skiprows=[0, 1], usecols=['Location', 'Total Residents'])
    population = population.dropna()
    population.rename(columns={'Total Residents': 'Population'}, inplace=True)
       # smk_data = pd.read_csv(filess[i], skiprows=[0, 1], usecols=['Location', 'All Adults'])
        # smk_data = smk_data.dropna()
        # smk_data.rename(columns={'All Adults': 'Smoking'}, inplace=True)
        # data_merge = pd.merge(population, smk_data, on='Location', how='inner')
    aqi = pd.read_csv(aqi_path, usecols=['State', 'County', 'Median AQI'])
    aqi.rename(columns={'State': 'Location'}, inplace=True)
    aqi_skip = aqi.groupby(['Location']).mean()
    data_merge = pd.merge(population, aqi_skip, on='Location', how='inner')
    density = pd.read_csv("Datasets/Land area.csv", usecols=['State', 'LandArea'])
    density.rename(columns={'State': 'Location'}, inplace=True)
    data_merge = pd.merge(data_merge, density, on='Location', how='inner')
    data_merge.insert(loc=3, column='Population Density',
                          value=data_merge['Population'] / data_merge['LandArea'])
    data_merge.drop('LandArea', axis=1, inplace=True)
        # data_merge['Location']=data_merge.index()
    data_merge.set_index('Location', inplace=True)
    #print('\n', years[i])
    #data_merge=pd.merge(data_merge,df, how='inner')
    frames=[df,data_merge]
    data_merge=pd.concat(frames,axis=1, join="inner")
    #result = pd.concat(frames_1, axis=0, join="inner")
    ##data_merge=pd.concat(frames_1,axis=0)
    #print(result)
    #i = i + 1
    #data_merge.append(year)
    #print(data_merge.head())
    #frames_1=[final,data_merge]
    #final_1=pd.concat(frames_1, axis=0)
    #print(final_1)
    data_merge.insert(5, 'Metric', '0.0')
    skewed_data=data_merge.skew(axis=0, skipna=True)
    quantile_50=data_merge.quantile(0.5, axis = 0)
    quantile_75=data_merge.quantile(0.75, axis=0)
    #print(skewed_data)
    #print(quantile_50)
    #print(quantile_75)
    data_merge['Metric'] = data_merge['Metric'].astype(float)
    for i, row in data_merge.iterrows():
        sum=0
        #print(f"Index: {i}")
        #print(f"{row[0]}\n")
        if row[2] >= quantile_75[2] and row[4] >= quantile_75[4] and row[0] >= quantile_75[0]:
            sum = +3
        if row[2] >= quantile_75[2] and row[4] >= quantile_75[4] and quantile_75[0] > row[0] >= quantile_50[0]:
            sum = +2.5
        if row[2] >= quantile_75[2] and row[4] >= quantile_75[4] and row[0] < quantile_75[0]:
            sum = +2
        if quantile_75[2] >= row[2] >= quantile_50[2] and quantile_75[4] >= row[4] >= quantile_50[4] and row[0] >= \
                quantile_75[0]:
            sum = -1
        if row[2] < quantile_50[2] and row[4] < quantile_75[4] and row[0] >= quantile_75[0]:
            sum = -2

        row[5]=sum
        #print(row[5])

    #print(data_merge['Metric'])
    print(data_merge.sort_values(by=['Population'], inplace=False))



annual_filenames=['Datasets/Annual Reports/2012-Annual.csv',
                  'Datasets/Annual Reports/2013-Annual.csv','Datasets/Annual Reports/2014-Annual.csv',
                  'Datasets/Annual Reports/2015-Annual.csv','Datasets/Annual Reports/2016-Annual.csv',
                  'Datasets/Annual Reports/2017-Annual.csv','Datasets/Annual Reports/2018-Annual.csv',
                  'Datasets/Annual Reports/2019-Annual.csv','Datasets/Annual Reports/2020-Annual (1).csv']
population_files = ["Datasets/Population/population_2012.csv",
                    "Datasets/Population/population_2013.csv","Datasets/Population/population_2014.csv",
                    "Datasets/Population/population_2015.csv","Datasets/Population/population_2016.csv",
                    "Datasets/Population/population_2017.csv","Datasets/Population/population_2018.csv",
                    "Datasets/Population/population_2019.csv","Datasets/Population/population_2020.csv"]
AQI_files=["Datasets/AQI/annual_aqi_by_county_2012.csv",
           "Datasets/AQI/annual_aqi_by_county_2013.csv","Datasets/AQI/annual_aqi_by_county_2014.csv",
           "Datasets/AQI/annual_aqi_by_county_2015.csv","Datasets/AQI/annual_aqi_by_county_2016.csv",
           "Datasets/AQI/annual_aqi_by_county_2017.csv","Datasets/AQI/annual_aqi_by_county_2018.csv",
           "Datasets/AQI/annual_aqi_by_county_2019.csv","Datasets/AQI/annual_aqi_by_county_2020.csv"]
years=['2012','2013','2014','2015','2016','2017','2018','2019','2020']
final=pd.DataFrame
for i in range(1):
    #function_name([i])
    data(annual_filenames[i],population_files[i],AQI_files[i],i)
   #final= pd.concat([final,data(annual_filenames[i],population_files[i],AQI_files[i],i)],axis=0)
    #final=final.append(other=result)