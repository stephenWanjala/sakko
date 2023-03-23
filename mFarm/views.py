from django.shortcuts import render, redirect

# Create your views here.

from .models import MilkEvaluation

# Let's add a register function to the views
# Here, we import NewUserForm from forms.py and login from django.contrib.auth.
# Then write a new view function called register_request.

from .forms import NewUserForm
from django.contrib.auth import login, authenticate, logout  # add authenticate to imports
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm  # import authentication form


def register_request(request):
    if request.method == "POST":  # First if checks to see whether the form is being posted while
        form = NewUserForm(request.POST)
        if form.is_valid():  # Second if checks to see whether form is valid and if both are true
            user = form.save()  # the form information is saved under a user,
            login(request, user)  # the user is logged in,
            messages.success(request, "Registration successful.")  # and the user is redirected to the
            return redirect("mFarm:homepage")  # homepage showing a success message
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request=request, template_name="mFarm/register.html", context={"register_form": form})


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)  # verify user credentials
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("mFarm:homepage")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="mFarm/login.html", context={"login_form": form})


def logout_request(request):  # add a logout function
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("main:homepage")


def homepage(request):
    return render(request=request, template_name='mFarm/home.html')


def index(request):
    evaluation = MilkEvaluation.objects.all()
    context = {'milk_evaluation': evaluation}
    return render(request, 'mFarm/home.html', context=context)
