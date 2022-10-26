from sklearn.model_selection import train_test_split
import xgboost as xgb
import pandas as pd
import numpy as np
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import mean_squared_error
from math import sqrt
import matplotlib.pyplot as plt
import boto3
import pickle
import joblib
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import Ridge, Lasso


from reading_files_s3 import _data_preprocessing,_feature_engineering
from model_training_predictions import _model_training

def _models (df, lags) :

    mdl_list = ["XgBoost", "Random Forest", "Lasso", "Ridge"]

    for mdl in mdl_list :
        
        res = _model_training(df, mdl, lags)
        if mdl == "XgBoost":
            newres = res
        else :
            newres[mdl] = res[mdl]
    # print (newres.head(3))
    return newres








def _accuracy (df) :
    # calculate MAE
    error_xgb = mean_squared_error(df["Actual"], df["XgBoost"], squared=False)
    error_rf = mean_squared_error(df["Actual"], df["Random Forest"], squared=False)
    error_lasso = mean_squared_error(df["Actual"], df["Lasso"], squared=False)
    error_ridge = mean_squared_error(df["Actual"], df["Ridge"], squared=False)
  

    print("XgBoost RMSE : " + str(error_xgb))
    print("Random Forest RMSE : " + str(error_rf))
    print("Lasso RMSE : " + str(error_lasso))
    print("Ridge RMSE : " + str(error_ridge))

if __name__ == "__main__":

    #parameters
    stock_name = 'GOOG'


    # Read data from s3
    client = boto3.client('s3')
    path = 's3://fortunestockdata/'+ stock_name + '/' + stock_name +  '.csv'

    df = pd.read_csv(path)

    df_pre_process = _data_preprocessing(df, stock_name)
    df_feature_engineering = _feature_engineering(df_pre_process)

    df_model = _models(df_feature_engineering, 7)
    # print ("df_model", df_model)

    df_accuracy  = _accuracy (df_model) 
    
















