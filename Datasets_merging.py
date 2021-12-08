import pandas as pd
import numpy as np
from scipy.stats import skew
import matplotlib.pyplot as plt

def data(annual_path, population_path, aqi_path,i) -> pd.DataFrame():
    dataset=pd.read_csv(annual_path)
    dataset.rename(columns={'Edition': 'Year'}, inplace=True)
    list1=dataset['Measure Name'].unique()
    #print(list1)
    list2=['Asthma','Smoking','Air Pollution']
    df=pd.DataFrame()
    for i in range(len(list1)):
        if list1[i] in list2:
            df=df.append(dataset.loc[(dataset['Measure Name']== list1[i])])


    df.drop(columns=['Report Type','Lower CI','Upper CI','Source','Source Year','Rank'], inplace=True)
    df.rename(columns={'State Name': 'Location'}, inplace=True)

    df = df.pivot(index='Location', columns='Measure Name', values='Value')

    population = pd.read_csv(population_path, skiprows=[0, 1], usecols=['Location', 'Total Residents'])
    population = population.dropna()
    population.rename(columns={'Total Residents': 'Population'}, inplace=True)
    aqi = pd.read_csv(aqi_path, usecols=['State', 'County', 'Median AQI'])
    aqi.rename(columns={'State': 'Location'}, inplace=True)
    aqi_skip = aqi.groupby(['Location']).mean()
    data_merge = pd.merge(population, aqi_skip, on='Location', how='inner')
    density = pd.read_csv("Datasets/Land area.csv", usecols=['State', 'LandArea'])
    density.rename(columns={'State': 'Location'}, inplace=True)
    data_merge = pd.merge(data_merge, density, on='Location', how='inner')
    data_merge.insert(loc=3, column='Population_Density',
                          value=data_merge['Population'] / data_merge['LandArea'])
    data_merge.drop('LandArea', axis=1, inplace=True)

    data_merge.set_index('Location', inplace=True)

    frames=[df,data_merge]
    data_merge=pd.concat(frames,axis=1, join="inner")

    return data_merge


if __name__ == '__main__':
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
    final=pd.DataFrame()
    temp=pd.DataFrame()
    for i in range(len(years)):
        temp=data(annual_filenames[i],population_files[i],AQI_files[i],i)
        final=final.append(temp)

    final.to_csv('Datasets/DATA.csv')
