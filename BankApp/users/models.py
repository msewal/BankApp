from django.db import models
from django.contrib.auth.models import AbstractUser

class Musteri(models.Model):
    ad = models.CharField(max_length=50)
    soyad = models.CharField(max_length=50)
    tc_kimlik_no = models.CharField(max_length=11, unique=True)
    dogum_tarihi = models.DateField()
    cinsiyet = models.CharField(max_length=10)
    email = models.EmailField(unique=True)
    telefon_numarasi = models.CharField(max_length=15)
    adres = models.CharField(max_length=255)
    sehir = models.CharField(max_length=50)
    posta_kodu = models.CharField(max_length=10)
    uyruk = models.CharField(max_length=50)
    hesap_durumu = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.ad} {self.soyad}"