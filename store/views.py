from django.shortcuts import render, redirect
from .models import * 
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here
from .forms import CreateUserForm

from django.shortcuts import render

def tu_vista(request):
    # Otras operaciones de tu vista
    context = {}
    
    # Verifica si el usuario ha iniciado sesión
    if request.user.is_authenticated:
        context['user_authenticated'] = True
    else:
        context['user_authenticated'] = False

    return render(request, 'store.html', context)

def store(request):
	products = Product.objects.all()
	context = {'products':products}
	return render(request, 'store/store.html', context)

def cart(request):
	context = {}
	return render(request, 'store/cart.html', context)

def checkout(request):
	context = {}
	return render(request, 'store/checkout.html', context)

def loginPage(request):

	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(request, username=username, password=password)

		if user is not None:
			login(request, user)
			return redirect('store')
		else:
			#messages.info(request 'usuario o contraseña invalido')
			return render(request, 'accounts/login.html', context)

	context = {}
	return render(request, 'store/login.html', context)

#@login_required(login_url='Login')
#if request.user.is_authenticed:
def logoutUser(request):
	logout(request)
	return redirect('login')

def register(request):
	form = CreateUserForm()
	
	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			form.save()

	context = {'form' :form}
	return render(request, 'store/register.html', context)