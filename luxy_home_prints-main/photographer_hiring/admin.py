from django.contrib import admin
from .models import PhotographerHire
# Register your models here.

class PhotographerHireAdmin(admin.ModelAdmin):
    model = PhotographerHire

admin.site.register(PhotographerHire, PhotographerHireAdmin)