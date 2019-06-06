from django.urls import path
from django.contrib import admin
from django.contrib.auth import logout

from django.conf.urls import include, url

app_name = 'api'


urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('logout/', logout, {'next_page': '/'}, name='logout')
]
