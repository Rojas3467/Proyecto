from django import forms

class InterpolacionForm(forms.Form):
    puntos_x = forms.CharField(label='Valores de x (separados por comas)')
    puntos_y = forms.CharField(label='Valores de y (separados por comas)')


class InterpolacionInversaForm(forms.Form):
    puntos_y = forms.CharField(label='Valores de y (separados por comas)', widget=forms.TextInput(attrs={'placeholder': 'Ejemplo: 2,4,9'}))
    puntos_x = forms.CharField(label='Valores de x (separados por comas)', widget=forms.TextInput(attrs={'placeholder': 'Ejemplo: 1,2,3'}))

