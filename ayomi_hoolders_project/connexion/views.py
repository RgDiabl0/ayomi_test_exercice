# coding=utf-8

from django.contrib.auth import authenticate
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from models import CustomUser


# Index form registering or connecting the user
def index(request):
	if request.method == 'POST':
		first_name = request.POST.get('first-name')
		last_name = request.POST.get('last-name')
		email = request.POST.get('email')
		username = request.POST.get('username')
		password = request.POST.get('password')

		# If the user wants to register (checking if the 3 registering inputs are not empty)
		if len(first_name) > 0 and len(last_name) > 0 and len(email) > 0:
			# Verifying that the other inputs are not empty as well
			if len(username) > 0 and len(password) > 0:
				# Checking if the user already exists, if it doesn't -> creates the user
				if not CustomUser.objects.filter(username=username).exists():
					CustomUser.objects.create_user(username=username, email=email, password=password,
					                               first_name=first_name, last_name=last_name.upper()).full_clean()

				# Connecting the user
				if connect_user(request, username, password):
					return HttpResponseRedirect(reverse("profile"))
		# If the user wants to connect (checking if the 2 connecting inputs are not empty
		elif len(username) > 0 and len(password) > 0:
			if connect_user(request, username, password):
				return HttpResponseRedirect(reverse("profile"))

	# If all the inputs aren't correctly entered, recharge the page
	return render(request, 'connexion/pages/index.html')


# Profile page
@login_required
def profile(request):
	return render(request, 'connexion/pages/profile.html', {'user': request.user})


# Allow the disconnection of the user
def logout_view(request):
	logout(request)

	return redirect('/')


# Modal form to modify the user's data
@csrf_exempt
def modify_infos(request):
	if request.method == 'POST':
		user = request.user
		new_email = request.POST.get('email')

		# Verifiying if the new and old email are differents
		if user.email != new_email:
			user.email = new_email
			user.save()

			return JsonResponse({'email': user.email})


# Connecting the user
def connect_user(request, username, password):
	user = authenticate(username=username, password=password)

	if user is not None:
		login(request, user)

		return True

	return False
