from django import forms

METHOD_CHOICES = [
    ('gauss', 'Eliminación de Gauss'),
    ('gauss_jordan', 'Gauss-Jordan'),
]

class SistemaForm(forms.Form):
    ecuaciones = forms.CharField(
        label="Sistema de ecuaciones",
        widget=forms.Textarea(attrs={'rows': 5, 'cols': 40})
    )
    metodo = forms.ChoiceField(
        choices=METHOD_CHOICES,
        label="Método numérico"
    )
