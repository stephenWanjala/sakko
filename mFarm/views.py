import re
from datetime import datetime

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseBadRequest
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms.FarmerCreationForm import FarmerCreationForm
# Create your views here.
from .models import MilkEvaluation, Sacco, Farmer


def currentYear():
    return datetime.now().year


def index(request):
    if request.user.is_authenticated:
        return redirect(to='home')
    return render(request, 'mFarm/index.html')


@login_required(login_url='login')
def home(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            return redirect(to='/admin')
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
    saccos = Sacco.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')

        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        pattern = "^0(7(?:(?:[129][0-9])|(?:0[0-8])|(4[0-1]))[0-9]{6})$"
        if not re.match(pattern, request.POST.get('phone')):
            messages.add_message(request, messages.ERROR, 'Phone number is not valid')
            return redirect(to='signup')
        phone = request.POST.get('phone')

        if request.POST.get('sacco') == 'Select Sacco':
            messages.add_message(request, messages.ERROR, 'Please select a Sacco')
            return redirect(to='signup')
        saccoId = request.POST.get('sacco')
        if saccoId is None:
            messages.add_message(request, messages.ERROR, 'Please select a Sacco')
            return redirect(to='signup')

        sacco = Sacco.objects.get(id=saccoId)
        address = sacco.location

        try:
            if password2 != password1:
                messages.error(request, 'Passwords do not match')
                return redirect(to='signup')
            user = get_user_model().objects.create_user(name=name, phone=phone, email=email, address=address,
                                                        sacco=sacco, password=password1)
            user.save()

            messages.add_message(request, messages.INFO, 'Account created successfully')
            login(request, user)
            return redirect(to='home')
        except Exception as e:
            print(e)
            messages.add_message(request, messages.ERROR, e)
            return redirect(to='signup')
    else:
        form = FarmerCreationForm()
    context = {'saccos': saccos, 'messages': messages.get_messages(request)}
    return render(request, 'mFarm/signUp.html', context)


