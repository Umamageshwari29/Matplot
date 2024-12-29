
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
'''
dataframe=pd.read_csv("ZomatodataCSV.csv")
print(dataframe.head())

def handleRate(value):
    value=str(value).split('/')
    value=value[0];
    return float(value)

dataframe['rate']=dataframe['rate'].apply(handleRate)
print(dataframe.head())
'''
dataframe.info()

