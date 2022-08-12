import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy.stats as stats
import seaborn as sns
from acquire import *
from prepare import *
from pydataset import data
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split



def cat_vis(train, col, target):

    sns.barplot(x = col, y = target, data = train)
    target_rate = train[target].mean()
    plt.axhline(target_rate, label = "average " + target + " rate")
    plt.legend()
    plt.show()
    
def cat_test(train, col, target):
    
    α = 0.05
    null_hyp = col + " and " + target + " are independent."
    alt_hyp = "There appears to be a relationship between " + target + " and " + col + "."
    observed = pd.crosstab(train[target], train[col])
    chi2, p, degf, expected = stats.chi2_contingency(observed)
    if p < α:
        print("We reject the null hypothesis that", null_hyp)
        print(alt_hyp)
    else:
        print("We fail to reject the null hypothesis that", null_hyp)
        print("There appears to be no relationship between ", target, "and ", col, ".")

def cat_analysis(train, col, target):

    cat_vis(train, col, target)
    cat_test(train, col, target)

def dtypes_to_list(df):

    num_type_list = []
    cat_type_list = []

    for column in df:

        col_type =  df[column].dtype

        if col_type == "object" : 
        
            cat_type_list.append([column, col_type])
    
        if col_type in ["int64", "uint8"] and \
             ((df[column].max() + 1) / df[column].nunique())  == 1 :

            cat_type_list.append([column, col_type])

        if col_type in ["float64", "int64", "uint8"] and \
            ((df[column].max() + 1) / df[column].nunique()) != 1 :

            num_type_list.append([column, col_type])

    return "num_vars = ", num_type_list, "cat_vars = ", cat_type_list

    
         