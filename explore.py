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


def dtypes_to_list(df):

    num_type_list, cat_type_list = [], []

    for column in df:

        col_type =  df[column].dtype

        if col_type == "object" : 
        
            cat_type_list.append(column)
    
        if np.issubdtype(df[column], np.number) and \
             ((df[column].max() + 1) / df[column].nunique())  == 1 :

            cat_type_list.append(column)

        if np.issubdtype(df[column], np.number) and \
            ((df[column].max() + 1) / df[column].nunique()) != 1 :

            num_type_list.append(column)

    return num_type_list, cat_type_list

def cat_vis(train, cat_type_list):

    # sns.barplot(x = col, y = target, data = train)
    # target_rate = train[target].mean()
    # plt.axhline(target_rate, label = "average " + target + " rate")
    # plt.legend()
    # plt.show()
    for col in cat_type_list:

        print(col)
        print(train[col].value_counts())
        print(train[col].value_counts(normalize = True) * 100)
        sns.countplot(x=col, data=train)
        plt.show()
    
def cat_test(train, target, cat_type_list):
    
    for col in cat_type_list:

        α = 0.05
        null_hyp = col + " and " + target + " are independent."
        alt_hyp = "There appears to be a relationship between " + target + " and " + col + ".\n"
        observed = pd.crosstab(train[target], train[col])
        chi2, p, degf, expected = stats.chi2_contingency(observed)
        if p < α:
            print("We reject the null hypothesis that", null_hyp)
            print(alt_hyp)
        else:
            print("We fail to reject the null hypothesis that", null_hyp)
            print("There appears to be no relationship between ", target, "and ", col, ".\n")

def cat_analysis(train, target, cat_type_list):

    cat_vis(train, cat_type_list)
    cat_test(train, target, cat_type_list)
    
         