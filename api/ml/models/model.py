from sklearn.model_selection import train_test_split
import xgboost as xgb
import pandas as pd
import numpy as np
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import mean_squared_error
from math import sqrt
import matplotlib.pyplot as plt
# import boto3
import pickle
import joblib
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import Ridge, Lasso
import matplotlib.dates as mdates


from .reading_files_s3 import _data_preprocessing,_feature_engineering
from .model_training_predictions import _model_training

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
    # calculate RMSE
    print (df.head(2))
    error_xgb = mean_squared_error(df["Actual"], df["XgBoost"], squared=False)
    error_rf = mean_squared_error(df["Actual"], df["Random Forest"], squared=False)
    error_lasso = mean_squared_error(df["Actual"], df["Lasso"], squared=False)
    error_ridge = mean_squared_error(df["Actual"], df["Ridge"], squared=False)
  

    print("XgBoost RMSE : " + str(error_xgb))
    print("Random Forest RMSE : " + str(error_rf))
    print("Lasso RMSE : " + str(error_lasso))
    print("Ridge RMSE : " + str(error_ridge))
    return {
        "error_xgb": error_xgb,
        "error_rf": error_rf,
        "error_lasso": error_lasso,
        "error_ridge": error_ridge
    }


def _plot (df) :


# first plot with X and Y data

    # fig = plt.figure(figsize=(6,5))
    # fig, ax = plt.subplots(2, 2)
    
    # # Adding axes on the figure
    # # ax = fig.add_subplot(111)
    # # fig.autofmt_xdate()

    # # ax.plot(df["Date"], df["Actual"], '-ro', label="Actual")

    # # ax.plot(df["Date"], df["XgBoost"], '-bo', label = "Predicted")

    # ax[0, 0].plot(df["Date"], df["Actual"], '-ro', label="Actual")
    # ax[0, 0].plot(df["Date"], df["XgBoost"], '-bo', label="Predicted")
    # # xfmt = mdates.DateFormatter('%y-%m-%d')
    # # ax[0, 0].xaxis.set_major_formatter(xfmt)
    # ax[0, 0].set_title("XgBoost")
    
    # # For Random Forest
    # ax[0, 1].plot(df["Date"], df["Actual"], '-ro', label="Actual")
    # ax[0, 1].plot(df["Date"], df["Random Forest"], '-bo', label="Predicted")
    # ax[0, 1].set_title("Random Forest")
    
    # # For Lasso
    # ax[1, 0].plot(df["Date"], df["Actual"], '-ro', label="Actual")
    # ax[1, 0].plot(df["Date"], df["Lasso"], '-bo', label="Predicted")
    # ax[1, 0].set_title("Lasso")



    # ax[1, 1].plot(df["Date"], df["Actual"], '-ro', label="Actual")
    # ax[1, 1].plot(df["Date"], df["Ridge"], '-bo', label="Predicted")
    # ax[1, 1].set_title("Ridge")
  
    # ax.legend()
    # ax.set_xlabel("Date")
    # ax.set_ylabel("Forecast")
    # ax.set_title('Forecasts')
    # xfmt = mdates.DateFormatter('%y-%m-%d')
    # ax.xaxis.set_major_formatter(xfmt)
    # plt.savefig("Plot_Lasso.png")
    # plt.show()
    return df



# if __name__ == "__main__":
def main(stock_name):
    
    #parameters
    # stock_name = 'GOOG'


    # Read data from s3
    # client = boto3.client('s3')
    # path = 's3://fortunestockdata/'+ stock_name + '/' + stock_name +  '.csv'
    
    import os
    path = os.getcwd()
    # path = path + '/' + stock_name + '/' + stock_name + '.csv'
    path = path + '/' + 'ml' + '/' + 'models' + '/' + stock_name + '/' + stock_name + '.csv'

    df = pd.read_csv(path)

    #Calling functions
    df_pre_process = _data_preprocessing(df, stock_name)
    df_feature_engineering = _feature_engineering(df_pre_process)
    df_model = _models(df_feature_engineering, 7)
    df_accuracy  = _accuracy (df_model)
    df_plot = _plot(df_model)
    return {
        "df_accuracy": df_accuracy,
        "df_plot": df_plot
    }
















