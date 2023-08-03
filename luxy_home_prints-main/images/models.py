from django.db import models
from users.models import User
from django.utils import timezone

# Create your models here.

class Categorie(models.Model):
    name = models.CharField(max_length=25)
    icon = models.ImageField(upload_to='icons/categories', null=True)
    def __str__(self):
        return f'{self.name}'

class Image(models.Model):
    title = models.CharField(max_length=25, null=True)
    date_uploaded = models.DateTimeField('Upload date', default=timezone.now())
    image = models.ImageField(upload_to='images')
    category = models.ForeignKey(Categorie, on_delete=models.CASCADE, null=True)
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.title}'