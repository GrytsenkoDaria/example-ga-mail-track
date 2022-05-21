from django.contrib import admin
from django.urls import path

from ga_mail import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.base, name='base'),
]
