from django.contrib import admin
from .models import Photo, PhotoUpload
# Register your models here.

class PhotoAdmin(admin.ModelAdmin):
    model = Photo

class PhotoUploadAdmin(admin.ModelAdmin):
    model = PhotoUpload

admin.site.register(Photo, PhotoAdmin)
admin.site.register(PhotoUpload, PhotoUploadAdmin)