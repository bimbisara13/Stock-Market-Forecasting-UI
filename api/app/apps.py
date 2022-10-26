import os
import joblib
from django.apps import AppConfig
from django.conf import settings

class AppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app'
    MODEL_FILE = os.path.join(settings.MODELS, 'XgBoost_model.joblib')
    model = joblib.load(MODEL_FILE)
