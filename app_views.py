from django.shortcuts import render

from .models import *


def index(request):

    context = {}
    return render(request, 'myapp/index.html', context)