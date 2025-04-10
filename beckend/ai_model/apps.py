from django.apps import AppConfig
from .ml import load_rbs_model,load_freq_model,load_rl_model

class AiModelConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ai_model'

    def ready(self):
    # Load the model when the app is ready (only once)
        load_rbs_model()
        load_freq_model()
        load_rl_model()

