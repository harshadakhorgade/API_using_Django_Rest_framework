from django.apps import AppConfig


class ApiAppConfig(AppConfig):
    # This attribute sets the default type for the primary key field in models within this app. 'django.db.models.BigAutoField' is a 64-bit integer that auto-increments, which is useful for handling larger databases.
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api_app'
