# apps/core/forms.py
from django import forms
from .models import Departamento, CentroCusto


class FiltroFolhaForm(forms.Form):

    departamentos = forms.ModelMultipleChoiceField(
        queryset=Departamento.objects.all(),
        required=False,
        widget=forms.CheckboxSelectMultiple,
        label="Departamentos"
    )

    centros_custo = forms.ModelMultipleChoiceField(
        queryset=CentroCusto.objects.all(),
        required=False,
        widget=forms.CheckboxSelectMultiple,
        label="Centros de Custo"
    )

    competencia_inicio = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={'type': 'date'}),
        label="Competência Início"
    )
    
    competencia_fim = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={'type': 'date'}),
        label="Competência Fim"
    )
    