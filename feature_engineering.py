from datavisualization import data_vis

def feat_eng():
    data = data_vis()
    print(data)
    
    data.to_csv("Mutual_Fund_Annual_Turnover.csv", index=False)
    
    return data
    
feat_eng()