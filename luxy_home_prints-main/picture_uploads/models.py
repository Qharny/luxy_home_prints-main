from django.db import models
from users.models import User
# Create your models here.

class Photo(models.Model):
    # title = models.CharField(max_length=25, null=True)
    photo = models.ImageField(upload_to='images', null=True)
    
    def __str__(self):
        return f'Picture {self.photo}'

class PhotoUpload(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    photo = models.ManyToManyField(Photo)

    def __str__(self):
        return f'{self.client.name}'