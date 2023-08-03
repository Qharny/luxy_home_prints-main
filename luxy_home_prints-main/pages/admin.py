from django.contrib import admin
from .models import Page
# Register your models here.

class PageAdmin(admin.ModelAdmin):
    model = Page

admin.site.register(Page, PageAdmin)