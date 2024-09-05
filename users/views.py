from django.shortcuts import render, redirect

from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth import logout
from django.shortcuts import redirect
from .models import User

def register(request):

     if request.method == 'POST':
          form = UserRegisterForm(request.POST)
          if form.is_valid():
               form.save()
               username = form.cleaned_data.get('username')
               messages.success(request, f'Account created for {username}')
               return redirect('login')

     else:
          form = UserRegisterForm()
     return render(request, 'users/register.html', {'form': form})
def user(request):
     return render(request, 'main/layout.html')


def custom_logout_view(request):
    logout(request)
    return render(request, 'users/logout.html')

def profile(request):
     return render(request, 'users/profile.html')