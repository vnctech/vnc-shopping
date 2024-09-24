from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import RegistrationForm


def home(request):
    return render(request, 'index.html')
    
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            mobile = form.cleaned_data.get('mobile')
            password = form.cleaned_data.get('password1')
            user = authenticate(mobile=mobile, password=password)
            login(request, user)
            return redirect('home')
    else:
        form = RegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})


