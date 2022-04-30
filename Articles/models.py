from distutils.command.upload import upload
from email.policy import default
from django.db import models
from django.utils import timezone

# Create your models here.

class BroadcastGroup(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100, null=True, blank=True)
    date_created = models.DateTimeField(default = timezone.now)
    
    def __str__(self):
        return self.name

class BroadcastMessage(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(upload_to='images/', default=None)
    video = models.FileField(upload_to='videos/',null=True, default=None)
    ytvideo = models.CharField(max_length=100 ,null=True,default=None)
    broadcastgroup = models.ForeignKey(BroadcastGroup, on_delete=models.CASCADE)
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title