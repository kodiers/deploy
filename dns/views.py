from django.shortcuts import render, render_to_response, RequestContext
from forms import MyUserCreationForm
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.core.context_processors import csrf

# Create your views here.

def reg_user(request):
    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            # Edit zone file
            return HttpResponseRedirect("/regsuccess/")
    else:
        form = MyUserCreationForm()
    return render_to_response("registration.html", {"form":form}, context_instance=RequestContext(request))

def reg_success(request):
    return render_to_response("regsuccess.html", context_instance=RequestContext(request))
