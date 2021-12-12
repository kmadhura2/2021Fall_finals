#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


# In[22]:


def correlation(corr_df:pd.DataFrame)->None:
    """
    This function calculates the correlation matrix using the pearson method and plots a heatmap of the matrix
    :param corr_df: A pandas dataframe containing data of all the states
    :return:
    >>> df=pd.DataFrame()
    >>> correlation(df) is None
    True
    """
    is_empty=corr_df.empty
    try:
        if is_empty==True:
            raise ValueError("DataFrame cannot be empty")
        # Creating correlation matrix using pearson method
        corr_matrix = corr_df[['Air_Pollution', 'Population', 'Asthma', 'Smoking', 'Population_Density']].corr(
               method='pearson')
        sns.set(rc={'figure.figsize': (12, 6)})
        sns.heatmap(corr_matrix, cmap="RdBu", linewidth=0.5, fmt='.2f', annot=True, vmin=-1, vmax=1, \
                        annot_kws={'fontsize': 14, 'fontweight': 'bold'})
    except ValueError:
        pass

    return None

# In[73]:


def calling_plots(subset_df1:pd.DataFrame, locations:list, subset_df2:pd.DataFrame, locations2:list)->None:
    """
    This function is calculates the subset of a dataframe with respective location
    :param subset_df1: a pandas dataframe containing data of the densely populated states
    :param locations: a list containing the densely populated state names
    :param subset_df2: a pandas dataframe containing data of the sparsely populated states
    :param locations2: a list containing the sparsely populated state names
    >>> df=pd.DataFrame()
    >>> correlation(df) is None
    True
    """
    try:
        for j in range(len(locations2)):
            #Creating a subset of densely populated states
            sub_df=subset_df1[subset_df1['Location']==locations[j]]
            state1=locations[j]
            # Creating a subset of sparsely populated states
            sub_df2=subset_df2[subset_df2['Location']==locations2[j]]
            state2=locations2[j]
            plotting_top(sub_df,state1)
            plotting_bottom(sub_df2,state2)
    except ValueError:
        pass


# In[63]:


def plotting_top(data1:pd.DataFrame,state2:str)->None:
    """
    This function plots a double line plot of Population VS Asthma over the years for densely populated states
    :param data1: a pandas dataframe containing data for the specific location
    :param state2: a string containing the state name
    >>> df=pd.DataFrame()
    >>> correlation(df) is None
    True
    """
    try:
        scaler1 = MinMaxScaler()
        #Normalizing the values
        data1[["Population"]] = scaler1.fit_transform(data1[["Population"]])
        data1[["Asthma"]] = scaler1.fit_transform(data1[["Asthma"]])

        sns.lineplot(data=data1,x='Year',y='Population',label='Population')
        sns.lineplot(data=data1,x='Year',y='Asthma',label='Asthma')
        plt.xlabel('Years')
        plt.ylabel('Number of Persons')
        plt.title('Population and Asthma in densely populated states in United Stats- '+state2,\
                  fontdict={'fontweight':'bold', 'fontsize':17})
        plt.figure(figsize=(12,6))
        plt.legend(labels=["Population","Asthma"])
    except ValueError:
        pass



# In[71]:


def plotting_bottom(data2:pd.DataFrame,state4:str)->None:
    """
    This function plots a double line plot of Population VS Asthma over the years for densely populated states
    :param data2: a pandas dataframe containing data for the specific location
    :param state4: a string containing the sparsely populated state name
    >>> df=pd.DataFrame()
    >>> correlation(df) is None
    True
    """
    try:
        scaler2 = MinMaxScaler()
        #Normalizing the values
        data2[["Population"]] = scaler2.fit_transform(data2[["Population"]])
        data2[["Asthma"]] = scaler2.fit_transform(data2[["Asthma"]])

        sns.lineplot(data=data2,x='Year',y='Population',label='Population')
        sns.lineplot(data=data2,x='Year',y='Asthma',label='Asthma')
        plt.xlabel('Years')
        plt.ylabel('Number of Persons')
        plt.title('Population and Asthma in sparsely populated states in United Stats- '+state4,\
                  fontdict={'fontweight':'bold', 'fontsize':17})
        plt.figure(figsize=(12,6))
        plt.legend(labels=["Population","Asthma"])
    except ValueError:
        pass


# In[5]:


def correlation_factors(corr_data:pd.DataFrame)->None:
    """
    This function plots a line chart explaining the correlation between various factors over the years
    :param corr_data: a pandas dataframe containing data of all the states over the years
    >>> df=pd.DataFrame()
    >>> correlation(df) is None
    True
    """
    try:
        #Grouping by Year
        corr_data=corr_data.groupby(['Year'])['Population','Population_Density','Smoking','Asthma','Air_Pollution'].sum()
        #Normalizing the values
        corr_data[["Population"]] = scaler.fit_transform(corr_data[["Population"]])
        corr_data[["Asthma"]] = scaler.fit_transform(corr_data[["Asthma"]])
        corr_data[["Smoking"]] = scaler.fit_transform(corr_data[["Smoking"]])
        corr_data[["Air_Pollution"]] = scaler.fit_transform(corr_data[["Air_Pollution"]])
        corr_data[["Population_Density"]] = scaler.fit_transform(corr_data[["Population_Density"]])
        #Plotting the graph
        plt.figure(figsize=(16,8))
        plt.title('Correlation between various factors and Asthma in United States',fontdict={'fontweight':'bold', 'fontsize':17})
        plt.plot(corr_data.index,corr_data['Population'],'b.-',linewidth=2, label='Population')
        plt.plot(corr_data.index,corr_data['Population_Density'],'r.-',linewidth=2,label='Population_Density')
        plt.plot(corr_data.index,corr_data['Asthma'],'g.-',linewidth=2, label='Asthma')
        plt.plot(corr_data.index,corr_data['Smoking'],'y.-',linewidth=2, label='Smoking')
        plt.plot(corr_data.index,corr_data['Air_Pollution'],'m.-',linewidth=2, label='Air_Pollution')
        plt.xlabel('Years')
        plt.ylabel('Number of Persons')
        plt.legend()
        plt.grid()
        plt.show()
    except ValueError:
        pass

