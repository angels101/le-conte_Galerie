from .import views
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.main_flikr,name='main_flikr'),
    path('location/<str:location>/',views.location, name='location'),
    path('search/',views.search, name='search'),
   
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

