from django.shortcuts import render, render_to_response, RequestContext
from forms import MyUserCreationForm
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.core.context_processors import csrf

# Create your views here.

def reg_user(request):
    # TODO: fix Exception Value: reg_user() takes exactly 1 argument (0 given)
    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect("/regsuccess/")
    else:
        form = MyUserCreationForm()
    return render_to_response("registration.html", {"form":form}, context_instance=RequestContext(request))
