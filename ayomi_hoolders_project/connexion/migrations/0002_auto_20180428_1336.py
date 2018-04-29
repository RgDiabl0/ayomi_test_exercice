# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime

from django.db import models, migrations
from django.utils.timezone import utc


class Migration(migrations.Migration):
	dependencies = [
		('connexion', '0001_initial'),
	]

	operations = [
		migrations.AddField(
			model_name='customuser',
			name='date_joined',
			field=models.DateTimeField(default=datetime.datetime(2018, 4, 28, 11, 36, 51, 596919, tzinfo=utc)),
		),
		migrations.AddField(
			model_name='customuser',
			name='email',
			field=models.EmailField(max_length=30, blank=True),
		),
		migrations.AddField(
			model_name='customuser',
			name='first_name',
			field=models.CharField(default=b'non rempli', max_length=30),
		),
		migrations.AddField(
			model_name='customuser',
			name='last_name',
			field=models.CharField(default=b'non rempli', max_length=30),
		),
		migrations.AddField(
			model_name='customuser',
			name='username',
			field=models.CharField(default=b'non rempli', max_length=10),
		),
		migrations.AlterField(
			model_name='customuser',
			name='desc',
			field=models.TextField(default=b'non rempli'),
		),
		migrations.AlterField(
			model_name='customuser',
			name='interests',
			field=models.TextField(default=b'non rempli'),
		),
		migrations.AlterField(
			model_name='customuser',
			name='website',
			field=models.URLField(blank=True),
		),
	]
