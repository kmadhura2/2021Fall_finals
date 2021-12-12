import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

def Mortatlity_analysis(data):
       data = data.replace('Insufficient Data', np.NaN)
       data = data.dropna()
       data.astype('str')
       data = data.replace(',', '', regex=True)

       # print(data)
       df_2 = pd.melt(data, id_vars=['SUB AREA', 'SEASON', 'WEEK'], var_name='DISEAS', value_name='NO. OF DEATHS')
       df_2['NO. OF DEATHS'] = df_2['NO. OF DEATHS'].astype(float)
       list1 = ['2019-20', '2018-19', '2017-18','2020-21']
       for i in range(len(list1)):
              fluzone = df_2[df_2["SEASON"] == list1[i]]
              fluzone.set_index(['WEEK'], inplace=True)
              pivoted_df = pd.pivot_table(fluzone, values="NO. OF DEATHS", index="WEEK", columns=["DISEAS"],
                                          aggfunc=[np.sum])
              # print(pivoted_df.info())
              # print(pivoted_df)
              ax = plt.figure()
              pivoted_df.plot()
              # legend(['2017','2018','2019','2020','2021'])
              plt.title("Weekly Influenza,Pneumonia and COVID Deaths in US in Year " + list1[i])
              plt.ylabel('No of Deaths')
              plt.xlabel('Number of Week')
              plt.legend()
              # pivoted_df.plot.barh()
              plt.show()
              # sns.regplot(pivoted_df)
              corr = pivoted_df.corr()
              sns.set(rc={'figure.figsize': (12, 6)})
              res = sns.heatmap(corr, cmap="RdBu", linewidth=0.5, fmt='.2f', annot=True, vmin=-1, vmax=1,
                                annot_kws={'fontsize': 14, 'fontweight': 'bold'})

              if list1[i] == '2020-21':
                     return pivoted_df


def Incidence_rate(df_2):
       df_2['date'] = pd.to_datetime(df_2['date'], errors='coerce')
       df_2.astype('str')
       df_2 = df_2.replace(',', '', regex=True)
       df_2['Population'] = df_2['Population'].astype(float)
       df_2['Week_Number'] = df_2['date'].dt.week
       print(df_2)
       # print(df_2.info())
       df_2['Population']=df_2['Population']-df_2['total_deaths']
       print(df_2)
       df_2=df_2.dropna()
       df_2['Incidence_Rate']=df_2['new_cases']/df_2['Population']
       df3=df_2[['Incidence_Rate']]
       print(df3)
       plt.show()
       return df3

def sub_plot(ai,am):
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
       plt.legend()


data=pd.read_csv('Datasets/State_Custom_Data (1).csv',usecols=['SUB AREA', 'SEASON', 'WEEK','NUM INFLUENZA DEATHS', 'NUM PNEUMONIA DEATHS',
       'NUM COVID-19 DEATHS'])
data_2=pd.read_csv('Datasets/owid-covid-data (1).csv',usecols=['location','date','new_cases','total_deaths','Population'])
a1=Incidence_rate(data_2)
a2=Mortatlity_analysis(data)
sub_plot(a1,a2)

