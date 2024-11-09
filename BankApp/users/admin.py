# örneğin, users/admin.py dosyasında:
from django.contrib import admin
from .models import Musteri 

admin.site.register(Musteri)
