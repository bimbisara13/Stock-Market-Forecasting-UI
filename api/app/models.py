from django.db import models

# Create your models here.
class MLModels(models.Model):
    xgboost = models.FloatField()
    random_forest = models.FloatField()
    lasso = models.FloatField()
    ridge = models.FloatField()

    def __str__(self):
        message = f'XgBoost: {self.xgboost}\n' \
                f'Random Forest: {self.random_forest}\n' \
                f'Lasso: {self.lasso}\n' \
                f'Ridge: {self.ridge}\n'
        return message