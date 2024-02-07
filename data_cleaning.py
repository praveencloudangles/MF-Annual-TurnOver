from data_analysis import data_analysis
from sklearn.preprocessing import LabelEncoder
import pandas as pd

def data_preproc():
    df = data_analysis()
    print("---------------",df)
        
    print("after nulls values------------", df.isnull().sum())
    
    print("data--------", df)
    print("data types----------", df.dtypes)
    
    categ = []
    numer = []
    
    for col in df.columns:
        if df[col].dtypes == object:
            categ.append(col)
        else:
            numer.append(col)
    
    #print("categ--------", categ)
    #print("numer--------", numer)
    
    
    df['quote_type'] = df['quote_type'].replace(['MutualFund'], ['0'])
    df['size_type'] = df['size_type'].replace(['Large', 'Medium', 'Small'], ['0', '1', '2'])
    df['investment_type'] = df['investment_type'].replace(['Blend', 'Value', 'Growth'], ['0', '1', '2'])
    df['exchange_timezone'] = df['exchange_timezone'].replace(['America/New_York'], ['0'])
    df['exchange_name'] = df['exchange_name'].replace(['Nasdaq'], ['0'])
    df['exchange_code'] = df['exchange_code'].replace(['NAS'], ['0'])
    df['currency'] = df['currency'].replace(['USD'], ['0'])
    df['region'] = df['region'].replace(['US'], ['0'])
    
    convert_dict = {'quote_type': int, 'size_type': int, 'investment_type': int, 'exchange_timezone': int, 'exchange_name': int, 'exchange_code': int, 'currency': int, 'region': int}
    df = df.astype(convert_dict)
    
    df[['price_date', 'fund_short_name', 'fund_long_name', 'fund_category', 'fund_family', 'management_name', 'management_bio', 'management_start_date', 'investment_strategy', 'inception_date']] = df[['price_date', 'fund_short_name', 'fund_long_name', 'fund_category', 'fund_family', 'management_name', 'management_bio', 'management_start_date', 'investment_strategy', 'inception_date']].apply(LabelEncoder().fit_transform)
    
    final_conv_dict = {'price_date': int, 'fund_short_name': int, 'fund_long_name': int, 'fund_category': int, 'fund_family': int, 'management_name': int, 'management_bio': int, 'management_start_date': int, 'investment_strategy': int, 'inception_date': int}
    
    df = df.astype(final_conv_dict)
    
    print("checkinf types-------------", df.dtypes)
    
    df.drop(['fund_symbol','fund_short_name', 'fund_long_name', 'region', 'management_bio', 'fund_max_deferred_sales_load', 'fund_max_12b1_fee', 'fund_max_front_end_sales_load', 'quote_type', 'currency', 'exchange_timezone', 'exchange_name', 'exchange_code', 'fund_prospectus_gross_expense_ratio'], inplace=True, axis=1)
    
    print(df)
    
    return df
    
    
data_preproc()
