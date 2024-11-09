# örneğin, users/admin.py dosyasında:
from django.contrib import admin
from .models import Islem, KrediBasvurusu

admin.site.register(Islem)
admin.site.register(KrediBasvurusu)
