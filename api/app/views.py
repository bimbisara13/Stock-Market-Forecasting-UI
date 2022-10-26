from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from .apps import AppConfig
from ml.models.model import main

class Prediction(APIView):
    def get(self, request):
        response_dict = {
            'Hello': 'World'
        }
        return Response(response_dict)
    
    def post(self, request):
        stock_name = request.data['stock_name']
        accuracy = main(stock_name)
        print(accuracy)
        # predict using the model
        response_dict = {
            "accuracy": accuracy
        }
        print(response_dict)
        return Response(response_dict, status=200)