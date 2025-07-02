from django import forms

class CodeForm(forms.Form):
    code = forms.CharField(
        label='Parolu daxil edin',
        max_length=100,
        widget=forms.PasswordInput(attrs={
            'class': 'input-field',
            'placeholder': 'Parolu daxil edin',
        })
    )