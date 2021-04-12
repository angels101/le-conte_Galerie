from django.contrib import admin
from .models import Location, Image, categories
#from .models import Upload
# Register your models here.




class ImageAdmin(admin.ModelAdmin):
    filter_horizontal = ('categories',)

admin.site.register(Location)
admin.site.register(Image,ImageAdmin)
admin.site.register(categories)
#admin.site.register(Upload)
