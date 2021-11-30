import numpy as np
import pandas as pd
files=["C:/Users/PC/Desktop/AQI/annual_aqi_by_county_2016.csv", "C:/Users/PC/Desktop/AQI/annual_aqi_by_county_2017.csv",
       "C:/Users/PC/Desktop/AQI/annual_aqi_by_county_2018.csv", "C:/Users/PC/Desktop/AQI/annual_aqi_by_county_2019.csv",
       "C:/Users/PC/Desktop/AQI/annual_aqi_by_county_2020.csv"]
def aqi_data(file_name):
    aqi=pd.read_csv(file_name, usecols=['State','County','Year', 'Median AQI'])
    aqi_skip=aqi.groupby(['State','Year']).mean()
    print(aqi_skip)


for i in range(len(files)):
    aqi_data(files[i])
