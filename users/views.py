from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect

from users.forms import CustomUsuarioCreateForm


def home_view(request):
    return render(request, 'home.html')


def signup_view(request):
    form = CustomUsuarioCreateForm(request.POST)
    if form.is_valid():
        form.save()
        email = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=email, password=password)
        login(request, user)
        return redirect('home')
    return render(request, 'signup.html', {'form': form})