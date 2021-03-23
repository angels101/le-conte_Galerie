from .import views
from django.urls import path,include

urlpatterns = [
    path('', views.main_flikr,name='main_flikr'),
   
]
