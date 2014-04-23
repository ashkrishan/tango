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
        
    django_cat = add_cat(name='Django', views=100, likes=2000)    
    add_page(cat=django_cat,title="Django docs",url="www.djangoproject.com",views=5000)
    add_page(cat=django_cat,title="StackOverflow Questions",url="http://stackoverflow.com/questions/tagged/django",views=50)
    add_page(cat=django_cat,title="Django re-usable apps",url="https://www.djangopackages.com",views=20)    
    
    other_cat = add_cat(name="Misc Framework",views=14,likes=2)
    add_page(cat=other_cat,title="Flask",url="http://flask.pocoo.org/",views=5)
    add_page(cat=other_cat,title="Bottle",url="http://bottlepython.co.uk/",views=5)
    
    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
           print (c,p)
        
if __name__ == '__main__':
    print ("Starting Rango population Script",)    
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'twd.settings')
    django.setup()
    from rango.models import Category, Page 
    populate()