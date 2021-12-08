import pandas as pd
import numpy as np
from scipy.stats import skew
import matplotlib.pyplot as plt
#from matplotlib import pyplot as plt
def data(annual_path, population_path, aqi_path,i):
    dataset = pd.read_csv(annual_path)
    dataset.rename(columns={'Edition': 'Year'}, inplace=True)
    list1 = dataset['Measure Name'].unique()
    # print(list1)
    list2 = ['Asthma', 'Smoking', 'Air Pollution']
    df = pd.DataFrame()
    for i in range(len(list1)):
        if list1[i] in list2:
            df = df.append(dataset.loc[(dataset['Measure Name'] == list1[i])])

    df.drop(columns=['Report Type', 'Lower CI', 'Upper CI', 'Source', 'Source Year', 'Rank'], inplace=True)
    df.rename(columns={'State Name': 'Location'}, inplace=True)

    df = df.pivot(index='Location', columns='Measure Name', values='Value')

    population = pd.read_csv(population_path, skiprows=[0, 1], usecols=['Location', 'Total Residents'])
    population = population.dropna()
    population.rename(columns={'Total Residents': 'Population'}, inplace=True)
    density = pd.read_csv("Datasets/Land area.csv", usecols=['State', 'LandArea'])
    density.rename(columns={'State': 'Location'}, inplace=True)
    data_merge = pd.merge(population, density, on='Location', how='inner')
    data_merge.insert(loc=3, column='Population_Density',
                      value=data_merge['Population'] / data_merge['LandArea'])
    data_merge.drop('LandArea', axis=1, inplace=True)

    data_merge.set_index('Location', inplace=True)

    frames = [df, data_merge]
    data_merge = pd.concat(frames, axis=1, join="inner")


    for location in data_merge.index:
        data_merge['Asthma'][location] = (data_merge['Asthma'][location] * data_merge['Population'][location]) / 100
        data_merge.insert(5, 'Metric', '0.0')
        skewed_data=data_merge.skew(axis=0, skipna=True)
        quantile_50=data_merge.quantile(0.5, axis = 0)
        quantile_100 = data_merge.quantile(1.0, axis=0)
        quantile_75=data_merge.quantile(0.75, axis=0)
        #print(skewed_data)
        #print(quantile_50)
        #print(quantile_75)
        #print(quantile_25)
        print(quantile_50)
        print(quantile_75)
        print(quantile_100)
        data_merge['Metric'] = data_merge['Metric'].astype(float)
        for i, row in data_merge.iterrows():
            row[0]=(row[0]*row[2])/100
            #print(row[0],[row[2]])
            #row[0]=(row[0]*row[2])/100
            sum=0
            #print(f"Index: {i}")
            #print(f"{row[0]}\n")
            if (row[2] >= quantile_75[2] and row[4] >= quantile_75[4] and row[0] >= quantile_75[0]) or \
                    (quantile_50[2]<=row[2]<quantile_75[2] and quantile_50[4]<=row[4]<quantile_75[4] and
                     quantile_50[0]<=row[0]<quantile_75[0]) or (row[2]<quantile_50[2] and row[4]<quantile_50[4]and row[0]<quantile_50[0]):
                sum = +3
            elif (row[2]<quantile_50[2] and quantile_50[4]<=row[4]<quantile_75[4] and quantile_50[0]<=row[0]<quantile_75[0]) \
                    or (quantile_50[2]<=row[2]<quantile_75[2] and row[4]>quantile_75[4] and row[0]>=quantile_75[0]):
                sum=+3.25
            elif(row[2] >= quantile_75[2] and row[4] >= quantile_75[4] and quantile_50[0] <= row[0] < quantile_75[0]) or \
                (quantile_50[2]<=row[2]<quantile_75[2] and quantile_50[4]<=row[4]<quantile_75[4] and row[0]<quantile_50[0]):
                sum=+2.7

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
            #print(row[5])
            plt.plot(row[0],row[2])
            plt.show()
            #plt.plot(row[0],row[2])
            #plt.show()
        #print(data_merge['Metric'])
        print(data_merge.sort_values(by=['Population'], inplace=False))
        #print('\n')
        #print(data_merge[['Population','Asthma', 'Population Density']])

        print(data_merge[['Population','Asthma', 'Population_Density']])
        plt.figure(figsize=(8,5))
        plt.plot(data_merge.index, data_merge.Population,'red',label="Population")
        plt.plot(data_merge.index, data_merge.Asthma, 'blue', label="Asthma")
        plt.title('Population VS Asthma')
        plt.ylabel('Number of persons')
        plt.legend()
        plt.show()
        #print(data_merge.index)


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

for i in range(1):
    #function_name([i])
    data(annual_filenames[i],population_files[i],AQI_files[i],i)
   #final= pd.concat([final,data(annual_filenames[i],population_files[i],AQI_files[i],i)],axis=0)