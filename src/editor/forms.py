from django import forms


class ArtistForm(forms.Form):
    name = forms.CharField(label='Artist name', max_length=120)
