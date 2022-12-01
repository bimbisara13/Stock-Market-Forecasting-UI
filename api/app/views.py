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
        best_model = data['best_model']
        mape = data['MAPE']
        predictions = data['predictions']
        df = data['df_plot']
        model = MLModels()
        model.stock_name = stock_name
        model.best_model = best_model
        model.mape = mape
        model.save()
        return Response(data, status=200)
