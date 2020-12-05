from django import forms
from django.forms import SelectDateWidget
from django.contrib.admin import widgets
from .models import Jobs, Criterio, Aplication


class JobModelForm(forms.ModelForm):
    criterict = forms.ModelMultipleChoiceField(queryset=Criterio.objects, widget=forms.CheckboxSelectMultiple(),
                                               required=False)

    class Meta:
        model = Jobs
        fields = ['cargo', 'description', 'city', 'state', 'contract_type', 'expiration_date']


class AplicationModelForm(forms.ModelForm):

    class Meta:
        model = Aplication
        fields = ['jobs']


class CriterioModelForm(forms.ModelForm):

    class Meta:
        model = Criterio
        fields = ['criterict']