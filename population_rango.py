import os
import django

    
def add_page(cat,title,url,views=0):
    p = Page.objects.get_or_create(category=cat,title=title,url=url,views=views)[0]
    return p

def add_cat(name,views=0,likes=0):
    c = Category.objects.get_or_create(name=name,views=views,likes=likes)[0]
    return c

def populate():
    python_cat = add_cat(name='Python',views=128,likes=64)
        
    add_page(cat=python_cat,title="Official Python Site",url="www.python.org")
    add_page(cat=python_cat,title="test",url="www.developmentops.co.uk")
        
    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
           print (c,p)
        
if __name__ == '__main__':
    print ("Starting Rango population Script",)    
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'twd.settings')
    django.setup()
    #from django.conf import settings
    #from django.db import models
    #from django.contrib.auth.models import User
    from rango.models import Category, Page 
    populate()