from django.contrib import messages
from django.db.models import Count, Q
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.core.paginator import Paginator

from .models import Jobs, Aplication
from .forms import JobModelForm, CriterioModelForm, AplicationModelForm


'''Faz a listagem das vagas, paginação e search das vagas, aqui e feito por usuario e empresa, em algumas parte
temos tratamento de permições'''


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


''' Adicionar uma nova vaga, exclusivo para empresa '''


@permission_required('jobs.add_jobs')
@login_required
def new_job(request):

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


''' Adicionando um criterio, fluxonão esta certo, deve ser feito uma refatoração e uma melhoria na construção'''


@login_required
def new_criterio(request):

    if str(request.method) == 'POST':

        form = CriterioModelForm(request.POST)
        if form.is_valid():
            criterio = form.save(commit=False)

            criterio.user = request.user
            criterio.save()
            return redirect('/newjob')
        else:
            messages.error(request, 'Erro ao cadastrar um criterio')
    else:
        form = CriterioModelForm()
        return render(request, 'add_criterio.html', {'form': form})

    return redirect('add_jobs.html')


'''Listar informações sobre uma vaga'''


@login_required
def job_view(request, id):
    job = get_object_or_404(Jobs, pk=id)
    if request.user.has_perm('jobs.add_jobs'):
        jobs = Aplication.objects.filter(jobs_id=id)
        list = len(jobs)
        return render(request, 'jobs.html', {'job': job, 'list': list})
    else:
        return render(request, 'jobs.html', {'job': job})



'''Editar uma nova vaga, exclusivo para empresa'''


@permission_required('jobs.change_jobs')
@login_required
def edit_job(request, id):
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


'''Incluir usuarios em uma vaga, exclusivo para usarios '''


@permission_required('jobs.add_aplication')
@login_required
def aplication(request):
    if str(request.method) == 'POST':
        form = AplicationModelForm(request.POST)
        if form.is_valid():
            aplication = form.save(commit=False)
            aplication.user = request.user
            aplication.save()
            return redirect('/')
        else:
            messages.error(request, 'Erro ao aplicar a uma vaga')
    else:
        form = AplicationModelForm()
        return render(request, 'aplicar.html', {'form': form})

    return redirect('aplicar.html')


'''Deletar uma nova vaga, exclusivo para empresa'''


@permission_required('jobs.delete_jobs')
@login_required
def delete_job(request, id):
    job = get_object_or_404(Jobs, pk=id)

    job.delete()
    messages.info(request, 'Vaga deletada com sucesso.')

    return redirect('/')