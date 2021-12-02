import pandas as pd
import numpy as np

dataset=pd.read_csv('Datasets/2020-Annual (1).csv')
list1=dataset['Measure Name'].unique()
#print(list1)
list2=['Access to Care - Annual','Air and Water Quality - Annual','Asthma',
 'Asthma - $25-$49,999', 'Asthma - $50-$74,999', 'Asthma - $75,000 or More',
 'Asthma - Ages 18-44', 'Asthma - Ages 45-64', 'Asthma - Ages 65+',
 'Asthma - American Indian/Alaska Native', 'Asthma - Asian',
 'Asthma - Black', 'Asthma - College Grad', 'Asthma - Female',
 'Asthma - Hawaiian/Pacific Islander', 'Asthma - High School Grad',
 'Asthma - Hispanic', 'Asthma - Less Than $25,000',
 'Asthma - Less Than High School', 'Asthma - Male' 'Asthma - Multiracial',
 'Asthma - Other Race', 'Asthma - Some College', 'Asthma - White','E-cigarette Use - $25-$49,999', 'E-cigarette Use - $50-$74,999',
 'E-cigarette Use - $75,000 or More', 'E-cigarette Use - Ages 18-44',
 'E-cigarette Use - Ages 45-64', 'E-cigarette Use - Ages 65+',
 'E-cigarette Use - American Indian/Alaska Native',
 'E-cigarette Use - Asian', 'E-cigarette Use - Black',
 'E-cigarette Use - College Grad', 'E-cigarette Use - Female',
 'E-cigarette Use - Hawaiian/Pacific Islander',
 'E-cigarette Use - High School Grad', 'E-cigarette Use - Hispanic',
 'E-cigarette Use - Less Than $25,000',
 'E-cigarette Use - Less Than High School', 'E-cigarette Use - Male',
 'E-cigarette Use - Multiracial', 'E-cigarette Use - Other Race',
 'E-cigarette Use - Some College', 'E-cigarette Use - White',
       'Use of Illicit Opioids - $75,000 or More',
       'Use of Illicit Opioids - American Indian/Alaska Native',
       'Use of Illicit Opioids - Asian' 'Use of Illicit Opioids - Black',
       'Use of Illicit Opioids - College Grad' 'Use of Illicit Opioids - Female',
       'Use of Illicit Opioids - Hawaiian/Pacific Islander',
       'Use of Illicit Opioids - High School Grad',
       'Use of Illicit Opioids - Hispanic',
       'Use of Illicit Opioids - Less Than $25,000',
       'Use of Illicit Opioids - Less Than High School',
       'Use of Illicit Opioids - Male' 'Use of Illicit Opioids - Other Race',
       'Use of Illicit Opioids - Some College' 'Use of Illicit Opioids - White']
df=pd.DataFrame()
for i in range(len(list1)):
    if list1[i] in list2:
        #print(list1[i])
        df=df.append(dataset.loc[(dataset['Measure Name']== list1[i])])
        #dataset.drop(list1[i],axis=1)

# print(df.head())
df.drop(columns=['Report Type','Lower CI','Upper CI','Source','Source Year','Rank'], inplace=True)
print(df)







