from django.db import models
import cloudinary
from cloudinary.models import CloudinaryField 
import datetime as dt 
# Create your models here.
class categories(models.Model):
    name = models.CharField(max_length=30)

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()

    def __str__(self):
        return self.name
