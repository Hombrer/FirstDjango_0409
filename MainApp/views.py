from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def home(request):
    text = """ <h1>"Изучаем django"</h1><br>
            <strong>Автор</strong>: <i>Шиховцов В.В.</i>
           """
    return HttpResponse(text)