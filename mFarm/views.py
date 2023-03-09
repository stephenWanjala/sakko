from django.shortcuts import render

# Create your views here.
from .models import MilkEvaluation


def index(request):
    context = {}
    return render(request, 'mFarm/home.html', context=context)
