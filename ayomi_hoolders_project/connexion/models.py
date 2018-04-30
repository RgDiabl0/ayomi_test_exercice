# coding=utf-8

from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator, URLValidator
from django.db import models


class CustomUser(AbstractUser):
	birth_date = models.DateField(null=True, blank=True)

	phone_number_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
	                                    message="Veuillez entrer un numéro de téléphone au format: '+999999999'..")
	home_phone_number = models.CharField(validators=[phone_number_regex], max_length=17, blank=True, null=True)
	mobile_phone_number = models.CharField(validators=[phone_number_regex], max_length=17, blank=True, null=True)

	address = models.CharField(max_length=30, blank=True, null=True)
	city = models.CharField(max_length=30, blank=True, null=True)

	numeric_regex = RegexValidator(r'^[0-9]*', message="Ce champs ne peut contenir que des chiffres.")
	postal = models.CharField(validators=[numeric_regex], max_length=5, blank=True, null=True)

	website = models.CharField(validators=[URLValidator], max_length=100, null=True)

	desc = models.TextField(blank=True, null=True)

	linkedin_regex = RegexValidator(r'https?:\/\/(www\.)?linkedin\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&\/\/=]*)',
	                                message="Veuillez entrer un lien au format: 'http(s)://(www.)linkedin.(...).")
	linkedin = models.URLField(validators=[linkedin_regex], blank=True, null=True)

	facebook_regex = RegexValidator(r'https?:\/\/(www\.)?facebook\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&\/\/=]*)',
	                                message="Veuillez entrer un lien au format: 'http(s)://(www.)facebook.(...).")
	facebook = models.URLField(validators=[facebook_regex], blank=True, null=True)

	twitter_regex = RegexValidator(r'https?:\/\/(www\.)?linkedin\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&\/\/=]*)',
	                               message="Veuillez entrer un lien au format: 'http(s)://(www.)linkedin.(...).")
	twitter = models.URLField(validators=[twitter_regex], blank=True, null=True)

	interests = models.TextField(blank=True, null=True)
