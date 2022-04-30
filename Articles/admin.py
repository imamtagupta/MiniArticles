from django.contrib import admin
from .models import BroadcastGroup, BroadcastMessage

# Register your models here.

admin.site.register(BroadcastMessage)
admin.site.register(BroadcastGroup)
