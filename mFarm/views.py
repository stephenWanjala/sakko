from datetime import datetime

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from .forms.FarmerCreationForm import FarmerCreationForm
# Create your views here.
from .models import MilkEvaluation


def currentYear():
    return datetime.now().year


def index(request):
    if request.user.is_authenticated:
        return redirect(to='home')
    return render(request, 'mFarm/index.html')


@login_required(login_url='login')
def home(request):
    if request.user.is_authenticated:
        evaluation = MilkEvaluation.objects.all().filter(the_milk__farmer=request.user)
        context = {'milk_evaluation': evaluation, 'currentYear': datetime.now().year}
        return render(request=request, template_name='mFarm/home.html', context=context)
    return redirect(to='login')


def loginPage(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            return redirect(to='/admin')
        redirect(to='home')
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            if user.is_superuser:
                return redirect(to='/admin')
            return redirect(to='home')
        else:
            messages.info(request, 'Email or password is incorrect')
    context = {'messages': messages, 'currentYear': datetime.now().year}
    return render(request=request, template_name='mFarm/login.html', context=context)


def logout_view(request):
    logout(request)
    return redirect(to='index')


def signup(request):
    if request.method == 'POST':
        form = FarmerCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = FarmerCreationForm()
    context = {'form': form}
    return render(request, 'mFarm/signUp.html', context)
