import numpy as np
import pandas as pd
def aqi_data(file_name:str,top_five:pd.DataFrame, year:str)->None:
    """
    :param file_name: Includes the year_wise file_path
    :param top_five: Includes a dataframe containing the top-5 populated states in that year
    :param year: A string for the population-year

    """
    aqi=pd.read_csv(file_name, usecols=['State','County','Year', 'Median AQI'])
    aqi.rename(columns={'State': 'Location'}, inplace=True)
    aqi_skip=aqi.groupby(['Location','Year']).mean()
    merged_data = pd.merge(top_five, aqi_skip, on='Location', how="inner")
    merged_data=merged_data.round(decimals=2)
    print("\n",year)
    print(merged_data)
    # smoking_data('Datasets/Smoking.csv', merged_data, column_name)

# def smoking_data(file_name:str,top_five:pd.DataFrame,year:str)-> None:
#     smk_data=pd.read_csv(file_name,skiprows=[1])
#     print('\n',year)
#     if year == 'Population-2016':
#         data_merge = pd.merge(top_five, smk_data, on='Location', how='inner')
#         remove=data_merge.drop(['Smoking-2017','Smoking-2018','Smoking-2019','Smoking-2020'],axis=1)
#         print(remove)
#     elif year == 'Population-2017':
#         data_merge = pd.merge(top_five, smk_data, on='Location', how='inner')
#         remove = data_merge.drop(['Smoking-2016', 'Smoking-2018', 'Smoking-2019', 'Smoking-2020'], axis=1)
#         print(remove)
#     elif year == 'Population-2018':
#         data_merge = pd.merge(top_five, smk_data, on='Location', how='inner')
#         remove = data_merge.drop(['Smoking-2016', 'Smoking-2017', 'Smoking-2019', 'Smoking-2020'], axis=1)
#         print(remove)
#     elif year == 'Population-2019':
#         data_merge = pd.merge(top_five, smk_data, on='Location', how='inner')
#         remove = data_merge.drop(['Smoking-2016', 'Smoking-2017', 'Smoking-2018', 'Smoking-2020'], axis=1)
#         print(remove)
#     elif year == 'Population-2020':
#         data_merge = pd.merge(top_five, smk_data, on='Location', how='inner')
#         remove = data_merge.drop(['Smoking-2016', 'Smoking-2017', 'Smoking-2018', 'Smoking-2019'], axis=1)
#         print(remove)

if __name__ == '__main__':
    population=pd.read_csv("Datasets/Population asthama.csv", skiprows=[1])
    smk_data = pd.read_csv('Datasets/Smoking.csv', skiprows=[1])
    density = pd.read_csv("C:/Users/PC/Desktop/2021Fall_finals/Datasets/Land area.csv", usecols=['State', 'LandArea'])
    density.rename(columns={'State': 'Location'}, inplace=True)
    data_merge = pd.merge(population, smk_data, on='Location', how='inner')
    population_year = pd.merge(population, density, on='Location', how="left")
    population_year = population_year.drop(
        columns=['Population-2016', 'Population-2017', 'Population-2018', 'Population-2019'], axis=1)
    #population_year = pd.DataFrame(data_merge['Location'].copy())
    i=0
    for column_name, column_values in data_merge.items():

        if column_name=="Location":
            continue
        selection=column_values.values
        if column_name=="Population-2016" and "Smoking-2016":
            population_year.insert(loc=1,column='Population',value=selection)
            population_year.insert(loc=2, column='Smoking',value=selection)
            population_year.insert(loc=3, column='Population Density',
                                   value=population_year['Population'] / population_year['LandArea'])
        else:
            population_year['Population']=selection
            population_year['Population Density'] = population_year['Population'] / population_year['LandArea']
        population_year=population_year.sort_values(by=['Population'], ascending=False)
        files = ["Datasets/AQI/annual_aqi_by_county_2016.csv",
                 "Datasets/AQI/annual_aqi_by_county_2017.csv",
                 "Datasets/AQI/annual_aqi_by_county_2018.csv",
                 "Datasets/AQI/annual_aqi_by_county_2019.csv",
                 "Datasets/AQI/annual_aqi_by_county_2020.csv"]
        aqi_data(files[i], population_year.head(),column_name)
        population_year = population_year.sort_values(by=['Location'])
        i = i + 1