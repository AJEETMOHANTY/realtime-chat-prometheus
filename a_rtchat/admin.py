# It’s used to register your models so they appear in Django’s built-in Admin Dashboard.
from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(ChatGroup)
admin.site.register(GroupMessage)
