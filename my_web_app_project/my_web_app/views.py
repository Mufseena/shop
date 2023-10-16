from django.http import HttpResponse
from django.shortcuts import render
from .models import Web_app


# Create your views here.
def index(request):
    web = Web_app.objects.all()
    return render(request,"index.html",{'web':web})

def detail(request,id):
     web = Web_app.objects.get(id=id)
     return render(request,"detail.html",{'web':web})