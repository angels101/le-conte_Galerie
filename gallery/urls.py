from django.urls import path
from .views import welcome, gallery_today, dynamic_urls
# from django.conf.urls import url
urlpatterns = [
    path('', welcome, name='home')
    path('gallery-today/', gallery_today, name='galleryToday'),
    path('dynamic/<slug:query>/'. dynamic_urls, name='dynamic'),
]