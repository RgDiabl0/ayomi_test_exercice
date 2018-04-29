# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import django.core.validators
from django.db import models, migrations


class Migration(migrations.Migration):
	dependencies = [
		('connexion', '0006_auto_20180428_2313'),
	]

	operations = [
		migrations.AlterField(
			model_name='customuser',
			name='address',
			field=models.CharField(max_length=30, null=True, blank=True),
		),
		migrations.AlterField(
			model_name='customuser',
			name='birth_date',
			field=models.DateField(null=True, blank=True),
		),
		migrations.AlterField(
			model_name='customuser',
			name='city',
			field=models.CharField(max_length=30, null=True, blank=True),
		),
		migrations.AlterField(
			model_name='customuser',
			name='desc',
			field=models.TextField(null=True, blank=True),
		),
		migrations.AlterField(
			model_name='customuser',
			name='facebook',
			field=models.URLField(blank=True, null=True, validators=[django.core.validators.RegexValidator(
				b'https?:\\/\\/(www\\.)?facebook\\.[a-z]{2,6}\\b([-a-zA-Z0-9@:%_\\+.~#?&\\/\\/=]*)',
				message=b"Veuillez entrer un lien au format: 'http(s)://(www.)facebook.(...).")]),
		),
		migrations.AlterField(
			model_name='customuser',
			name='home_phone_number',
			field=models.CharField(blank=True, max_length=17, null=True, validators=[
				django.core.validators.RegexValidator(regex=b'^\\+?1?\\d{9,15}$',
				                                      message=b"Veuillez entrer un num\xc3\xa9ro de t\xc3\xa9l\xc3\xa9phone au format: '+999999999'..")]),
		),
		migrations.AlterField(
			model_name='customuser',
			name='interests',
			field=models.TextField(null=True, blank=True),
		),
		migrations.AlterField(
			model_name='customuser',
			name='linkedin',
			field=models.URLField(blank=True, null=True, validators=[django.core.validators.RegexValidator(
				b'https?:\\/\\/(www\\.)?linkedin\\.[a-z]{2,6}\\b([-a-zA-Z0-9@:%_\\+.~#?&\\/\\/=]*)',
				message=b"Veuillez entrer un lien au format: 'http(s)://(www.)linkedin.(...).")]),
		),
		migrations.AlterField(
			model_name='customuser',
			name='phone_number_regex',
			field=models.CharField(blank=True, max_length=17, null=True, validators=[
				django.core.validators.RegexValidator(regex=b'^\\+?1?\\d{9,15}$',
				                                      message=b"Veuillez entrer un num\xc3\xa9ro de t\xc3\xa9l\xc3\xa9phone au format: '+999999999'..")]),
		),
		migrations.AlterField(
			model_name='customuser',
			name='postal',
			field=models.CharField(blank=True, max_length=5, null=True, validators=[
				django.core.validators.RegexValidator(b'^[0-9]*',
				                                      message=b'Ce champs ne peut contenir que des chiffres.')]),
		),
		migrations.AlterField(
			model_name='customuser',
			name='twitter',
			field=models.URLField(blank=True, null=True, validators=[django.core.validators.RegexValidator(
				b'https?:\\/\\/(www\\.)?linkedin\\.[a-z]{2,6}\\b([-a-zA-Z0-9@:%_\\+.~#?&\\/\\/=]*)',
				message=b"Veuillez entrer un lien au format: 'http(s)://(www.)linkedin.(...).")]),
		),
		migrations.AlterField(
			model_name='customuser',
			name='website',
			field=models.URLField(null=True, blank=True),
		),
	]
