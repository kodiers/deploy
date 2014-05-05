from django.conf.urls import patterns, include, url
from dns import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'deploy.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^register/', views.reg_user),
    url(r'regsuccess/', views.reg_success),
    url(r'^admin/', include(admin.site.urls)),
)
