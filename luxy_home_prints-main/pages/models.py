from django.db import models

# Create your models here.

class Page(models.Model):
    name = models.CharField(max_length=25)
    icon = models.ImageField(upload_to='icons/pages')
    def __str__(self):
        return f'Picture {self.icon}'