from data_loading import data_load
import pandas as pd
import warnings


warnings.filterwarnings("ignore")
def data_analysis():
    df = data_load()

    print("null values-----------", df.isnull().sum())
    print("duplicate values----------", df.duplicated().sum())
    print("shape of data------------", df.shape)
    
    return df

data_analysis()
