from django.shortcuts import render

# Create your views here.
from .models import MilkEvaluation


def index(request):
    evaluation = MilkEvaluation.objects.all()
    context = {'milk_evaluation': evaluation}
    return render(request, 'mFarm/home.html', context=context)
