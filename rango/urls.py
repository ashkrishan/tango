from django.conf.urls import patterns, include, url
#from django.contrib import admin


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'twd.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
    url(r'^about/$', 'rango.views.about_page', name='about_page'),
    url(r'^$', 'rango.views.index', name='index'),
    url(r'^category/(?P<category_name_url>\w+)/$','rango.views.category', name='category'),
)
