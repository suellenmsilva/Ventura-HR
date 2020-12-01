from django.urls import path

from jobs.views import jobs, newJob, jobView, editJob, deleteJob, newCriterio

urlpatterns = [
    path('', jobs, name='job'),
    # path('', jobs_adc, name='job-list'),
    path('job/<int:id>', jobView, name="job-view"),
    path('newjob/', newJob, name="new-job"),
    path('newjob/newcriterio/', newCriterio, name="new-criterio"),
    path('newcriterio/', newCriterio, name="new-criterio"),
    path('edit/<int:id>', editJob, name="edit-job"),
    path('delete/<int:id>', deleteJob, name="delete-job"),

]