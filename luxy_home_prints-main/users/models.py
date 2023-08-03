import datetime
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import AbstractUser

PHOTOG_STATUS = (
    (0, "Not a Photographer"),
    (1, "A Photographer")
)

DAYS = (
    ('mon', "Monday"),
    ('tue', "Tuesday"),
    ('wed', "Wednesday"),
    ('thu', "Thursday"),
    ('fri', "Friday"),
    ('sat', "Saturday"),
    ('sun', "Sunday"),
)

class Avatar(models.Model):
    image = models.ImageField(upload_to='avatar', null=True)
    
    def __str__(self):
        return f'Picture {self.image}'

class User(AbstractUser):
    name = models.CharField(max_length=25)
    email = models.CharField(max_length=25, unique=True)
    avatar = models.ForeignKey(Avatar, on_delete=models.CASCADE, null=True)     
    
    auth_token = models.CharField(max_length=255, default="")
    auth_type = models.CharField(max_length=10, default="")
    token_date = models.DateTimeField('date published', default=timezone.now())

    photographer = models.IntegerField(choices=PHOTOG_STATUS, default=0)
    region = models.CharField(max_length=25, null=True)
    town = models.CharField(max_length=25, null=True)
    address = models.CharField(max_length=25, null=True)
    workday_start = models.CharField(max_length=25, choices=DAYS, null=True)
    workday_end = models.CharField(max_length=25, choices=DAYS, null=True)
    pricing = models.IntegerField(default=0)
    pricing_period = models.CharField(max_length=25, null=True)
    rating = models.IntegerField(default=0)
    ratings = models.IntegerField(default=0)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'password', 'username']

    class Meta:
        ordering = ['rating']
    def __str__(self):
        return self.name

    def token_valid(self):
        now = timezone.now()
        return now - datetime.timedelta(minutes=10) <= self.token_date <= now





