from django.db import models

# Create your models here.
from django.views.generic import TemplateView

# from http://m-x.io/blog/how-to-use-django-postman-with-django-notifications/

"""Handle notification signals from django-postman and pass
them to django-notifications. Postman does not """

# In the app's models.py:

from django.contrib.auth.models import User

from notifications.signals import notify


def send(users=[], label='', extra_context={}):
    print("send fired")

    if label == 'postman_message':
        print("send in pm fired")
        msg = extra_context['pm_message']
        user = User.objects.get(pk=msg.sender_id)
        notify.send(user, recipient=users[0], verb='New message', description=msg.subject)
