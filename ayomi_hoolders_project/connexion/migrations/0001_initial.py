# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import django.core.validators
from django.db import models, migrations


class Migration(migrations.Migration):
	dependencies = [
	]

	operations = [
		migrations.CreateModel(
			name='CustomUser',
			fields=[
				('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
				('password', models.CharField(max_length=128, verbose_name='password')),
				('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
				('birth_date', models.DateField()),
				('home_phone_number', models.CharField(blank=True, max_length=17, validators=[
					django.core.validators.RegexValidator(regex=b'^\\+?1?\\d{9,15}$',
					                                      message=b"Veuillez entrer un num\xc3\xa9ro de t\xc3\xa9l\xc3\xa9phone au format: '+999999999'..")])),
				('phone_number_regex', models.CharField(blank=True, max_length=17, validators=[
					django.core.validators.RegexValidator(regex=b'^\\+?1?\\d{9,15}$',
					                                      message=b"Veuillez entrer un num\xc3\xa9ro de t\xc3\xa9l\xc3\xa9phone au format: '+999999999'..")])),
				('address', models.CharField(default=b'non rempli', max_length=30)),
				('city', models.CharField(default=b'non rempli', max_length=30)),
				('postal', models.CharField(default=b'0', max_length=5, validators=[
					django.core.validators.RegexValidator(b'^[0-9]*',
					                                      message=b'Ce champs ne peut contenir que des chiffres.')])),
				('website', models.URLField()),
				('desc', models.TextField()),
				('linkedin', models.URLField(blank=True, validators=[django.core.validators.RegexValidator(
					b'https?:\\/\\/(www\\.)?linkedin\\.[a-z]{2,6}\\b([-a-zA-Z0-9@:%_\\+.~#?&\\/\\/=]*)',
					message=b"Veuillez entrer un lien au format: 'http(s)://(www.)linkedin.(...).")])),
				('facebook', models.URLField(blank=True, validators=[django.core.validators.RegexValidator(
					b'https?:\\/\\/(www\\.)?facebook\\.[a-z]{2,6}\\b([-a-zA-Z0-9@:%_\\+.~#?&\\/\\/=]*)',
					message=b"Veuillez entrer un lien au format: 'http(s)://(www.)facebook.(...).")])),
				('twitter', models.URLField(blank=True, validators=[django.core.validators.RegexValidator(
					b'https?:\\/\\/(www\\.)?linkedin\\.[a-z]{2,6}\\b([-a-zA-Z0-9@:%_\\+.~#?&\\/\\/=]*)',
					message=b"Veuillez entrer un lien au format: 'http(s)://(www.)linkedin.(...).")])),
				('interests', models.TextField()),
			],
			options={
				'abstract': False,
			},
		),
	]
