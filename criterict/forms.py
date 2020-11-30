from django import forms

from criterict.models import Criterict


class CriterictModelForm(forms.ModelForm):

    class Meta:
        model = Criterict
        fields = ['criterict', 'experience']