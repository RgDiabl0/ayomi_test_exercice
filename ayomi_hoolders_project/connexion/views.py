# coding=utf-8

from django.contrib.auth import authenticate
from django.contrib.auth.views import logout
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.utils import timezone

from models import CustomUser


# Create your views here.

def index(request):
	if request.method == 'POST':
		first_name = request.POST.get('first-name')
		last_name = request.POST.get('last-name')
		email = request.POST.get('email')
		username = request.POST.get('username')
		password = request.POST.get('password')

		if len(first_name) > 0 and len(last_name) > 0 and len(email) > 0:
			if len(username) > 0 and len(password) > 0:
				if CustomUser.objects.filter(username=username, email=email, password=password).exists():
					user = authenticate(username=username, password=password)

					if user:
						user.last_login = timezone.now()
						return render(request, 'connexion/profile.html', {'user': user})
				else:
					if not CustomUser.objects.filter(username=username).exists():
						CustomUser.objects.create_user(username=username, email=email, password=password,
						                               first_name=first_name, last_name=last_name)

					user = authenticate(username=username, password=password)

					if user:
						user.date_joined = timezone.now()
						user.last_login = timezone.now()

						return render(request, 'connexion/profile.html', {'user': user})
		elif len(username) > 0 and len(password) > 0:
			if CustomUser.objects.filter(username=username).exists():

				user = authenticate(username=username, password=password)

				if user:
					user.last_login = timezone.now()

					return render(request, 'connexion/profile.html', {'user': user})

	template = loader.get_template('connexion/index.html')
	return HttpResponse(template.render(request=request))


def profile(request):
	return render(request, 'connexion/profile.html', {'user': request.user})


def logout_view(request):
	logout(request)

	template = loader.get_template('connexion/index.html')
	return HttpResponse(template.render(request=request))


def modify_infos(request):
	from django.http import JsonResponse
	if request.method == 'POST':
		username = request.POST.get('username')
		new_email = request.POST.get('new-email')

		if len(new_email) > 0:
			print("test")
			user = CustomUser.objects.get(username=username)
			user.email = new_email
			user.save()

			return JsonResponse({'email': user.email})

	return JsonResponse({'result': 'nok'})
