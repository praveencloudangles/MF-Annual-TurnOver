from data_cleaning import data_preproc

def feat_eng():
    data = data_preproc()
    print(data)
    
    data.to_csv("Mutual_Fund_Annual_Turnover.csv", index=False)
    
    return data
    
feat_eng()
