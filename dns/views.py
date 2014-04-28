from django.shortcuts import render, render_to_response, RequestContext
from forms import MyUserCreationForm
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

def register_user(request):
    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect("/regsuccess/")
    else:
        form = MyUserCreationForm()
    return render_to_response("registration.html", {"form":form}, context_instance=RequestContext(request))
