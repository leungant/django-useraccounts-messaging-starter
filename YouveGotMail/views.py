from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect, HttpResponse
from django.views.decorators.csrf import csrf_exempt


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


def send_message(request, username):
    print(username)
    return HttpResponse("sending message to %s\n" % username)
    # render(request.GET.to)
    # return


@csrf_exempt
def logout(request):
    logout()
    render(request)
    return HttpResponseRedirect('/accounts/login')
