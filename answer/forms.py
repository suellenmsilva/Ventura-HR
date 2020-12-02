from django import forms

from answer.models import Answer, AnswerCriterict


class AnswerModelForm(forms.ModelForm):

    class Meta:
        model = Answer
        fields = ['answercriterict']


class AnswerCriterictModelForm(forms.ModelForm):

    class Meta:
        model = AnswerCriterict
        fields = ['criterict','experience']