import numpy as np
import scipy.stats as stats
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import seaborn as sns
import os
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from acquire import *

def prep_iris(df):

    df = df.drop(columns=["species_id", "measurement_id"])
    df = df.rename(columns={"species_name": "species"})
    dummy_df = pd.get_dummies(df[["species"]], drop_first=True)
    df = pd.concat([df, dummy_df], axis=1)
    return df



def prep_tit(titanic):
    titanic = titanic.drop(columns=['embarked','class', 'age','deck'])
    dummy_df = pd.get_dummies(data=titanic[['sex','embark_town']], drop_first=True)
    titanic = pd.concat([titanic, dummy_df], axis=1)
    
    return titanic



def prep_telco(telco):
    telco = telco.drop(columns=['internet_service_type_id', 'contract_type_id', 'payment_type_id'])

    telco['gender_encoded'] = telco.gender.map({'Female': 1, 'Male': 0})
    telco['partner_encoded'] = telco.partner.map({'Yes': 1, 'No': 0})
    telco['dependents_encoded'] = telco.dependents.map({'Yes': 1, 'No': 0})
    telco['phone_service_encoded'] = telco.phone_service.map({'Yes': 1, 'No': 0})
    telco['paperless_billing_encoded'] = telco.paperless_billing.map({'Yes': 1, 'No': 0})
    telco['churn_encoded'] = telco.churn.map({'Yes': 1, 'No': 0})
    
    dummy_df = pd.get_dummies(telco[['multiple_lines', \
                              'online_security', \
                              'online_backup', \
                              'device_protection', \
                              'tech_support', \
                              'streaming_tv', \
                              'streaming_movies', \
                              'contract_type', \
                              'internet_service_type', \
                              'payment_type'
                            ]],
                              drop_first=True)
    telco = pd.concat( [telco, dummy_df], axis=1 )
    
    return telco
    
# Split your data
# #
# 
# 
#  Write a function to split your data into train, test and validate datasets. Addthis function to prepare.py.



def prep_split(df, target):
    
    train, test = train_test_split(df, test_size=.2, random_state=269, 
    stratify = df[target])
    train, validate = train_test_split(train, test_size=.25, random_state=269, stratify = train[target])
    
    return train, validate, test

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

