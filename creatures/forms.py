from django import forms
from .models import Creature

class CreatureForm(forms.ModelForm):
    class Meta:
        model = Creature
        fields = ['name', 'weight', 'height']