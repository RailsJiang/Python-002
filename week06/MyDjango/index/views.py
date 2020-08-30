from django.shortcuts import render

# Create your views here.
from .models import T1


def index(request):
    queryset = T1.objects.all()
    conditions = {'n_star__gt': 3}
    shorts = queryset.filter(**conditions)

    return render(request, 'index.html', locals())