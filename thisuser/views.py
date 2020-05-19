from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth import login, logout, authenticate
from .forms import SignUpForm, LoginForm
from thisuser.models import CustomUser
from customusers.settings import AUTH_USER_MODEL
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def index(request):
    html = 'home.html'
    data = CustomUser.objects.all()

    return render(request, html, {'data':data, 'auth_user': AUTH_USER_MODEL})

def signupView(request):
    html= 'signup.html'
    form=SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
    if form.is_valid():
            data = form.cleaned_data
            new_user = CustomUser.objects.create_user(
                username=data['username'],
                display_name=data['display_name'],
                password=data['password1'],
                
                )
            new_user.save()
            login(request, new_user)
            return HttpResponseRedirect(reverse('home'))
    form = SignUpForm()
    return render(request, html, {'form': form}) 

def loginview(request):
    html = 'login.html'
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user= authenticate(
                request, username = data['username'], 
                password= data['password']
                )
            if user:
                login(request, user)
                
            return HttpResponseRedirect(
                    request.GET.get('next', reverse('home'))
                )
    form = LoginForm()
    return render(request, html, {'form': form})

def logoutview(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))