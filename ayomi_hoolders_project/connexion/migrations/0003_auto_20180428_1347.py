# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import django.contrib.auth.models
import django.core.validators
import django.utils.timezone
from django.db import models, migrations


class Migration(migrations.Migration):
	dependencies = [
		('auth', '0006_require_contenttypes_0002'),
		('connexion', '0002_auto_20180428_1336'),
	]

	operations = [
		migrations.AlterModelOptions(
			name='customuser',
			options={'verbose_name': 'user', 'verbose_name_plural': 'users'},
		),
		migrations.AlterModelManagers(
			name='customuser',
			managers=[
				(b'objects', django.contrib.auth.models.UserManager()),
			],
		),
		migrations.AddField(
			model_name='customuser',
			name='groups',
			field=models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Group',
			                             blank=True,
			                             help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
			                             verbose_name='groups'),
		),
		migrations.AddField(
			model_name='customuser',
			name='is_active',
			field=models.BooleanField(default=True,
			                          help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.',
			                          verbose_name='active'),
		),
		migrations.AddField(
			model_name='customuser',
			name='is_staff',
			field=models.BooleanField(default=False,
			                          help_text='Designates whether the user can log into this admin site.',
			                          verbose_name='staff status'),
		),
		migrations.AddField(
			model_name='customuser',
			name='is_superuser',
			field=models.BooleanField(default=False,
			                          help_text='Designates that this user has all permissions without explicitly assigning them.',
			                          verbose_name='superuser status'),
		),
		migrations.AddField(
			model_name='customuser',
			name='user_permissions',
			field=models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Permission',
			                             blank=True, help_text='Specific permissions for this user.',
			                             verbose_name='user permissions'),
		),
		migrations.AlterField(
			model_name='customuser',
			name='date_joined',
			field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined'),
		),
		migrations.AlterField(
			model_name='customuser',
			name='email',
			field=models.EmailField(max_length=254, verbose_name='email address', blank=True),
		),
		migrations.AlterField(
			model_name='customuser',
			name='first_name',
			field=models.CharField(max_length=30, verbose_name='first name', blank=True),
		),
		migrations.AlterField(
			model_name='customuser',
			name='last_name',
			field=models.CharField(max_length=30, verbose_name='last name', blank=True),
		),
		migrations.AlterField(
			model_name='customuser',
			name='username',
			field=models.CharField(error_messages={'unique': 'A user with that username already exists.'},
			                       max_length=30, validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$',
			                                                                                        'Enter a valid username. This value may contain only letters, numbers and @/./+/-/_ characters.',
			                                                                                        'invalid')],
			                       help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.',
			                       unique=True, verbose_name='username'),
		),
	]
