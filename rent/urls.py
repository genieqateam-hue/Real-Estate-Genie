from django.urls import path
from . import views

app_name = 'rent'

urlpatterns = [
    path('', views.rent_list, name='rent_list'),
    path('<slug:slug>/', views.rent_detail, name='rent_detail'),
]
