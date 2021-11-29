import numpy as np
import pandas as pd
if __name__ == '__main__':
    population=pd.read_csv("C:/Users/PC/Desktop/2021Fall_finals/Datasets/Population asthama.csv", skiprows=[1])
    population_year=pd.DataFrame(population['Location'].copy())
    print(type(population_year))
    for column_name, column_values in population.items():
        if column_name=="Location":
            continue
        selection=column_values.values
        if column_name=="Population-2011":
            population_year.insert(loc=1,column='Population',value=selection)
        else:
            population_year['Population']=selection
        population_year=population_year.sort_values(by=['Population'], ascending=False)
        print("\n",column_name)
        print(population_year.head())
        population_year = population_year.sort_values(by=['Location'])
