# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 11:21:58 2020

@author: saketh
"""
import pandas as pd
import numpy as np

wq_data =pd.read_csv("complete_dataset.csv",encoding='iso-8859-1')

#replacing missing values with column means
means =wq_data.mean();


wq_data=wq_data.fillna(means);

#Outlier analysis 

#Records are deleted if no State is mentioned
missing_state=pd.notnull(wq_data['STATE'])
wq_final_data=wq_data[missing_state];

missing_data = wq_final_data.isnull().sum();
total_cells= np.product(wq_final_data.shape)
total_missing_values = missing_data.sum();

print("Total missing values:"+str(total_missing_values))
print("Percentage of missing data:" +str ( (total_missing_values/total_cells)*100) )

wq_final_data.to_csv("combined_csv_missingval_mean.csv", index=False, encoding='iso-8859-1');