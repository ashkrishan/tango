from django.conf.urls import patterns, include, url
#from django.contrib import admin


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'twd.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
    url(r'^about/$', 'rango.views.about_page', name='about_page'),
    url(r'^register/$', 'rango.views.register', name='register'),
    url(r'^login/$', 'rango.views.user_login', name='user_login'),
    url(r'^restricted/$', 'rango.views.restricted', name='restricted'),
    url(r'^$', 'rango.views.index', name='index'),
    #url(r'^category/(?P<category_name_url>\w+)/$','rango.views.category', name='category'),
    url(r'^category/(?P<category_name_url>[[\w|\W]+)/add_page/$','rango.views.add_page', name='add_page'),
    url(r'^category/add_category/$', 'rango.views.add_category', name='add_category'),
    url(r'^category/(?P<category_name_url>[[\w|\W]+)/$','rango.views.category', name='category'),
    
    #url(r'^category/(?P<category_name_url>\S+)/$','rango.views.category', name='category'),

)
