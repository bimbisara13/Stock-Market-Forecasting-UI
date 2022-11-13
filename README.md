# Stock-Market-Forecasting-UI
Predicting the future value of a stock traded on a stock exchange for reaping profits using supervised machine learning. 

## Running the application

```
cd stock-market-forecasting/

npm install

npm start
```

## Running the django application

```
pip install -r requirements.txt

cd api/

python3 manage.py runserver

```

## Perform request

```
 curl -X POST http://127.0.0.1:8000 -H "Content-Type: application/json" -d '{"stock_name": "GOOGL"}'

```
