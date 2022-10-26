import boto3
s3 = boto3.resource('s3')


tickers = ['WMT', 'AMZN' , 'AAPL' , 'CVS.F' , 'UNH' , 'XOM' , 'BRK-A' , 'GOOGL' , 'MCK' , 'ABC' , 'COST' , 'CI' , 'T' , 'MSFT' , 'CAH' , 'CVX' , 'HD' , 'WBA' , 'MPC' , 'ELV' , 'KR' , 'F' , 'VZ' , 'JPM' , 'GM' , 'CNC' , 'META' , 'CMCSA' , 'PSX' , 'VLO' , 'DELL' , 'TGT' , 'FNMA' , 'UPS' , 'LOW' , 'BAC' , 'JNJ' , 'ADM' , 'FDX' , 'HUM' , 'WFC' , 'STFGX' , 'PFE' , 'C' , 'PEP' , 'INTC' , 'PG' , 'GE' , 'IBM' , 'MET'  ]


for com in tickers :


    s3.meta.client.upload_file('C:\\Users\\mabbasi4\\Documents\\Courses\\5337\\AWS\\scripts\\' + com + '\\' + com + '.csv',
 'fortunestockdata',com + '/' + com + '.csv')