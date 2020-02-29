from django.urls import path
from . import views

#Application URLconf

urlpatterns = [
    path('', views.home, name='home'),
    path('red-tools/', views.redtools, name='red-tools'),
    path('blue-tools/', views.bluetools, name='blue-tools'),

]
