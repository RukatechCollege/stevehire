from django.apps import AppConfig


class Myblog1Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'myblog1'

    def ready(self):
      import myblog1.signals
    
