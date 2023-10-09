from django import forms
from testapp.models import Movie

class Movieform(forms.ModelForm):
    mname = forms.CharField(max_length=30)
    hero = forms.CharField(max_length=30)
    heroin = forms.CharField(max_length=30)
    rating = forms.IntegerField()

    class Meta:
        model=Movie
        fields='__all__'