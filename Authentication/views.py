from django.shortcuts import render, redirect
from . forms import CustomUserCreationForm, CustomAuthenticationForm
from django.contrib import messages
from django.contrib.auth import login, logout

# Create your views here.

def RegistrationView(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # messages.success('Account created successfully, Please log in')
            return redirect('login')
    else:
        form = CustomUserCreationForm() 
    
    context = {
        'form':form
    }
    return render(request, 'singup.html', context)


def LoginView(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data = request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = CustomAuthenticationForm()

    context = {
        'form':form
    }
    return render(request, 'login.html', context)


def LogoutView(request):
    logout(request)
    return redirect('login')