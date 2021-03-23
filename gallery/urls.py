from .import views
from django.urls import path,include

urlpatterns = [
    path('', views.main_flikr,name='main_flikr'),
    path('location/(\d+',views.location, name='location'),
    path('search/',views.search, name='search')
   
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

