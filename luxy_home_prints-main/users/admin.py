from django.contrib import admin
from .models import User, Photo, Avatar, PhotoUploads

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    model = User

    fieldsets = (
        (None, {'fields': (('first_name', 'last_name'), 'name', 'username', 'email', 'photographer',
                         ('region', 'town'), 'address', ('workday_start', 'workday_end'), 'rating', 'ratings')}),
        ('Advanced options', {
                'classes': ('collapse',),
                'fields': ('password', 'auth_type', 'auth_token', 'token_date', 'is_active', 'is_staff',
                            'is_superuser', 'last_login', 'date_joined')})
    )

    list_display = ('name', 'email', 'town', 'photographer')
    list_filter = ('town', 'photographer')
    search_fields = ('name', 'email')

class AvatarAdmin(admin.ModelAdmin):
    model = Avatar

admin.site.register(User, UserAdmin)
admin.site.register(Avatar, AvatarAdmin)



