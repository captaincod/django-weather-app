from django import forms

class CityForm(forms.Form):
    city = forms.CharField(label='Введите город', max_length=100, )
                           # widget=forms.TextInput(attrs={'list': 'cities'}))