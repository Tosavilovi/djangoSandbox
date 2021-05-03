from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<H3>Hell world!!!</H3>")
# Create your views here.

def index_html(request):
    return render(request, 'testPages/homePage.html')