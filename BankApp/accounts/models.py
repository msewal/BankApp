from django.db import models
from users.models import Musteri

class Hesap(models.Model):
    musteri = models.ForeignKey(Musteri, on_delete=models.CASCADE)
    hesap_numarasi = models.CharField(max_length=20, unique=True)
    hesap_tipi = models.CharField(max_length=30)
    bakiye = models.DecimalField(max_digits=18, decimal_places=2)
    olusturma_tarihi = models.DateTimeField(auto_now_add=True)
    durum = models.CharField(max_length=20)

    def __str__(self):
        return f"Hesap {self.hesap_numarasi} - {self.musteri.ad}"

class KrediKarti(models.Model):
    musteri = models.ForeignKey(Musteri, on_delete=models.CASCADE)
    kart_numarasi = models.CharField(max_length=16, unique=True)
    kart_tipi = models.CharField(max_length=50)
    son_kullanma_tarihi = models.DateTimeField()
    cvv = models.CharField(max_length=3)
    limit = models.DecimalField(max_digits=18, decimal_places=2)
    kullanilabilir_limit = models.DecimalField(max_digits=18, decimal_places=2)

    def __str__(self):
        return f"Kredi Kartı {self.kart_numarasi} - {self.musteri.ad}"