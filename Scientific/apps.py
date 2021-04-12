from django.apps import AppConfig


class SimpleConfig(AppConfig):
    name = 'posts'


class MigrateConfig(AppConfig):
    name = 'migrate'