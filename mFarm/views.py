from datetime import datetime

from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.
from .models import MilkEvaluation


def index(request):
    if request.user.is_authenticated:
        return redirect(to='home')
    return render(request, 'mFarm/index.html')


@login_required(login_url='login')
def home(request):
    if request.user.is_authenticated:
        evaluation = MilkEvaluation.objects.all()
        context = {'milk_evaluation': evaluation, 'currentYear': datetime.now().year}
        return render(request=request, template_name='mFarm/home.html', context=context)
    return redirect(to='login')


def loginPage(request):
    messages.info(request, 'You are not logged in')
    if request.user.is_authenticated:
        return redirect(to='home')
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user = User.objects.get(email=email)
            user = authenticate(request, username=user.username, password=password)
            if user is not None:
                login(request, user)
                return redirect(to='home')
            else:
                messages.info(request, 'Username OR password is incorrect')
        except(User.DoesNotExist, User.MultipleObjectsReturned) as e:
            messages.info(request, e)
    return render(request, 'mFarm/login.html')
