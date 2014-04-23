from django.shortcuts import render
from rango.models import Category,Page


def index(request):
    category_list = Category.objects.order_by('-likes')[:2]
    
    for category in category_list:
        category.url = category.name.replace(' ', '_')
        
    context_dict = {"categories": category_list}
    return render(request,'home.html', context_dict)
    

def about_page(request):
    return render(request, 'about.html')
    

def category(request, category_name_url):
    #Encode spaces 
    category_name = category_name_url.replace("_"," ")    
    context_dict = {'category_name': category_name}    
    try:
        cat = Category.objects.get(name=category_name)
        pages = Page.objects.filter(category=cat)
        context_dict['pages'] = pages
        context_dict['category'] = cat
    except Category.DoesNotExist:
        pass
    return render(request, 'category.html', context_dict)
    