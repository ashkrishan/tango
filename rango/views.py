from urllib.parse import unquote
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.core.exceptions import ValidationError
from django.contrib.auth.decorators import login_required
from rango.models import Category,Page
from rango.forms import CategoryForm ,PageForm, UserForm, UserProfileForm


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

    context_dict = {'category_name': category_name, 'category_name_url' : category_name_url}    
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
            page = form.save(commit=False)
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
        form = PageForm()
    return render(request,'add_page.html', {'category_name': category_name, 'category_name_url': category_name_url, 'form':form})
    

def register(request):
    
    registered = False
    
    if request.method =='POST':
        user_form =  UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            
            profile = profile_form.save(commit=False)
            profile.user = user
            
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
                
            profile.save()
            
            registered = True
            
        else:
            print (user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
    
    return render(request, 'register.html', {'user_form': user_form, 'profile_form': profile_form, 'registered': registered})
    
    
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect('/rango/')
            else:
                return HttpResponse("Your account is disabled")
        else:
            print (username,password)
            return HttpResponse("Invalid details")
            
    else:
        return render(request,'login.html', {})
        
@login_required
def restricted(request):
    return HttpResponse("You are logged in that is why you can see this text")
    
@login_required
def user_logout(request):
    logout(request)
    