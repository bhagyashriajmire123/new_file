from django.http import HttpResponse
from django.shortcuts import render

from app.forms import NewUserForm

# Create your views here.


def homepage(request):
    return render(request, "home.html")


def register_request(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save() 
        return HttpResponse("success")
    else:
        return render(request , "register.html", context={"register_form": NewUserForm()})