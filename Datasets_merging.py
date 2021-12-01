import pandas as pd
import numpy as np


population = pd.read_csv("Datasets/population_2016.csv", skiprows=[0,1],usecols=['Location','Total Residents'])
population=population.dropna()
print(population)