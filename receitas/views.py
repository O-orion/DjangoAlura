from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return HttpResponse('<h1>JESUS CRISTO É O SENHOR!</h1><br> <h2>Obrigado por tudo!</h2>')