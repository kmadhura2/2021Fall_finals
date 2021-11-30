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
    print("\n",year)
    print(merged_data)

if __name__ == '__main__':
    population=pd.read_csv("C:/Users/PC/Desktop/2021Fall_finals/Datasets/Population asthama.csv", skiprows=[1])
    population_year=pd.DataFrame(population['Location'].copy())
    i=0
    for column_name, column_values in population.items():

        if column_name=="Location":
            continue
        selection=column_values.values
        if column_name=="Population-2016":
            population_year.insert(loc=1,column='Population',value=selection)
        else:
            population_year['Population']=selection
        population_year=population_year.sort_values(by=['Population'], ascending=False)
        files = ["C:/Users/PC/Desktop/AQI/annual_aqi_by_county_2016.csv",
                 "C:/Users/PC/Desktop/AQI/annual_aqi_by_county_2017.csv",
                 "C:/Users/PC/Desktop/AQI/annual_aqi_by_county_2018.csv",
                 "C:/Users/PC/Desktop/AQI/annual_aqi_by_county_2019.csv"]
        aqi_data(files[i], population_year.head(),column_name)
        population_year = population_year.sort_values(by=['Location'])

        i = i + 1
