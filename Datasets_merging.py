import pandas as pd
import numpy as np

files = ["Datasets/population_2016.csv",
         "Datasets/population_2017.csv",
         "Datasets/population_2018.csv",
         "Datasets/population_2019.csv"]
filess =["Datasets/smoking_2016.csv",
         "Datasets/smoking_2017.csv",
         "Datasets/smoking_2018.csv",
         "Datasets/smoking_2019.csv",]
filesss=["Datasets/AQI/annual_aqi_by_county_2016.csv",
         "Datasets/AQI/annual_aqi_by_county_2017.csv",
         "Datasets/AQI/annual_aqi_by_county_2018.csv",
         "Datasets/AQI/annual_aqi_by_county_2019.csv"]
years=['2016','2017','2018','2019']
i = 0
while i < len(files):
    population = pd.read_csv(files[i], skiprows=[0,1],usecols=['Location','Total Residents'])
    population=population.dropna()
    population.rename(columns={'Total Residents': 'Population'}, inplace=True)
    smk_data = pd.read_csv(filess[i], skiprows=[0, 1], usecols=['Location', 'All Adults'])
    smk_data = smk_data.dropna()
    smk_data.rename(columns={'All Adults': 'Smoking'}, inplace=True)
    data_merge = pd.merge(population, smk_data, on='Location', how='inner')
    aqi = pd.read_csv(filesss[i], usecols=['State', 'County', 'Median AQI'])
    aqi.rename(columns={'State': 'Location'}, inplace=True)
    aqi_skip = aqi.groupby(['Location']).mean()
    data_merge= pd.merge(data_merge,aqi_skip, on='Location', how='inner')
    density = pd.read_csv("Datasets/Land area.csv", usecols=['State', 'LandArea'])
    density.rename(columns={'State': 'Location'}, inplace=True)
    data_merge = pd.merge(data_merge, density, on='Location', how='inner')
    data_merge.insert(loc=3, column='Population Density',
                           value=data_merge['Population'] / data_merge['LandArea'])
    data_merge.drop('LandArea',axis=1,inplace=True)

    print('\n',years[i])
    print(data_merge)
    i=i+1

