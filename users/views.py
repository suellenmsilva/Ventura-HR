from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect

from users.forms import CustomUsuarioCreateForm
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
    return render(request, 'perfil.html', {'perfil': perfil})