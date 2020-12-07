from django.urls import path

from jobs.views import jobs, aplication, new_job, new_criterio, edit_job, delete_job, job_view

urlpatterns = [
    path('', jobs, name='job'),
    path('job/<int:id>', job_view, name="job-view"),
    path('newjob/', new_job, name="new-job"),
    path('newjob/newcriterio/', new_criterio, name="new-criterio"),
    path('newcriterio/', new_criterio, name="new-criterio"),
    path('edit/<int:id>', edit_job, name="edit-job"),
    path('aplication/<int:id>', aplication, name="aplication-job"),
    path('delete/<int:id>', delete_job, name="delete-job")
]
