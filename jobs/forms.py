from django import forms
from .models import Jobs, Criterio, Aplication


class JobModelForm(forms.ModelForm):

    class Meta:
        model = Jobs
        fields = ['cargo', 'description', 'city', 'state', 'contract_type', 'expiration_date', 'criterict']


class AplicationModelForm(forms.ModelForm):

    class Meta:
        model = Aplication
        fields = ['Answer']


class CriterioModelForm(forms.ModelForm):

    class Meta:
        model = Criterio
        fields = ['criterict', 'experience']