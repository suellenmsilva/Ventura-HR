from django import forms
from .models import Jobs,Criterio


class JobModelForm(forms.ModelForm):

    class Meta:
        model = Jobs
        fields = ['cargo', 'description', 'city', 'state', 'contract_type', 'expiration_date', 'criterict']


class AplicarModelForm(forms.ModelForm):

    class Meta:
        model = Jobs
        fields = ['candidate']


class CriterioModelForm(forms.ModelForm):

    class Meta:
        model = Criterio
        fields = ['criterict', 'experience']