from django.db import models
from django.utils import timezone
from users.models import User

# Create your models here.

class PhotographerHire(models.Model):
    photographer = models.ForeignKey(User, on_delete=models.CASCADE)
    client = models.ForeignKey(User,related_name='client', on_delete=models.CASCADE)
    pricing = models.IntegerField(default=0)
    pricing_period = models.CharField(max_length=25, null=True)
    start_date = models.DateTimeField('Start date', default=timezone.now())
    end_date = models.DateTimeField('End date', default=timezone.now())
    rating = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['start_date']

    def __str__(self):
        return f'CLient ID: {self.client_id} | Photographer: {self.photographer.name}'