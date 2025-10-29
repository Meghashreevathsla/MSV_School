from django.urls import path
from . import views

urlpatterns = [
    path('all/', views.get_all),
    path('form/', views.showformdata),


]
