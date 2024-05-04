from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm

def home(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Welcome back, " + user.username)
            return redirect('home')
        else:
            messages.success(request, "There was an error logginig in. Please try again...!")
            return redirect('home')

    else:
        return render(request, 'home.html', {})

def user_login(request):
    pass

def user_logout(request):
    logout(request)
    messages.success(request, "You have been logged out...!")
    return redirect('home')

def user_registration(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username, password)
            login(request, user)
            messages.success(request, "You have successfully registered. Welcome aboard, " + user.first_name)
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form':form})
    return render(request, 'register.html', {'form':form})

