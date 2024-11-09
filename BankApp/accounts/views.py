from django.shortcuts import render, redirect, get_object_or_404
from .models import Hesap, Islem
from .forms import HesapForm, IslemForm

def hesap_list(request):
    # Kullanıcının hesaplarını listeleyin
    hesaplar = Hesap.objects.filter(musteri=request.user)
    return render(request, 'accounts/hesap_list.html', {'hesaplar': hesaplar})

def islem_olustur(request, hesap_id):
    # Belirli bir hesap için yeni bir işlem oluşturma
    hesap = get_object_or_404(Hesap, id=hesap_id, musteri=request.user)
    if request.method == 'POST':
        form = IslemForm(request.POST)
        if form.is_valid():
            islem = form.save(commit=False)
            islem.hesap = hesap
            islem.save()
            return redirect('hesap_list')   
    else:
        form = IslemForm()
    return render(request, 'accounts/islem_olustur.html', {'form': form, 'hesap': hesap})
