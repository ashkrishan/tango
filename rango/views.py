from urllib.parse import unquote
from django.shortcuts import render
from rango.models import Category,Page
from rango.forms import CategoryForm ,PageForm
from django.core.exceptions import ValidationError

#def encode_url_space(url_name):
    

def index(request):
    category_list = Category.objects.order_by('-likes')[:2]
    page_list = Page.objects.order_by('-views')[:3]

    context_dict = {"categories": category_list, "pages": page_list}
    return render(request,'home.html', context_dict)
    

def about_page(request):
    return render(request, 'about.html')
    

def category(request, category_name_url):
    category_name = unquote(category_name_url)

    context_dict = {'category_name': category_name}    
    try:
        cat = Category.objects.get(name=category_name)
        pages = Page.objects.filter(category=cat)
        context_dict['pages'] = pages
        context_dict['category'] = cat
    except Category.DoesNotExist:
        pass
    return render(request, 'category.html', context_dict)
    
def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
             form.save(commit=True)
             #return index(request)
        else:
            print(form.errors)
    else:
        form = CategoryForm()
        
    return render(request, 'add_category.html', {'form': form})
    
def add_page(request,category_name_url):
    category_name = unquote(category_name_url)
    
    if request.method=='POST':
        form = PageForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            try:
                cat = Category.objects.get(name=category_name)
                page.category = cat
            except Category.DoesNotExist:
                return render(request, 'add_category.html', {})
            except ValidationError:
                print (form.errors)
            
            page.views=0
            page.save()
            return category(request,category_name_url)
        else:
            print(form.errors)
    else:
        page = PageForm()
    return render(request,'add_page.html', {'category_name': category_name, 'category_name_url': category_name_url, 'form':form})
    
    
    
        