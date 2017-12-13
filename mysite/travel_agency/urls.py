from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('excursions/', views.excursions, name='excursions'),
    path('excursions/<int:id>/', views.excursion_detail, name='excursion_detail'),
    path('destinations/', views.destinations, name='destinations'),
    path('destinations/<int:id>/', views.destination_detail, name='destination_detail')
]
