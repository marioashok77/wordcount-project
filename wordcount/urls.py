
from django.contrib import admin
from django.urls import path
from .views import home,eggs,count

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name='home'),
    path('eggs/',eggs,name='eggs'),
    path('count/',count,name='count')
]
