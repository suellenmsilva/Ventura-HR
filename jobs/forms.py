from django import forms
from .models import Jobs


class JobModelForm(forms.ModelForm):

    class Meta:
        model = Jobs
        fields = ['cargo', 'description', 'city', 'state', 'contract_type', 'expiration_date', 'criterict']