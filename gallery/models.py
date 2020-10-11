from django.db import models
from cloudinary import CloudinaryImage
# Create your models here.
class Image(models.Model):
    title = models.CharField(max_length=100)
    image = CloudinaryImage('image')
    