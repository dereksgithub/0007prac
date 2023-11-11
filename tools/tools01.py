import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# this is a data clearning function
def data_cleaning(df):
    df = df.dropna()
    df = df.drop_duplicates()
    df = df.reset_index(drop=True)
    return df

# this is a data visualization function
def data_visualization(df):
    df.plot()
    plt.show()
    return None

# this is a data normalization function
def data_normalization(df):
    df = (df - df.mean()) / df.std()
    return df   

# this is a data standardization function
def data_standardization(df):
    df = (df - df.min()) / (df.max() - df.min())
    return df   

# this is a data standardization function
def data_standardization(df):
    df = (df - df.min()) / (df.max() - df.min())
    return df   


