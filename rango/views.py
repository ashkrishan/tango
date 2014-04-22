from django.shortcuts import render
#from django.http import HttpResponse
#from django.template import RequestContext


def index(request):
    context_dict = {"boldmessage": "Welcome to space and time. Event horizon"}
    return render(request,'home.html', context_dict)
    
def about_page(request):
    return render(request, 'about.html')