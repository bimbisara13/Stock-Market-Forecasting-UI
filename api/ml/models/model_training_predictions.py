from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import Ridge, Lasso
import xgboost as xgb
from sklearn.model_selection import GridSearchCV
import pandas as pd


def _model_training (df, model, lags) :

    max_date = df["Date"].max()
    lag_columns = []
    for i in range (1,lags):
        lag_columns.append('lag_' + str(i))


    col_list  = [col for col in df if col.startswith('lag')] + ["Low"]
    df_data = df[ ["Date"] + col_list ]
    df_data.dropna(inplace = True)
    df_data.reset_index(drop = True,inplace = True)


    df_data.sort_values(by='Date')
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

    if model == "XgBoost":
        model_name = xgb.XGBRegressor()
        # grid_values = {'max_depth': [10,20],'n_estimators':[1000 ,500],'learning_rate':[0.01,0.1,1]}
        # model_name = GridSearchCV(reg_xgb, param_grid = grid_values)
        # print (" XgBoost Model Training...........")
        model_name.fit(x, y)

    # pickle.dump(grid_reg_xgb, open('model.pkl', 'wb'))

    # filename = 'XgBoost_model.joblib'
    # joblib.dump(grid_reg_xgb, filename)
    elif model == "Random Forest" :
        model_name = RandomForestRegressor()
        print ("RandomForest Model Training...........")
        model_name.fit(x, y)

    elif model == "Ridge" : 

        print ("Ridge Model Training")
        model_name = Ridge()
        model_name.fit(x, y)

    elif model == "Lasso":

        print ("Lasso Model Training")
        model_name = Lasso()
        model_name.fit(x, y)




    test_data.reset_index(drop=True,inplace=True)

    testpart = test_data[test_data['Date']== date_split + pd.DateOffset(1)]
    testpart.reset_index(drop=True, inplace = True)
    keyd = testpart.loc[[0], ['Date']]

    predicted_xgb =  model_name.predict(testpart[feature_cols])


    lastlag = testpart



    finalpred = keyd.copy()

# finalpred['YearWeek']=str(firstweek)
    finalpred['Actual']=testpart['Low'][0]
    finalpred[model]=list(predicted_xgb)[0]

    finaloutput = pd.DataFrame()



    for num, dat in enumerate (test_data.Date):
          if num != 0 :
            testpart = test_data[test_data['Date']== dat]
            testpart = testpart.reset_index(drop=True)
            
            #updating lags
            testpart[lag_columns[1 : ]] = lastlag[lag_columns[0 : -1]].values
            testpart['lag1']=list(finalpred[model])[-1]

          #   testpart['lags_mean'] = testpart[lag_columns].mean(axis=1)
          #   testpart['lags_sum'] = testpart[lag_columns].sum(axis=1)
          #   testpart['lags_std'] = testpart[lag_columns].std(axis=1)

            predicted_xgb =  model_name.predict(testpart[feature_cols])

            partpred=keyd.copy()
            partpred['Date']=testpart['Date'][0]
            partpred['Actual']=testpart['Low'][0]
            partpred[model]=list(predicted_xgb)[0]
            # partpred['Predicted_rf']=list(predicted_rf)[0]
            # partpred['Predicted_lasso']=list(predicted_lasso)[0]
            # partpred['Predicted_ridge']=list(predicted_ridge)[0]
            

            finalpred = finalpred.append(partpred, ignore_index = True, sort = False)
            lastlag = testpart


    finaloutput  = finaloutput.append(finalpred, ignore_index = True, sort = False)
    return finaloutput






























    
    reg_xgb = xgb.XGBRegressor()
    grid_values = {'max_depth': [10,20],'n_estimators':[1000 ,500],'learning_rate':[0.01,0.1,1]}
    grid_reg_xgb = GridSearchCV(reg_xgb, param_grid = grid_values)
    print (" XgBoost Model Training...........")
    grid_reg_xgb = grid_reg_xgb.fit(x, y)
    # pickle.dump(grid_reg_xgb, open('model.pkl', 'wb'))

    # filename = 'XgBoost_model.joblib'
    # joblib.dump(grid_reg_xgb, filename)

    rf = RandomForestRegressor()
    print ("RandomForest Model Training...........")
    rf.fit(x, y)

    print ("Ridge Model Training")
    ridge = Ridge()
    ridge.fit(x, y)

    print ("Lasso Model Training")
    lasso = Lasso()
    lasso.fit(x, y)




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