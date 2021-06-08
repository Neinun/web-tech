from django import forms

from .models import Oink

class OinkerForm(forms.ModelForm):
    class Meta:
        model = Oink
        fields = ('body_img',)