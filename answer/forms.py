from django import forms

from answer.models import Answer


class AnswerModelForm(forms.ModelForm):

    class Meta:
        model = Answer
        fields = ['criterict', 'experience']

