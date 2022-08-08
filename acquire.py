import env
import numpy as np
import scipy.stats as stats
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import seaborn as sns
from pydataset import data
import os

def get_db_url(hostname, username, password, database):
    url = f'mysql+pymysql://{username}:{password}@{hostname}/{database}'
    return url

def new_tit_df():

    url_tit = get_db_url(env.hostname, env.username, env.password, "titanic_db")
    query = pd.read_sql('''SELECT * \
                         FROM passengers; ''', url_tit)

def get_titanic_data():
    filename = "titanic.csv"
    
    # if file is available locally, read it
    if os.path.isfile(filename):
        return pd.read_csv(filename)
    
    # if file not available locally, acquire data from SQL database
    # and write it as csv locally for future use
    else:
        # read the SQL query into a dataframe
        df = new_tit_df()
        
        # Write that dataframe to disk for later. Called "caching" the data for later.
        df.to_csv(filename)

        # Return the dataframe to the calling code
        return df  

def new_iris_df():

    url_iris = get_db_url(env.hostname, env.username, env.password, "iris_db")
    query = pd.read_sql('''SELECT * \
                         FROM species \
                         JOIN measurements \
                            USING(species_id); ''', url_iris)
    return query

def get_iris_data():
    filename = "iris.csv"
    
    # if file is available locally, read it
    if os.path.isfile(filename):
        return pd.read_csv(filename)
    
    # if file not available locally, acquire data from SQL database
    # and write it as csv locally for future use
    else:
        # read the SQL query into a dataframe
        df = new_iris_df()
        
        # Write that dataframe to disk for later. Called "caching" the data for later.
        df.to_csv(filename)

        # Return the dataframe to the calling code
        return df  


def get_telco_data():
    
    sql_query = ''' \
                select * from customers \
                join contract_types using (contract_type_id) \
                join internet_service_types using (internet_service_type_id) \
                join payment_types using (payment_type_id); \
                '''
    
    # Read in DataFrame from Codeup db.
    df = pd.read_sql(sql_query, get_db_url(env.hostname, env.username,env.password, "telco_churn"))
    
    return df