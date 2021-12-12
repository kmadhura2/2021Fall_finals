import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns



def Mortatlity_analysis(data)-> pd.DataFrame:
       """
       :param data: DataFrame from main class containg State Custom Data
       :return: DataFrame, prints pivoted dataframe and plots graphs of mortatlity rate of Pneumonia, Influenza and COVID-19 in duration of 2017-2020

       >>> df=pd.DataFrame()
       >>> Mortatlity_analysis(df)
       """
       isempty=data.empty
       if isempty == True:
              raise ValueError('DataFrame cannot be empty.')

       # replacing in cells with insufficient data with NAN
       data = data.replace('Insufficient Data', np.NaN)
       # dropping NAN from the DataFrame
       data = data.dropna()
       # Converting the string containg commas (',') in it with no space('')
       data.astype('str')
       data = data.replace(',', '', regex=True)
       #Melt function is useful to massage a DataFrame into a format where one or more columns are
       # identifier variables (id_vars), while all other columns, considered measured variables (value_vars),
       # are “unpivoted” to the row axis, leaving just two non-identifier columns, ‘variable’ and ‘value’.
       # We have kept SUB AREA, SEASON,WEEK as indentifer variables and DISEAS as non-indentifier variable and no of deaths as value.
       df_2 = pd.melt(data, id_vars=['SUB AREA', 'SEASON', 'WEEK'], var_name='DISEAS', value_name='NO. OF DEATHS')
       # converting DataFrame column No. of Deaths from string to Float64
       df_2['NO. OF DEATHS'] = df_2['NO. OF DEATHS'].astype(float)
       # created a for loop to get each year dataframe and plot garphs, therefore a list of SEASONS
       list1 = ['2017-18', '2018-19','2019-20','2020-21']
       for i in range(len(list1)):
              fluzone = df_2[df_2["SEASON"] == list1[i]]
              # indexing week i would also like to inofrm this idea came from A6 Assignment
              fluzone.set_index(['WEEK'], inplace=True)
              # Creating Pivoted Table
              pivoted_df = pd.pivot_table(fluzone, values="NO. OF DEATHS", index="WEEK", columns=["DISEAS"],
                                          aggfunc=[np.sum])
              # Ploting Figures for pivoted table consisting Pneumonia, Infouenza and COVID-19 Deaths
              ax = plt.figure()
              pivoted_df.plot()
              plt.title("Weekly Influenza,Pneumonia and COVID Deaths in US in Year " + list1[i])
              plt.ylabel('No of Deaths')
              plt.xlabel('Number of Week')
              plt.show()
              #Ploting Correlation matrix Cmap
              corr = pivoted_df.corr()

              sns.set(rc={'figure.figsize': (15, 6)})
              res = sns.heatmap(corr, cmap="RdBu", linewidth=0.5, fmt='.2f', annot=True, vmin=-1, vmax=1,
                                annot_kws={'fontsize': 14, 'fontweight': 'bold'}).set(title="Weekly Influenza,Pneumonia and COVID Deaths in US in Year " + list1[i])
              # Using If condition to retun specific Dataframe of season 2020-21 to main class
              if list1[i] == '2020-21':
                     return pivoted_df


def Incidence_rate(df_2)-> pd.DataFrame:
       """
       :param df_2: DataFrame from Main consiting dataframe of Covid Data of 2020 with daily no of reported cases and deaths
       :return: DataFrame of Incident Rate to Main
       >>> df=pd.DataFrame()
       >>> Incidence_rate(df)

       """
       isempty = data.empty
       if isempty == True:
              raise ValueError('DataFrame cannot be empty.')

       # Using Datetime liabary to convert date from DataFrame of type Object to Datetime object
       df_2['date'] = pd.to_datetime(df_2['date'], errors='coerce')
       df_2.astype('str')
       # Converting the string containg commas (',') in it with no space('')
       df_2 = df_2.replace(',', '', regex=True)
       # Converting coloumn of Population values from Str to FLoat64
       df_2['Population'] = df_2['Population'].astype(float)
       #Using Datetime function to convert the daily dates into week numbers
       df_2['Week_Number'] = df_2['date'].dt.week
       # to calculate the updated population subracting total deaths from it and and overiding in Population itself
       df_2['Population']=df_2['Population']-df_2['total_deaths']
       # dropping NAN values
       df_2=df_2.dropna()
       # Created a new Column and Calculated Incidence_Rate by dividing new cases reprted each day by updated population
       df_2['Incidence_Rate']=df_2['new_cases']/df_2['Population']
       # Created a new Dataframe with only Incident Rate
       df3=df_2[['Incidence_Rate']]
       plt.show()
       return df3

def sub_plot(ai,am):
       """
       :param ai: DataFrame from Incidence Rate of COVID-19 2020 dataset
       :param am: DataFrame from Pneumonia,Influenza, and COVID-19
       :return: None, printing plots
       """
       fig=plt.figure()
       plt.subplot(1,2,1)
       plt.plot(am)
       plt.title("Weekly Influenza,Pneumonia and COVID Deaths in US in Year 2020-21 ")
       plt.ylabel('No of Deaths')
       plt.xlabel('Number of Week')
       plt.subplot(1,2,2)
       plt.plot(ai)
       plt.title("Incidence Rate of COVID-19 Deaths in US during  2020-21 ")
       plt.ylabel('Incidence Rate')
       plt.xlabel('Number of Week')
       plt.show()


if __name__ == '__main__':
       # Reading Datasets using read_csv functions
       # Reading State Custom Data and with help of usecols selcting columns that we need
       data=pd.read_csv('Datasets/State_Custom_Data (1).csv',usecols=['SUB AREA', 'SEASON', 'WEEK','NUM INFLUENZA DEATHS', 'NUM PNEUMONIA DEATHS',
              'NUM COVID-19 DEATHS'])
       # Reading Covid data
       data_2=pd.read_csv('Datasets/owid-covid-data (1).csv',usecols=['location','date','new_cases','total_deaths','Population'])
       # calling function and saving the dataframe into a1
       a1=Incidence_rate(data_2)
       # calling function and saving dataframe into a2
       a2=Mortatlity_analysis(data)
       # calling function to plot to understand relation between Pneumonia, Influenza and COVID-19
       sub_plot(a1,a2)

