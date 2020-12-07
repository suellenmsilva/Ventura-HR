from django.urls import path

from answer.views import resposta

urlpatterns = [
    path('', resposta, name="resposta")
]