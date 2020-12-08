from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect

from jobs.models import Aplication, Jobs
from users.forms import CustomUsuarioCreateForm, CustomUsuarioChangeForm
from users.models import CustomUsuario


def home_view(request):
    return render(request, 'home.html')


def signup_view(request):
    form = CustomUsuarioCreateForm(request.POST)
    if form.is_valid():
        form.save()
        email = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=email, password=password)
        # login(request, user)
        return redirect('index')
    return render(request, 'signup.html', {'form': form})


@login_required
def perfil(request, id):
    perfil = get_object_or_404(CustomUsuario, pk=id)
    if request.user.has_perm('jobs.add_jobs'):
        jobs = Jobs.objects.filter(user_id=id)

        for job in jobs:
            aplications = Aplication.objects.filter(jobs_id=job)
        list = len(jobs)

        return render(request, 'perfil.html', {'perfil': perfil, 'list': list, 'jobs': jobs, 'aplications': aplications,

                                               })
    else:
        aplication = Aplication.objects.filter(user_id=id)
        return render(request, 'perfil.html', {'perfil': perfil,  'jobs': aplication})

@login_required
def edit_user(request, id):
    user = get_object_or_404(CustomUsuario, pk=id)
    form = CustomUsuarioChangeForm(instance=user)
    if (request.method == 'POST'):
        form = CustomUsuarioChangeForm(request.POST, instance=user)

        if (form.is_valid()):
            user.save()
            return redirect('/')
        else:
            return render(request, 'edit_user.html', {'form': form, 'task': user})
    else:
        return render(request, 'edit_user.html', {'form': form, 'task': user})


@login_required
def delete_user(request, id):
    user = get_object_or_404(CustomUsuario, pk=id)

    user.delete()
    messages.info(request, 'Usuario Deletado')

    return redirect('/')