from django.db import models
from accounts.models import Hesap
from users.models import Musteri

class Islem(models.Model):
    hesap = models.ForeignKey(Hesap, on_delete=models.CASCADE)
    islem_tipi = models.CharField(max_length=50)
    islem_miktari = models.DecimalField(max_digits=18, decimal_places=2)
    islem_tarihi = models.DateTimeField(auto_now_add=True)
    aciklama = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.islem_tipi} - {self.islem_miktari}"

class KrediBasvurusu(models.Model):
    musteri = models.ForeignKey(Musteri, on_delete=models.CASCADE)
    basvuru_tarihi = models.DateTimeField(auto_now_add=True)
    kredi_miktari = models.DecimalField(max_digits=18, decimal_places=2)
    vade = models.IntegerField()
    faiz_orani = models.DecimalField(max_digits=5, decimal_places=2)
    durum = models.CharField(max_length=20)

    def __str__(self):
        return f"Kredi {self.kredi_miktari} - {self.musteri.ad}"


