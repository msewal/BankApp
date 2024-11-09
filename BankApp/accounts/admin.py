# örneğin, users/admin.py dosyasında:
from django.contrib import admin
from .models import Hesap
from .models import KrediKarti  

admin.site.register(Hesap)
admin.site.register(KrediKarti)

