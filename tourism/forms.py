from django import forms
from .models import VillageApplication

class VillageApplicationForm(forms.ModelForm):
    class Meta:
        model = VillageApplication
        fields = ['name', 'email', 'village', 'message']
