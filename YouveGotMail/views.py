from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect, HttpResponse
from django.views.decorators.csrf import csrf_exempt

from allauth.account.views import SignupView, LoginView

# Create your views here.

class ProfileView(TemplateView):
    """
    The Profile view.
    """
    template_name = "profile.html"


class IndexView(TemplateView):
    """
    The index view.
    """
    template_name = "index.html"


@csrf_exempt
def logout(request):
    logout()
    render(request)
    return HttpResponseRedirect('/accounts/login')


class NotificationsLoginView(LoginView):
    """ override Allauth login view """
    template_name = "login.html"


class NotificationsSignupView(SignupView):
    """ override Allauth signup view """
    template_name = "signup.html"
