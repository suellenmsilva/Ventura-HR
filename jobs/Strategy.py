import abc
from django.core.paginator import Paginator
from jobs.models import Jobs

class IStrategy(object):
    @abc.abstractmethod
    def type_filter(self):
        raise NotImplementedError()

class JobsFilterSuperUser(IStrategy):
    def filter(self, request):
        job_list = Jobs.objects.all().order_by('-creation_date').filter(user=request.user)
        paginator = Paginator(job_list, 5)
        page = request.GET.get('page')
        jobs = paginator.get_page(page)
        return jobs

class JobsFilter(IStrategy):
    def filter(self, request):
        job_list = Jobs.objects.all().order_by('-creation_date')
        paginator = Paginator(job_list, 5)
        page = request.GET.get('page')
        jobs = paginator.get_page(page)
        return jobs

