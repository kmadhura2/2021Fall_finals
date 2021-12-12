#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
pd.options.mode.chained_assignment = None


# In[2]:


def data(data_merge):
    dict_columns_type = {'Air Pollution': float,'Population': float,'Asthma':float,'Smoking':float,'Population_Density':float,                         'Year':str}

    data_merge = data_merge.astype(dict_columns_type)
    for index in data_merge.index:
      # assert isinstance(data_merge, float)
       data_merge['Air Pollution'][index] = (data_merge['Air Pollution'][index] * data_merge['Population'][index])/ 100
       data_merge['Smoking'][index] = (data_merge['Smoking'][index] * data_merge['Population'][index]) / 100
       data_merge['Asthma'][index] = (data_merge['Asthma'][index] * data_merge['Population'][index]) / 100
       #print(data_merge)
       #data_merge.info()

    quantile_50 = data_merge.quantile(0.5, axis=0)
    
    quantile_75 = data_merge.quantile(0.75, axis=0)


    
    data_merge[['Air Pollution','Asthma','Smoking','Population_Density','Year','Population']] = data_merge[['Air Pollution','Asthma','Smoking','Population_Density','Year','Population']].astype('float64')
    
    data_merge['Metric'] = data_merge.apply(calculate_metric, args=(quantile_50,quantile_75),axis = 1)
#   data_merge['Metric'] = data_merge.apply(update_metric, args=(quantile_50,quantile_75))

    return data_merge


# In[3]:


def calculate_metric(row, quantile_50, quantile_75):
    sum_score = 0
    if (row[3] >= quantile_75[3] and row[4] >= quantile_75[4] and row[1] >= quantile_75[1]) or             (quantile_50[3] <= row[3] < quantile_75[3] and quantile_50[4] <= row[4] < quantile_75[4] and
             quantile_50[1] <= row[1] < quantile_75[1]) or (row[3] < quantile_50[3] and row[4] < quantile_50[4] and \
                                                            row[1] < quantile_50[1]):
        sum_score = 3.25
    elif (quantile_50[3] <= row[3] < quantile_75[3] and row[4] >= quantile_75[4] and           quantile_50[1] <= row[1] < quantile_75[1]) or (row[3] < quantile_50[3] and                                                          quantile_50[4] <= row[4] < quantile_75[4] and row[1] <
                                                         quantile_50[1]):
        sum_score = 3.0
    elif (quantile_50[3] <= row[3] < quantile_75[3] and row[4] >= quantile_75[4] and row[1] >= quantile_75[1]) or             (row[3] < quantile_75[3] and quantile_50[4] <= row[4] < quantile_75[4] and quantile_50[4] <= row[4] <
             quantile_75[4]):
        sum_score = 2.75
    elif (row[3] >= quantile_75[3] and row[4] >= quantile_75[4] and quantile_50[1] <= row[1] < quantile_75[2]) or             (quantile_50[3] <= row[3] < quantile_75[3] and quantile_50[4] <= row[4] < quantile_75[4] and row[2] <
             quantile_50[1]):
        sum_score = 2.5
    elif (row[3] >= quantile_75[3] and quantile_50[4] <= row[4] < quantile_75[4] and row[1] >= quantile_75[1]) or             (quantile_50[3] <= row[3] < quantile_75[3] and row[4] < quantile_50[4] and quantile_50[1] <= row[
                1] < quantile_75[1]):
        sum_score = 2.25
    elif (row[3] >= quantile_75[3] and quantile_50[4] <= row[4] < quantile_75[4] and quantile_50[1] <= row[1] <
          quantile_75[1]) or \
            (quantile_50[3] <= row[3] < quantile_75[3] and row[4] < quantile_50[4] and row[1] < quantile_50[2]):
        sum_score = 2.0
    elif (quantile_50[3] <= row[3] < quantile_75[3] and quantile_50[4] <= row[4] < quantile_75[4] and row[1] >=           quantile_75[1]) or (row[3] < quantile_50[3] and row[4] < quantile_50[4] and
                              quantile_50[1] <= row[1] < quantile_75[1]):
        sum_score = 1.75
    elif row[3] >= quantile_75[3] and row[4] < quantile_50[4] and row[1] >= quantile_75[1]:
        sum_score = 1.5

    elif row[3] >= quantile_75[3] and row[4] < quantile_50[4] and quantile_50[1] <= row[1] < quantile_75[1]:
        sum_score = 1.25
    elif row[3] >= quantile_75[3] and row[4] >= quantile_75[4] and row[1] < quantile_50[1]:
        sum_score = 1.0
    elif row[3] >= quantile_75[3] and quantile_50[4] <= row[4] < quantile_75[4] and quantile_50[1] <= row[1]:
        sum_score = 0.75
    elif quantile_50[3] <= row[3] < quantile_75[3] and row[4] < quantile_50[4] and row[1] >= quantile_75[1]:
        sum_score = 0.5
    elif row[3] >= quantile_75[3] and row[4] < quantile_50[4] and row[1] < quantile_50[1]:
        sum_score = 0.25
    elif row[3] < quantile_50[3] and row[1] >= quantile_75[1] and row[1] >= quantile_75[1]:
        sum_score = 0.0
    elif row[3] < quantile_50[3] and row[4] >= quantile_75[4] and quantile_50[1] <= row[1] < quantile_75[1]:
        sum_score = -0.25
    elif row[3] < quantile_50[3] and row[4] >= quantile_75[4] and row[1] < quantile_50[1]:
        sum_score = -0.5
    elif row[3] < quantile_50[3] and quantile_50[4] <= row[4] < quantile_75[4] and row[1] >= quantile_75[1]:
        sum_score = -0.75

    elif row[3] < quantile_50[3] and row[4] < quantile_50[4] and row[1] >= quantile_75[1]:
        sum_score = -1.0
    else:
        sum_score = 0
