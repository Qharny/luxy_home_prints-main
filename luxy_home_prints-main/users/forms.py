from .models import Avatar, User, Photo
from django import forms

class UserRegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('name', 'email', 'username', 'password')

class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ('photo',)

class AvatarForm(forms.ModelForm):
    class Meta:
        model = Avatar
        fields = ('image',)
        
