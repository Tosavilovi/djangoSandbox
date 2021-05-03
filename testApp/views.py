from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<H3>This is the test page</H3>")
# Create your views here.

def index_html(request):
    return render(request, 'testApp/homePage.html')

def contacts(request):
    return render(request, 'testApp/contacts.html', {'values':['Если у вас есть вопросы, вы можете их задать по телефону', '8-923-388-44-55']})

# Create your views here.
