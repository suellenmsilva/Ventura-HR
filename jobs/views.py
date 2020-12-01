from django.contrib import messages
from django.contrib.auth import _get_user_session_key
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.core.paginator import Paginator

from .models import Jobs
from .forms import JobModelForm, CriterioModelForm, AplicarModelForm


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

    return redirect('/')


@login_required
def newCriterio(request):

    if str(request.method) == 'POST':

        form = CriterioModelForm(request.POST)
        if form.is_valid():
            criterio = form.save(commit=False)

            criterio.user = request.user
            criterio.save()
            return redirect('/')
        else:
            messages.error(request, 'Erro ao cadastrar um criterio')
    else:
        form = CriterioModelForm()
        return render(request, 'add_criterio.html', {'form': form})

    return redirect('add_jobs.html')


@login_required
def jobView(request, id):
    job = get_object_or_404(Jobs, pk=id)
    form = JobModelForm(instance=job)
    if (request.method == 'POST'):
        form = JobModelForm(request.POST)
        if (form.is_valid()):
            post = form.save(commit=False)
            post.candidate = request.user

            return redirect('/')
        else:
            return render(request, 'jobs.html', {'form': form, 'task': job})
    else:
        return render(request, 'jobs.html', {'form': form, 'task': job})


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

@login_required
def aplicar(request, id):
    job = get_object_or_404(Jobs, pk=id)
    form = AplicarModelForm(instance=job)
    if(request.method == 'POST'):
        form = AplicarModelForm(request.POST, instance=job)
        if form.is_valid():
            job = form.save(commit=False)
            job.user = request.user
            print('passou')
            job.save()
            messages.info(request, 'Vaga aplicada com sucesso.')
            return redirect('/')
        else:
                return render(request, 'aplicar.html', {'form': form, 'task': job})
    else:
        return render(request, 'aplicar.html', {'form': form, 'task': job})

#Deletar uma nova vaga, exclusivo para empresa
@permission_required('jobs.delete_jobs')
@login_required
def deleteJob(request, id):
    job = get_object_or_404(Jobs, pk=id)

    job.delete()
    messages.info(request, 'Vaga deletada com sucesso.')

    return redirect('/')


