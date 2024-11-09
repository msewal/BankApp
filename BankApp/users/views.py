from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import RegisterForm

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():  # Formun geçerliliğini kontrol et
            user = form.save()  # Kullanıcıyı kaydet
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            # Kullanıcıyı otomatik olarak giriş yap
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')  # Kayıttan sonra ana sayfaya yönlendir
    else:
        form = RegisterForm()  # GET isteğinde formu oluştur
    return render(request, 'register.html', {'form': form})  # Şablonu render et
