from django import forms

class CityForm(forms.Form):
    city = forms.CharField(
        label='Город',
        widget=forms.TextInput(attrs={
            'id': 'cityInput',
            'autocomplete': 'off',
            'placeholder': 'Введите город',
            'class': 'form-control',
            'aria-describedby': 'searchButton',
        })
    )