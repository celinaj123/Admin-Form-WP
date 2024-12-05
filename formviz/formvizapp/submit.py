from django import forms
from .models import MapRowSec

class MapRowSecForm(forms.ModelForm):
    class Meta:
        model = MapRowSec
        fields = ['usr_access', 'param', 'paramvalue', 'dashboard_id']
