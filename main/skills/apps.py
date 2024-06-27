from django.apps import AppConfig


class SkillsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'skills'


class CertificationsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'certification'