from django.shortcuts import render,redirect
from .models import *
from .forms import *

# Create your views here.
def index(request):
    return render(request,"index.html")

def contect(request):
    if request.method == "POST":
        form = contect_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request,"contectus.html",{'form':contect_form()})

def login(request):
    return render(request,"login.html")