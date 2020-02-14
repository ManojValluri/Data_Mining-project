# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 19:54:37 2020

@author: saketh
"""

import pandas as pd
import numpy as np

wq_data =pd.read_csv("complete_dataset.csv",encoding='iso-8859-1')

small_set = wq_data.sample(10);

print("Sample data:\n")
print( small_set )
#no.of missing values each attribute

missing_data = wq_data.isnull().sum();
print("Missing data:\n")
print( missing_data )

total_cells= np.product(wq_data.shape)
total_missing_values = missing_data.sum();


print("Percentage of missing data:" +str ( (total_missing_values/total_cells)*100) )