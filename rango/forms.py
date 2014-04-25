from django import forms
from rango.models import Category,Page, UserProfile
from django.contrib.auth.models import User


class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=128, help_text="Create new Category")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    
    class Meta:
        model = Category
        
 
class PageForm(forms.ModelForm):
    title = forms.CharField(max_length=128, help_text="Add URL page title here")
    url = forms.URLField(max_length=128, help_text="Add URL here")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    
    class Meta:
        model = Page       
        fields = ('title', 'url', 'views' )
        
    def clean(self):
        cleaned_data = self.cleaned_data
        url = cleaned_data.get('url')
        
        if url and not url.startswith('http://'):
            cleaned_data['url'] = 'http://' + url        
        return cleaned_data
    
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class UserProfileForm(forms.ModelForm):
    
    class Meta:
        model = UserProfile
        fields = ('website', 'picture')