from django import forms
from .models import Islem

class IslemForm(forms.ModelForm):
    class Meta:
        model = Islem
        fields = ['islem_tipi', 'islem_miktari', 'aciklama']
