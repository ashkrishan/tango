#from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    #response = HttpResponse("An app")
    return HttpResponse("an app <a href='/rango/about/'>About page</a>")
    
def about_page(request):
    return HttpResponse("Here is about page <a href='/rango/'>Home page</a>")