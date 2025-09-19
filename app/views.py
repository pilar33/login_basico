from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import RegistroForm  # si usás tu form; si no, UserCreationForm

def login_view(request):
    error = None
    if request.method == 'POST':
        u = request.POST.get('username','').strip()
        p = request.POST.get('password','').strip()
        user = authenticate(request, username=u, password=p)
        if user is not None:
            login(request, user)
            return redirect('home')
        error = "Usuario o contraseña incorrectos"
    return render(request, 'login.html', {'error': error})          # <-- SIN 'app/'

def register_view(request):
    from django.contrib.auth.forms import UserCreationForm
    Form = RegistroForm if 'RegistroForm' in globals() else UserCreationForm
    if request.method == 'POST':
        form = Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = Form()
    return render(request, 'registro.html', {'form': form})         # <-- SIN 'app/'

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')
    return render(request, 'confirm_logout.html')                   # <-- SIN 'app/'

@login_required
def home(request):
    return render(request, 'home.html')                              # <-- SIN 'app/'
