from django.contrib import admin
#andre
#andre1305

# Register your models here.

from .models import Room, Messages, Topic

admin.site.register(Room)
admin.site.register(Messages)
admin.site.register(Topic)