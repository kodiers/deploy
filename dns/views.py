from django.shortcuts import render, render_to_response, RequestContext
from forms import MyUserCreationForm
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.core.context_processors import csrf
from functions import change_zone_file
FILEPATH = "/Users/kodiers/Desktop/PythonProjects/deploy/files/it-national.com" # path to zone file( shoul be in global settings

# Create your views here.

def reg_user(request):
    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            username = form.clean_username()
            form.save()
            # Edit zone file
            change_zone_file(FILEPATH, username)
            return HttpResponseRedirect("/regsuccess/")
    else:
        form = MyUserCreationForm()
    return render_to_response("registration.html", {"form":form}, context_instance=RequestContext(request))

def reg_success(request):
    return render_to_response("regsuccess.html", context_instance=RequestContext(request))
