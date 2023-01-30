from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse


def loginUser(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('home')


    if request.method== 'POST':
        username = request.POST['username']
        password = request.POST['password']        
        
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Username does not exist!')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username or password is incorrect')

    return render(request, 'base/login_register.html')

def logoutUser(request):
    logout(request)
    messages.error(request, 'User was logged out!')
    return redirect('login')

def registerUser(request):
    page = 'register'
    form = UserCreationForm

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            messages.success(request, 'User account was created!')

    context = {'page':page, 'form': form}
    return render(request, 'base/login_register.html', context)

@login_required(login_url="login")
def home(request):
    return render(request, "base/home.html")

@login_required(login_url="login")
def campaign(request):
    return render(request, "base/campaign.html")

@login_required(login_url="login")
def wallet(request):
    return render(request, "base/wallet.html")

@login_required(login_url="login")
def settings(request):
    return render(request, "base/settings.html")

@login_required(login_url="login")
def files(request):
    return render(request, "base/file.html")

@login_required(login_url="login")
def videos(request):
    return render(request, "base/video.html")

@login_required(login_url="login")
def texts(request):
    return render(request, "base/text.html")

@login_required(login_url="login")
def success(request):
    return render(request, "base/success.html")