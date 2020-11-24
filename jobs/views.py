from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .models import Jobs
from .forms import JobModelForm


def jobs(request):
    search = request.GET.get('search')
    if search:
        jobs = Jobs.objects.filter(cargo__icontains=search)

    else:
        job_list = Jobs.objects.all().order_by('-creation_date')

        paginator = Paginator(job_list, 5)

        page = request.GET.get('page')
        jobs = paginator.get_page(page)

    return render(request, 'list_jobs.html', {'jobs': jobs})


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
            return render(request, 'edit_jobs.html', {'form': form, 'task': job})
    else:
        return render(request, 'edit_jobs.html', {'form': form, 'task': job})


@login_required
def deleteJob(request, id):
    job = get_object_or_404(Jobs, pk=id)
    job.delete()

    messages.info(request, 'Vaga deletada com sucesso.')

    return redirect('/')

@login_required
def changeStatus(request, id):
    job = get_object_or_404(Jobs, pk=id)

    if(job.done == 'doing'):
        task.done = 'done'
    else:
        task.done = 'doing'

    task.save()

    return redirect('/')


