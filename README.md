# Django site with user login, messaging and message notifications


Django project with

1) Login with self-hosted (email-based) auth and auth via fb, gmail etc, 
2) User-user messages 
3) New message notification ability


## Modules

django-allauth for allauth 
postman for messages 
django-notifications-hq for notifications


## Versions/branches

Authentication, user logins only on master
\+ messaging and notifications on Add-Django-Notifictaions




## Motivation

One of the non-profit projects we were working with needed a Django set up that could handle user-user messages and a pollable notification mechanism for those messages. Django is not traditionally developed for a social network style application, but this is an example implementation of how this functionality might be provided. Feel free to use as a base for other projects.
