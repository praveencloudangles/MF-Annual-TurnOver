from data_cleaning import data_preproc
import pandas as pd
import plotly.express as px
import warnings
warnings.filterwarnings("ignore")
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.figure_factory as ff
import plotly.io as pio
import plotly.graph_objects as go
import io
from PIL import Image


def data_vis():
    data = data_preproc()
    print(data)
    
    column = list(data.columns)
    print("columns-----------", column)
    column_to_remove = ["price_date", 'subsequent_investment', 'fund_category', 'fund_family', 'management_name', 'management_start_date', 'year_to_date_return', 'morningstar_risk_rating', 'inception_date', 'investment_type', 'size_type', 'fund_annual_report_net_expense_ratio', 'category_annual_report_net_expense_ratio', 'fund_prospectus_net_expense_ratio', 'category_max_front_end_sales_load', 'category_max_deferred_sales_load', 'last_cap_gain']
    
    for col_to_remove in column_to_remove:
        column.remove(col_to_remove)
    print("shortlisted columns----------------------",column)
     
    columns_to_remove_outliers = ['nav_per_share', 'initial_investment', 'total_net_assets', 'investment_strategy', 'morningstar_overall_rating', 'last_dividend', 'annual_holdings_turnover']

    for col in columns_to_remove_outliers:
        q1 = data[col].quantile(0.25)
        q3 = data[col].quantile(0.75)
        iqr = q3 - q1
        upper_limit = q3 + (1.5 * iqr)
        lower_limit = q1 - (1.5 * iqr)

        # Apply the filtering conditions to the original DataFrame
        data = data.loc[(data[col] < upper_limit) & (data[col] > lower_limit)]

    
    for i in column:
        fig = px.histogram(data, y=i)
        fig.update_layout(template='plotly_dark')
        fig.update_xaxes(showgrid=False, zeroline=False)
        fig.update_yaxes(showgrid=False, zeroline=False)
        fig.write_image(f"{i}_hist.jpg")
#       
    for i in column:
        fig = px.box(data, y=i)
        fig.update_layout(template='plotly_dark')
        fig.update_xaxes(showgrid=False,zeroline=False)
        fig.update_yaxes(showgrid=False,zeroline=False)
        fig.write_image(f"{i}_box.jpg")

    df=data[column]
    print("f-----", df)
    y=df.corr().columns.tolist()
    z=df.corr().values.tolist()
    z_text = np.around(z, decimals=4) # Only show rounded value (full value on hover)
    fig = ff.create_annotated_heatmap(z,x=y,y=y,annotation_text=z_text,colorscale=px.colors.sequential.Cividis_r,showscale=True)
    fig.update_layout(template='plotly_dark')
    # fig.show()
    fig.write_image("heat_map.jpg")
    
    return data
    
data_vis()
