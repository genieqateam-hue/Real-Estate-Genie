from django.urls import path
from . import views

app_name = 'sale'

urlpatterns = [
    path('', views.sale_list, name='sale_list'),
    path('<slug:slug>/', views.sale_detail, name='sale_detail'),
]
