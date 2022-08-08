import numpy as np
import scipy.stats as stats
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import seaborn as sns
import os
import acquire

def prep_iris():

    df = acquire.get_iris_data()
    df = df.drop(columns=["species_id", "measurement_id"])
    df = df.rename(columns={"species_name": "species"})
    dummy_df = pd.get_dummies(df[["species"]], drop_first=True)
    df = pd.concat([df, dummy_df], axis=1)
    return df

def prep_telco():
    df = acquire.get_telco_data()
    df = df.drop(columns = ["contract_type", "payment_type",
                       "internet_service_type"])
    dummy_df = pd.get_dummies(df[["gender"]], drop_first=True)
    df = pd.concat([df, dummy_df], axis=1)
    return df
    
# Split your data
# #
# 
# 
#  Write a function to split your data into train, test and validate datasets. Add
# 
# 
#  this function to prepare.py.
# #
# 
# 
#  Run the function in your notebook on the Iris dataset, returning 3 datasets,
# 
# 
#  train_iris, validate_iris and test_iris.
# #
# 
# 
#  Run the function on the Titanic dataset, returning 3 datasets, train_titanic,
# 
# 
#  validate_titanic and test_titanic.
# #
# 
# 
#  Run the function on the Telco dataset, returning 3 datasets, train_telco,
# 
# 
#  validate_telco and test_telco.