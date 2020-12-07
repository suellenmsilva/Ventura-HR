from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from answer.forms import AnswerModelForm
from answer.models import Answer
from jobs.models import Jobs




