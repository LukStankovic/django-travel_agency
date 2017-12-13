from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('excursions/', views.excursions, name='excursions'),
    path('excursions/<int:id>/', views.excursion_detail, name='excursion_detail')
]
