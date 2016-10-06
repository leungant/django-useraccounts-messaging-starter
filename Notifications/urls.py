"""Notifications URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from YouveGotMail.views import ProfileView, IndexView
import notifications.urls

urlpatterns = [
    url(r'^accounts/', include('allauth.urls')),
    url(r'accounts/profile', ProfileView.as_view(), name='Profile View'),
    url(r'^$', IndexView.as_view(), name='Index View'),
    # url(r'^send/(\w+)', send_message, name='send View'),
    url(r'^admin/', admin.site.urls),

    # django-postman
    url(r'^messages/', include('postman.urls', namespace='postman', app_name='postman')),
    # django-notifications-hq
    url('^inbox/notifications/', include(notifications.urls, namespace='notifications')),


]
