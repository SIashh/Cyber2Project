from django.urls import path

from . import views

urlpatterns = [
    path('staff/blue', views.staff_blue, name='staff_blue'),
    path('staff/red', views.staff_red, name='staff_red'),
    path('customer/blue', views.customer_blue, name='customer_blue'),
    path('customer/red', views.customer_red, name='customer_red'),
    path('benchmark/blue', views.benchmark_blue, name='benchmark_blue'),
    path('benchmark/red', views.benchmark_red, name='benchmark_red'),
    path('note/red', views.note_blue, name='note_blue'),
    path('note/blue', views.note_red, name='note_red'),
]