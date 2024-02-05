import pandas as pd

def data_load():
    path = "https://stock-market-usecase.s3.amazonaws.com/Mutual+Funds+Annual+TurnOver.csv"
    df = pd.read_csv(path)
    print("dataframe----------", df)
    return df
data_load()