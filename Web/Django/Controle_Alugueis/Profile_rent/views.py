from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib import auth
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.views import View

# Create your views here.
def index(request):
    return render(request, 'profile_rent/index.html')

def login(request):
   form = AuthenticationForm(request)

   if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password') 

        usuario = authenticate(request, username=username, password=password)
        form = AuthenticationForm(request)

        if request.method == 'POST':
            form = AuthenticationForm(request, data=request.POST)  

        if form.is_valid():
            auth.login(request, user=usuario) 
            messages.success(request, 'Logado com sucesso!')
            return redirect('rent:list-location')    
        messages.error(request, 'Login inválido')

   return render(
        request,
        'profile_rent/login.html',
        {
            'form': form
        }
    )
    

def logout(request):
    #def get(self, *args, **kwargs):
        auth.logout(request)
        return render(request, 'profile_rent/index.html')