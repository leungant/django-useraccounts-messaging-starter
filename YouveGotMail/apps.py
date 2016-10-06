from django.apps import AppConfig


class YouvegotmailConfig(AppConfig):
    name = 'YouveGotMail'

    # for loading django-notifications-signal
    # def ready(self):
    #   import YouveGotMail.signals
