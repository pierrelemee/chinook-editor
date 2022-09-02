from django import forms
from django.forms import TextInput


class ArtistForm(forms.Form):
    name = forms.CharField(label='Artist name', min_length=2, max_length=120, widget=TextInput(attrs={'class': 'form-control'}))
