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


from .reading_files_s3 import _data_preprocessing,_feature_engineering



def _model (df) :

    max_date = df["Date"].max()
    lag_columns = []
    for i in range (1,7):
        lag_columns.append('lag_' + str(i))

 

    col_list  = [col for col in df if col.startswith('lag')] + ["Low"]

    df_data = df[ ["Date"] + col_list ]

    df_data.dropna(inplace = True)
    df_data.reset_index(drop = True,inplace = True)


    #Train-Test split
    df_data.sort_values(by='Date')
    # df_data.sort()
    # df_data['Date'] = df_data['Date'].astype("string")
    date_split = max_date - pd.DateOffset(30)


    train_data = df_data[df_data['Date'] <= date_split]
    test_data = df_data[df_data['Date'] > date_split]


    train_data.dropna(inplace=True)

    # Assigning values to x and y

    drop_cols = ['Low',  'Date']
    traincols = train_data.columns
    feature_cols  = list(set(traincols)-set(drop_cols))
    label_col = 'Low'

    x = train_data[feature_cols]
    y = train_data[label_col]


    #Model Training and parameter tuning using grid search

    reg_xgb = xgb.XGBRegressor()
    grid_values = {'max_depth': [10,20],'n_estimators':[1000 ,500],'learning_rate':[0.01,0.1,1]}
    grid_reg_xgb = GridSearchCV(reg_xgb, param_grid = grid_values)
    print ("Model Training...........")
    grid_reg_xgb.fit(x, y)
    # pickle.dump(grid_reg_xgb, open('model.pkl', 'wb'))

    filename = 'XgBoost_model.joblib'
    # joblib.dump(grid_reg_xgb, filename)

    test_data.reset_index(drop=True,inplace=True)

    testpart = test_data[test_data['Date']== date_split + pd.DateOffset(1)]
    testpart.reset_index(drop=True, inplace = True)
    keyd = testpart.loc[[0], ['Date']]

    predicted_xgb =  grid_reg_xgb.predict(testpart[feature_cols])


    lastlag = testpart



    finalpred = keyd.copy()

# finalpred['YearWeek']=str(firstweek)
    finalpred['Actual']=testpart['Low'][0]
    finalpred['Predicted_xgb']=list(predicted_xgb)[0]

    finaloutput = pd.DataFrame()



    for num, dat in enumerate (test_data.Date):
          if num != 0 :
            testpart = test_data[test_data['Date']== dat]
            testpart = testpart.reset_index(drop=True)
            
            #updating lags
            testpart[lag_columns[1 : ]] = lastlag[lag_columns[0 : -1]].values
            testpart['lag1']=list(finalpred['Predicted_xgb'])[-1]

          #   testpart['lags_mean'] = testpart[lag_columns].mean(axis=1)
          #   testpart['lags_sum'] = testpart[lag_columns].sum(axis=1)
          #   testpart['lags_std'] = testpart[lag_columns].std(axis=1)

            predicted_xgb =  grid_reg_xgb.predict(testpart[feature_cols])

            partpred=keyd.copy()
            partpred['Date']=testpart['Date'][0]
            partpred['Actual']=testpart['Low'][0]
            partpred['Predicted_xgb']=list(predicted_xgb)[0]
            # partpred['Predicted_rf']=list(predicted_rf)[0]
            # partpred['Predicted_lasso']=list(predicted_lasso)[0]
            # partpred['Predicted_ridge']=list(predicted_ridge)[0]
            

            finalpred = finalpred.append(partpred, ignore_index = True, sort = False)
            lastlag = testpart


    finaloutput  = finaloutput.append(finalpred, ignore_index = True, sort = False)
    return finaloutput


def _accuracy (df) :
    # calculate MAE
    error = mean_squared_error(df["Actual"], df["Predicted_xgb"], squared=False)
  

    # print("Root Mean Squared Error : " + str(error))
    return error


# if __name__ == "__main__":
def main(stock_name):
    #parameters
    # stock_name = 'GOOGL'

    # Read data from s3
    # client = boto3.client('s3')
    # path = 's3://fortunestockdata/'+ stock_name + '/' + stock_name +  '.csv'

    # read folders from current directory

    import os

    path = os.getcwd()
    path = path + '/' + 'ml' + '/' + 'models' + '/' + stock_name + '/' + stock_name + '.csv'
    df = pd.read_csv(path)
    # print(df.head())

    df_pre_process = _data_preprocessing(df, stock_name)
    df_feature_engineering = _feature_engineering(df_pre_process)

    df_model = _model(df_feature_engineering)

    df_accuracy  = _accuracy (df_model) 
    return df_accuracy