# In[6]:


def calculate_rate(data:pd.DataFrame)->pd.DataFrame:
    """
    This function calculates the difference of Population and Asthma in consecutive years and timeframe
    :param data: a pandas dataframe consisting of data of all the states over the years
    :return: returns a pandas dataframe containing the difference and timeframe
    >>> df=pd.DataFrame()
    >>> correlation(df) is None
    True
    """
    try:
        data=data.sort_values(by=['Location','Year'], inplace=False, ascending=True)
        data['TimeFrame']=''
        for k in range(1,len(data)-1):
            #Creating a new column named TimeFrame and concatenating two-consecutive year values
            data['TimeFrame'][k-1] = data['Year'][k-1] + "-" + data['Year'][k]
        #Calculating the difference between Population over the years using the diff() function
        data['Population_Diff']=data['Population'].diff()
        # Calculating the difference between Asthma over the years using the diff() function
        data['Asthma_Diff']=data['Asthma'].diff()
    except ValueError:
        pass
    except KeyError:
        raise KeyError("True")
        pass
    return data


# In[7]:


def top(data_file:pd.DataFrame):
    """
    This function calculates the top5 and the bottom5 populated states over the years 
    :param data_file: 
    :return: This function returns two list containing top5 and bottom5 populated states
    >>> df=pd.DataFrame()
    >>> correlation(df) is None
    True
    """
    #Getting the unique years
    try:

        years = data_file['Year'].unique()
        top5 = []
        bottom5 = []
        for m in range(len(years)):
            data2 = data_file[data_file['Year'] == years[m]]
            d1 = data2.sort_values(by=['Population'], inplace=False, ascending=False)
            #Fetching the top 5 populated states
            top_s = d1.head(5)
            #Fetching the bottom 5 populated states
            bottom = d1.tail(5)
            top_states = top_s['Location'].tolist()
            bottom_states = bottom['Location'].tolist()
            #Top 5 populated states over the years
            top5.append(top_states)
            #Bottom 5 populated states over the years
            bottom5.append(bottom_states)

        top5 = [n for elem in top5 for n in elem]
        top5 = set(top5)
        top5 = list(top5)
        bottom5 = [p for elem in bottom5 for p in elem]
        bottom5 = set(bottom5)
        bottom5 = list(bottom5)
    except ValueError:
        pass
    return top5, bottom5


# In[8]:


def dropping_rows(df:pd.DataFrame, states:list):
    """
    This function takes the dataframe and states input and drops the unnecessary rows
    :param df: a pandas dataframe consisting data of all the states over the years
    :param states: a list containing the desired states
    :return: a pandas dataframe consisting data of the require states
    >>> df=pd.DataFrame()
    >>> correlation(df) is None
    True
    """
    try:
        for l in range(len(df)):
            #Dropping the rows other than the top5/bottom5 rows
            if df['Location'][l] not in states:
                df = df.drop([l])
            else:
                pass
        df = df.reset_index()
        df = df.drop(columns=['index'])
    except ValueError:
        pass
    return df


# In[26]:

if __name__ == '__main__':
    final_data = pd.read_csv('C:/Users/PC/Desktop/2021Fall_finals/Datasets/DATA.csv')
    scaler = MinMaxScaler()
    
    for i in range(len(final_data)):
        if final_data['Location'][i]=="Location":
            final_data=final_data.drop([i])

    final_data=final_data.reset_index()
    final_data=final_data.drop(['index'], axis=1)

# In[31]:


    final_data[['Air_Pollution','Population','Asthma','Smoking','Population_Density']].apply(pd.to_numeric)
    dict_columns_type = {'Air_Pollution':float,'Asthma':float,'Smoking':float,'Population':float,'Population_Density':float}
    final_data = final_data.astype(dict_columns_type)
    for i in range(len(final_data)):
        final_data['Air_Pollution'][i] = (final_data['Air_Pollution'][i] * final_data['Population'][i])/ 100
        final_data['Smoking'][i] = (final_data['Smoking'][i] * final_data['Population'][i]) / 100
        final_data['Asthma'][i] = (final_data['Asthma'][i] * final_data['Population'][i]) / 100
    #Calling the correlation function to get the correlation matrix and heatmap
    correlation(final_data)
    #Calling the calculate_rate function to get the Difference's column added
    rate_data=calculate_rate(final_data)
    #Calling the top() function to get the top5 and bottom5 densely populated states over the years
    top_location, bottom_location=top(rate_data)
    #Calling the dropping_rows() function to drop rows other than top5 densely populated states
    rate_data_top=dropping_rows(rate_data, top_location)
    # Calling the dropping_rows() function to drop rows other than bottom5 densely populated states
    rate_data_bottom=dropping_rows(rate_data,bottom_location)
    #Calling the calling_plots() function to plot the top5 and bottom5 densely populated states
    calling_plots(rate_data_top,rate_data_top['Location'].unique(),rate_data_bottom, rate_data_bottom['Location'].unique())
#print(rate_data_bottom['Location'].unique())

    correlation_factors(rate_data)

    for i in range(len(top_location)):
        subset_df=rate_data_top[rate_data_top['Location']==top_location[i]]
        state=top_location[i]
