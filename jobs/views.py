from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponse
from .models import Jobs
from .forms import JobModelForm
import datetime


def jobs(request):
    context = {
        'jobs': Jobs.objects.all()
    }
    return render(request, 'list_jobs.html', context)


@login_required
def newJob(request):

    if str(request.method) == 'POST':
        form = JobModelForm(request.POST)
        if form.is_valid():
            form.save()
            # messages.success(request, 'Vaga cadastrada com sucesso')
            form = JobModelForm()
        else:
            messages.error(request, 'Erro ao cadastrar vaga ')
    else:
        form = JobModelForm()

    context = {
        'form': form
    }
    return render(request, 'add_jobs.html', context)


# @login_required
# def jobList(request):
#     search = request.GET.get('search')
#     filter = request.GET.get('filter')
#     # tasksDoneRecently = Jobs.objects.filter(done='done', updated_at__gt=datetime.datetime.now() - datetime.timedelta(
#     #     days=30)).count()
#     # tasksDone = Jobs.objects.filter(done='done', user=request.user).count()
#     # tasksDoing = Jobs.objects.filter(done='doing', user=request.user).count()
#
#     if search:
#         jobs = Jobs.objects.filter(title__icontains=search, user=request.user)
#     elif filter:
#         jobs = Jobs.objects.filter(done=filter, user=request.user)
#     else:
#         job_list = Jobs.objects.all().order_by('-creation_date').filter(user=request.user)
#
#         paginator = Paginator(job_list, 3)
#
#         page = request.GET.get('page')
#         jobs = paginator.get_page(page)
#
#     return render(request, 'listar_vagas.html',
#                   {'jobs': jobs})
#                   # {'jobs': jobs, 'tasksrecently': tasksDoneRecently, 'tasksdone': tasksDone,
#                   #  'tasksdoing': tasksDoing})


@login_required
def jobView(request, id):
    job = get_object_or_404(Jobs, pk=id)
    return render(request, 'jobs.html', {'job': job})


@login_required
def editJob(request, id):
    job = get_object_or_404(Jobs, pk=id)
    form = JobModelForm(instance=job)

    if(request.method == 'POST'):
        form = JobModelForm(request.POST, instance=job)

        if(form.is_valid()):
            job.save()
            return redirect('/')
        else:
            return render(request, 'editar_vagas.html', {'form': form, 'task': job})
    else:
        return render(request, 'edit_jobs.html', {'form': form, 'task': job})


@login_required
def deleteJob(request, id):
    job = get_object_or_404(Jobs, pk=id)
    job.delete()

    messages.info(request, 'Vaga deletada com sucesso.')

    return redirect('/')

