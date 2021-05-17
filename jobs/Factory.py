from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from jobs.Strategy import JobsFilterSuperUser, JobsFilter
from jobs.models import Jobs
from .Specification import UserSpecification, SuperUserSpecification, NameUser
from .forms import JobModelForm


class JobFactory:

    def job(self, request):
        search = request.GET.get('search')
        root_specification = UserSpecification().and_(SuperUserSpecification())

        result_user = root_specification.is_satisfied_by(request.user)
        if search:
            jobs = Jobs.objects.filter(cargo__icontains=search)

        elif result_user == True:
            jobs = JobsFilterSuperUser().filter(request)

        else:
            jobs = JobsFilter().filter(request)

        return render(request, 'list_jobs.html', {'jobs': jobs})


class NewFactory:
    def new_job(self, request):

         if str(request.method) == 'POST':
            form = JobModelForm(request.POST)

            root_specification = UserSpecification().and_(SuperUserSpecification())
            result_user = root_specification.is_satisfied_by(request.user)

            if result_user == True:
                if form.is_valid():
                    job = form.save(commit=False)

                    job.user = NameUser.user(request)
                    job.save()
                    return redirect('/')
                else:
                    messages.error(request, 'Erro ao cadastrar vaga ')
            else:
                form = JobModelForm()
                return render(request, 'add_jobs.html', {'form': form})

        return redirect('/')