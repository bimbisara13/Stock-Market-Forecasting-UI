from django.db import models

# Create your models here.
class MLModels(models.Model):
    stock_name = models.CharField(max_length=20)
    best_model = models.CharField(max_length=20)
    mape = models.FloatField()
    
    def __str__(self):
        message = f'stock_name: {self.stock_name}\n' \
                f'best_model: {self.best_model}\n' \
                f'mape: {self.mape}\n'
        return message