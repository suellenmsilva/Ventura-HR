from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.core.paginator import Paginator

from .models import Jobs
from .forms import JobModelForm


def jobs(request):

    search = request.GET.get('search')

    if search:
        jobs = Jobs.objects.filter(cargo__icontains=search)

    elif request.user.has_perm('jobs.add_jobs'):
        job_list = Jobs.objects.all().order_by('-creation_date').filter(user=request.user)
        paginator = Paginator(job_list, 5)
        page = request.GET.get('page')
        jobs = paginator.get_page(page)

    else:
        job_list = Jobs.objects.all().order_by('-creation_date')
        paginator = Paginator(job_list, 5)
        page = request.GET.get('page')
        jobs = paginator.get_page(page)

    return render(request, 'list_jobs.html', {'jobs': jobs})


#Adicionar uma nova vaga, exclusivo para empresa
@permission_required('jobs.add_jobs')
@login_required
def newJob(request):

    if str(request.method) == 'POST':

        form = JobModelForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)

            job.user = request.user
            job.save()
            return redirect('/')
        else:
            messages.error(request, 'Erro ao cadastrar vaga ')
    else:
        form = JobModelForm()
        return render(request, 'add_jobs.html', {'form': form})

    context = {
        'form': form
    }

    return redirect('/')


@login_required
def jobView(request, id):
    job = get_object_or_404(Jobs, pk=id)
    return render(request, 'jobs.html', {'job': job})

#Editar uma nova vaga, exclusivo para empresa
@permission_required('jobs.change_jobs')
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


#Deletar uma nova vaga, exclusivo para empresa
@permission_required('jobs.delete_jobs')
@login_required
def deleteJob(request, id):
    job = get_object_or_404(Jobs, pk=id)

    job.delete()
    messages.info(request, 'Vaga deletada com sucesso.')

    return redirect('/')


