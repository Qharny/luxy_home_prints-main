from django.contrib import admin
from .models import Image, Categorie
# Register your models here.


class CategorieAdmin(admin.ModelAdmin):
    model = Categorie
    
class ImageAdmin(admin.ModelAdmin):
    model = Image 

admin.site.register(Categorie, CategorieAdmin)
admin.site.register(Image, ImageAdmin)