from django.urls import path
from . import views

urlpatterns = [
    path('hesaplar/', views.hesap_list, name='hesap_list'),  
    path('hesap/<int:hesap_id>/islem_olustur/', views.islem_olustur, name='islem_olustur'), 
]