# import the libraries
import pandas as pd 






def _data_preprocessing (df, stock_name) :
    
    df['Date'] = pd.to_datetime(df['Date'])
    df.sort_values('Date', inplace = True)
    df["Stock_Name"] = stock_name

    max_date = df["Date"].max() 
    min_date = df["Date"].min()

    #genearate missing_dates and fill NaN values using forward fill method
    df_date = pd.DataFrame({'Date':pd.date_range(start=min_date, end=max_date)})
    df_date = df_date.merge(df, on  = 'Date',  how = 'left')
    df_date.fillna({'Stock Name':"Apple"}, inplace = True)
    df_date.ffill(axis = 0, inplace = True)
    return df_date



def _feature_engineering(df):

    # temporal features
    df['day'] = df['Date'].dt.day
    df['month'] = df['Date'].dt.month
    df['year'] = df['Date'].dt.year

 
    #lag features
    for x in range(1,7):
    # df_data['lag_high' + str(x)] = df_data.groupby('Stock Name')['High'].shift(x)
        df['lag_' + str(x)] = df.groupby('Stock_Name')['Low'].shift(x)


  # moving average features & standard deviation features
  # for fea in range (2,6):
  #   df_data['ma_high' +  str(fea)] = df_data.groupby('Stock Name')['High'].transform(lambda x: x.rolling(fea).mean().shift(1))
  #   df_data['std_high' +  str(fea)] = df_data.groupby('Stock Name')['High'].transform(lambda x: x.rolling(fea).std().shift(1))

  #   df_data['ma_low' +  str(fea)] = df_data.groupby('Stock Name')['Low'].transform(lambda x: x.rolling(fea).mean().shift(1))
  #   df_data['std_low' +  str(fea)] = df_data.groupby('Stock Name')['Low'].transform(lambda x: x.rolling(fea).std().shift(1))

    return df









