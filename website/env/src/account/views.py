from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from account.forms import RegistrationForm, LoginForm, AccountUpdateForm
from rest_framework.authtoken.models import Token
from .models import Account
from django.http import JsonResponse

def must_authenticate_view(request):
    if request.user.is_authenticated:
    	logout(request)
    return render(request, 'jade_island_media/account/must_authenticate.html', {})

def registration_view(request):
	context = {}
	if request.POST:
		form = RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			email = form.cleaned_data.get('email')
			raw_password = form.cleaned_data.get('password1')
			account = authenticate(email=email, password=raw_password)
			login(request, account)
			return redirect('home')
		else:
			context['registration_form'] = form

	else:
		form = RegistrationForm()
		context['registration_form'] = form
	return render(request, 'jade_island_media/account/register.html', context)


def logout_view(request):
	logout(request)
	return redirect('home')


def login_view(request):

	context = {}

	user = request.user
	if user.is_authenticated:
		return redirect("home")

	if request.POST:
		form = LoginForm(request.POST)
		if form.is_valid():
			email = request.POST['email']
			password = request.POST['password']
			user = authenticate(email=email, password=password)

			if user:
				login(request, user)
				return redirect("home")

	else:
		form = LoginForm()

	context['login_form'] = form

	return render(request, "jade_island_media/account/login.html", context)


def profile_view(request):

	if not request.user.is_authenticated:
			return redirect("login")

	context = {}
	if request.POST:
		form = AccountUpdateForm(request.POST, request.FILES or None, instance=request.user)
		if form.is_valid():
			form.save()
			form.initial = {
				"email": request.user.email,
				"display_name": request.user.display_name,
				"profile_picture": request.user.profile_picture,
			}
			context['success_message'] = "Updated"
		else:
    		#preserve initial data
			form.initial = {
				"email": request.POST['email'],
				"display_name": request.POST['display_name'],
				"profile_picture": request.user.profile_picture,
			}
	else:
		form = AccountUpdateForm(

			initial={
					"email": request.user.email, 
					"display_name": request.user.display_name,
					"profile_picture": request.user.profile_picture,
				}
			)

	context['profile_form'] = form
	return render(request, "jade_island_media/account/profile.html", context)
