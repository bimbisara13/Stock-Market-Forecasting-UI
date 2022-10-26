import time
import datetime
import pandas as pd

import os




period1 = int(time.mktime(datetime.datetime(2019, 10, 1, 23, 59).timetuple()))
period2 = int(time.mktime(datetime.datetime(2022, 10, 31, 23, 59).timetuple()))
interval = '1d' # 1d, 1m



tickers = ['WMT', 'AMZN' , 'AAPL' , 'CVS.F' , 'UNH' , 'XOM' , 'BRK-A' , 'GOOGL' , 'MCK' , 'ABC' , 'COST' , 'CI' , 'T' , 'MSFT' , 'CAH' , 'CVX' , 'HD' , 'WBA' , 'MPC' , 'ELV' , 'KR' , 'F' , 'VZ' , 'JPM' , 'GM' , 'CNC' , 'META' , 'CMCSA' , 'PSX' , 'VLO' , 'DELL' , 'TGT' , 'FNMA' , 'UPS' , 'LOW' , 'BAC' , 'JNJ' , 'ADM' , 'FDX' , 'HUM' , 'WFC' , 'STFGX' , 'PFE' , 'C' , 'PEP' , 'INTC' , 'PG' , 'GE' , 'IBM' , 'MET'  ]

for ticker in tickers :

    query_string = f'https://query1.finance.yahoo.com/v7/finance/download/{ticker}?period1={period1}&period2={period2}&interval={interval}&events=history&includeAdjustedClose=true'

    df = pd.read_csv(query_string)

    print (df.columns)

    # df = df[["Date", "High", "Low"]]
    # print(df)



    outname = ticker + '.csv'
    outdir = f"{ticker}" 

    if not os.path.exists(outdir):
        os.mkdir(outdir)

    fullname = os.path.join(outdir, outname)
    print (fullname)    

    df.to_csv(fullname)




# df.to_csv(r'C:\Users\mabbasi4\Documents\Courses\5337\Project\Data\Datasets\AAPL\AAPL.csv')