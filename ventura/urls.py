"""ventura URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from users.views import signup_view, perfil, edit_user, delete_user

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contas/', include('django.contrib.auth.urls')),
    path('', include('jobs.urls')),
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('signup/', signup_view, name="signup"),
    path('perfil/<int:id>', perfil, name="perfil"),
    path('edit_user/<int:id>', edit_user, name="edit_user"),
    path('delete_user/<int:id>', delete_user, name="delete_user"),


]
