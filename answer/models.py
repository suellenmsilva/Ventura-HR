from django.contrib.auth import get_user_model
from django.db import models

from jobs.models import Jobs, Criterio


class AnswerCriterict(models.Model):
    TYPE_crit = (
        ('ruim', 'Ruim'),
        ('bom', 'Bom'),
        ('muito_bom', 'Muito Bom'),
        ('excelente', 'Excelente'),
    )
    criterict = models.ManyToManyField(Criterio)
    experience = models.CharField(max_length=20, choices=TYPE_crit)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'AnswerCriterict'
        verbose_name_plural = 'AnswerCritericts'

    def __str__(self):
        return '{}'.format(self.criterict)


class Answer(models.Model):
    user = models.ManyToManyField(get_user_model())
    jobs = models.ManyToManyField(Jobs)
    date = models.DateTimeField(auto_now_add=True)
    answercriterict = models.ManyToManyField(AnswerCriterict)

    class Meta:
        verbose_name = 'Answer'
        verbose_name_plural = 'Answers'

    def __str__(self):
        return '{} {}'.format(self.user, self.jobs)




