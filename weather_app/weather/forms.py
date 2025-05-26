from django import forms

class CityForm(forms.Form):
    city = forms.CharField(
        label='Город',
        widget=forms.TextInput(attrs={
            'id': 'city',
            'autocomplete': 'off',
            'placeholder': 'Введите город'
        })
    )