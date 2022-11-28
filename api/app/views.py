from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from .apps import AppConfig
from ml.models.model import main
from .models import MLModels

class Prediction(APIView):
    
    def get(self, request):
        data = {
            'Hello': 'World'
        }
        return Response(data, status=200)

    def post(self, request):
        stock_name = request.data['stock_name']
        data = main(stock_name)
        df_accuracy = data['df_accuracy']
        error_xgb = df_accuracy['error_xgb']
        error_rf = df_accuracy['error_rf']
        error_ridge = df_accuracy['error_ridge']
        error_lasso = df_accuracy['error_lasso']
        model = MLModels()
        model.xgboost = error_xgb
        model.random_forest = error_rf
        model.lasso = error_lasso
        model.ridge = error_ridge
        model.save()
        return Response(data, status=200)