#     print(sum_score)
    return sum_score


# In[4]:


def update_metric(row, quantile_50, quantile_75):

    update_sum = 0
    if ((row[5] == 3.25 or row[5] == 3) and row[0] >= quantile_75[0] and row[2] >= quantile_75[2]) or             ((row[5] == 3.25 or row[5] == 3) and row[0] < quantile_50[0] and row[2] < quantile_50[2]) or             ((row[5] == 3.25 or row[5] == 3) and quantile_50[0] <= row[0] < quantile_75[0] and quantile_50[2] <= row[
                2] <
             quantile_75[2]):
        update_sum += 1.75
    elif ((row[5] == 3.25 or row[5] == 3) and quantile_50[0] <= row[0] < quantile_75[0] and row[2] >= quantile_75[2]) or             ((row[5] == 3.25 or row[5] == 3) and quantile_50[2] <= row[2] < quantile_75[2] and row[0] >= quantile_75[
                0]):
        update_sum += 1.5
    elif ((row[5] == 3.25 or row[5] == 3) and quantile_50[0] <= row[0] < quantile_75[0] and row[2] < quantile_50[2]) or             ((row[5] == 3.25 or row[5] == 3) and quantile_50[2] <= row[2] < quantile_75[2] and row[0] < quantile_50[0]):
        update_sum += 1.25
    elif ((row[5] == 3.25 or row[5] == 3) and row[0] >= quantile_75[0] and row[2] < quantile_50[2]) or             ((row[5] == 3.25 or row[5] == 3) and row[2] >= quantile_75[2] and row[0] < quantile_50[0]):
        update_sum += 1

    elif ((row[5] == 2.75 or row[5] == 2.5) and row[0] >= quantile_75[0] and row[2] >= quantile_75[2]) or             ((row[5] == 2.75 or row[5] == 2.5) and row[0] < quantile_50[0] and row[2] < quantile_50[2]) or             ((row[5] == 2.75 or row[5] == 2.5) and quantile_50[0] <= row[0] < quantile_75[0] and quantile_50[2] <= row[
                2] <
             quantile_75[2]):
        update_sum += 1.75
    elif ((row[5] == 2.75 or row[5] == 2.5) and quantile_50[0] <= row[0] < quantile_75[0] and row[2] >= quantile_75[
        2]) or \
            ((row[5] == 2.75 or row[5] == 2.5) and quantile_50[2] <= row[2] < quantile_75[2] and row[0] >= quantile_75[
                0]):
        update_sum += 1.5
    elif ((row[5] == 2.75 or row[5] == 2.5) and quantile_50[0] <= row[0] < quantile_75[0] and row[2] < quantile_50[
        2]) or \
            ((row[5] == 2.75 or row[5] == 2.5) and quantile_50[2] <= row[2] < quantile_75[2] and row[0] < quantile_50[
                0]):
        update_sum += 1.25
    elif ((row[5] == 2.75 or row[5] == 2.5) and row[0] >= quantile_75[0] and row[2] < quantile_50[2]) or             ((row[5] == 2.75 or row[5] == 2.5) and row[2] >= quantile_75[2] and row[0] < quantile_50[0]):
        update_sum += 1
    else:
        pass
    return update_sum


# In[5]:


final_data = pd.read_csv('Datasets/DATA.csv')
index=final_data.index
condition = final_data["Location"] == "Location"
location_indices = index[condition]
location_indices_list = location_indices.tolist()
location_indices_list.insert(0,-1)
for i in range(1,(len(location_indices_list)-1)):
    year_data = pd.DataFrame
    starting_index= location_indices_list[i-1]+1
    ending_index= location_indices_list[i]-1
    year_data=final_data.loc[starting_index:ending_index]
    year_data=year_data.set_index('Location')
#print(year_data)
    #print(year_data)
    data_merge = data(year_data)


# In[6]:


data_merge


# In[7]:


data_merge.corr(method = 'pearson')


# In[106]:


import matplotlib.pyplot as plt
temp.plot(x='Location',y=['Population','Asthma','Population_Density'],kind = 'line', figsize = (16,8))


# In[99]:


import matplotlib.pyplot as plt
temp.plot(x='Location',y='Metric',kind = 'line')


# In[89]:


temp = data_merge.apply(pd.to_numeric)

temp = temp.reset_index()

temp['Population'] = (temp['Population'] - temp['Population'].min()) / (temp['Population'].max() - temp['Population'].min())
temp['Asthma'] = (temp['Asthma'] - temp['Asthma'].min()) / (temp['Asthma'].max() - temp['Asthma'].min())

temp['Metric'] = (temp['Metric'] - temp['Metric'].min()) / (temp['Metric'].max() - temp['Metric'].min())

temp['Population_Density'] = (temp['Population_Density'] - temp['Population_Density'].min()) / (temp['Population_Density'].max() - temp['Population_Density'].min())

