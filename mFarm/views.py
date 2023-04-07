from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Create your views here.
from .models import MilkEvaluation


def index(request):
    if request.user.is_authenticated:
        return redirect(to='home')
    return render(request, 'mFarm/index.html')


def login(request):
    return render(request, 'mFarm/login.html')


@login_required(login_url='login')
def home(request):
    if request.user.is_authenticated:
        evaluation = MilkEvaluation.objects.all()
        context = {'milk_evaluation': evaluation, 'currentYear': datetime.now().year}
        return render(request=request, template_name='mFarm/home.html', context=context)
    return redirect(to='login')
