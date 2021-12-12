import pandas as pd
import numpy as np
from scipy.stats import skew

def data(annual_path, population_path) -> pd.DataFrame():
    dataset=pd.read_csv(annual_path)
    dataset.rename(columns={'Edition': 'Year'}, inplace=True)
    list1=dataset['Measure Name'].unique()
    #print(list1)
    list2=['Asthma','Smoking','Air Pollution']
    df=pd.DataFrame()
    for i in range(len(list1)):
        if list1[i] in list2:
            df=df.append(dataset.loc[(dataset['Measure Name']== list1[i])])

    #print(df)


    df.drop(columns=['Report Type','Lower CI','Upper CI','Source','Source Year','Rank'], inplace=True)
    df.rename(columns={'State Name': 'Location'}, inplace=True)
    #print(df)
    cols=['Location','Year','Measure Name','Value','Score']
    df_2=df[['Location', 'Year']]
    #print(df_2)

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
    df_2.set_index('Location', inplace=True)

    frames=[df,data_merge]
    data_merge=pd.concat(frames,axis=1, join="inner")
    data_merge=data_merge.merge(df_2,on='Location',how="inner")

    return data_merge.drop_duplicates()

def split_years(dt:pd.DataFrame):
    """

    :param dt: DataFrame from main class to get unique years
    :return: list of dataframes
    """

    return [dt[dt['Year'] == y] for y in dt['Year'].unique()]

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

    years=['2012','2013','2014','2015','2016','2017','2018','2019','2020']
    final=pd.DataFrame()
    temp=pd.DataFrame()
    final_1=pd.DataFrame()
    for i in range(len(years)):
        temp=data(annual_filenames[i],population_files[i])
        #print(temp)
        final=final.append(temp)
    final_1=split_years(final)
    print(type(final_1))
    f=open('Datasets/DATA.csv','a')
    for df in final_1:
        df.to_csv(f)
    f.close()



