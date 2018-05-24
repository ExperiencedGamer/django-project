from django.shortcuts import render, redirect, HttpResponseRedirect
from django.http import HttpResponse
from .models import Posts
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from posts.forms import RegistrationForm, EditUserForm
from django.contrib.auth import login, logout
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    posts = Posts.objects.all()[:10]
    context = {
        'title': 'Latest Posts',
        'posts': posts
    }
    #return HttpResponse('Hello From POSTS')
    return render(request, 'posts/index.html', context)

def details(requests, id):
    post = Posts.objects.get(id=id)
    context = {
        'posts': post
    }

    return render(requests, 'posts/details.html', context)

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return HttpResponseRedirect('/')
    else:
        form = AuthenticationForm()
    return render(request, 'posts/reg_form.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            #login
            user = form.get_user()
            login(request, user)
            return HttpResponseRedirect('/')
    else:
        form = AuthenticationForm()
    context = {
        'form' : form
    }
    return render(request, 'posts/login.html', context)

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

def account_view(request):
    if request.user.is_authenticated:
        return render(request, 'posts/account.html')
    else:
        return HttpResponseRedirect('/register')

def accountSettings(request):
    return render(request, 'posts/accounts/settings.html')

def editProfile(request):
    if request.method == 'POST':
        form = EditUserForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('/account')
    else:
        form = EditUserForm(instance=request.user)
        return render(request, 'posts/accounts/editprofile.html', {'form': form})

def passwordReset(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.POST, user=request.user)
        if form.is_valid():
            form.save()
            return rediect('/account')
    else:
        form = PasswordChangeForm(user=request.user)
        return render(request, 'posts/accounts/changepass.html', {'form': form})

def accountUrl(request, username):
    return render(request, 'posts/account.html')