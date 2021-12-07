import pandas as pd

def data(annual_path, population_path, aqi_path,i):
    dataset=pd.read_csv(annual_path)
    dataset.rename(columns={'Edition': 'Year'}, inplace=True)
    list1=dataset['Measure Name'].unique()
    #print(list1)
    list2=['Access to Care - Annual','Asthma','Avoid Care Due to Cost','Illicit Opioid Use',
           'Crowded Housing', 'Smoking']
    df=pd.DataFrame()
    for i in range(len(list1)):
        if list1[i] in list2:
            #print(list1[i])
            df=df.append(dataset.loc[(dataset['Measure Name']== list1[i])])
            #dataset.drop(list1[i],axis=1)

    # print(df.head())
    df.drop(columns=['Report Type','Lower CI','Upper CI','Source','Source Year','Rank'], inplace=True)
    df.rename(columns={'State Name': 'Location'}, inplace=True)

    df = df.pivot(index='Location', columns='Measure Name', values='Value')
    # df.groupby('Measure Name')
    #print(df.head())

    population = pd.read_csv(population_path, skiprows=[0, 1], usecols=['Location', 'Total Residents'])
    population = population.dropna()
    population.rename(columns={'Total Residents': 'Population'}, inplace=True)
       # smk_data = pd.read_csv(filess[i], skiprows=[0, 1], usecols=['Location', 'All Adults'])
        # smk_data = smk_data.dropna()
        # smk_data.rename(columns={'All Adults': 'Smoking'}, inplace=True)
        # data_merge = pd.merge(population, smk_data, on='Location', how='inner')
    aqi = pd.read_csv(aqi_path, usecols=['State', 'County', 'Median AQI'])
    aqi.rename(columns={'State': 'Location'}, inplace=True)
    aqi_skip = aqi.groupby(['Location']).mean()
    data_merge = pd.merge(population, aqi_skip, on='Location', how='inner')
    density = pd.read_csv("Datasets/Land area.csv", usecols=['State', 'LandArea'])
    density.rename(columns={'State': 'Location'}, inplace=True)
    data_merge = pd.merge(data_merge, density, on='Location', how='inner')
    data_merge.insert(loc=3, column='Population Density',
                          value=data_merge['Population'] / data_merge['LandArea'])
    data_merge.drop('LandArea', axis=1, inplace=True)
        # data_merge['Location']=data_merge.index()
    data_merge.set_index('Location', inplace=True)
    #print('\n', years[i])
    #data_merge=pd.merge(data_merge,df, how='inner')
    frames=[df,data_merge]
    data_merge=pd.concat(frames,axis=1, join="inner")
    #result = pd.concat(frames_1, axis=0, join="inner")
    ##data_merge=pd.concat(frames_1,axis=0)
    #print(result)
    #i = i + 1
    #data_merge.append(year)
    print(data_merge.head())
    #frames_1=[final,data_merge]
    #final_1=pd.concat(frames_1, axis=0)
    #print(final_1)

    print('\n',years[i])
    print(data_merge)
    data_append=data_append.append(data_merge)
    i=i+1

# converting to csv
print(data_append)
data_append.to_csv('Datasets/basic_info.csv')