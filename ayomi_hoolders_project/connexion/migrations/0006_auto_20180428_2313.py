# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import django.core.validators
from django.db import models, migrations


class Migration(migrations.Migration):
	dependencies = [
		('connexion', '0005_auto_20180428_1350'),
	]

	operations = [
		migrations.AlterField(
			model_name='customuser',
			name='address',
			field=models.CharField(max_length=30),
		),
		migrations.AlterField(
			model_name='customuser',
			name='city',
			field=models.CharField(max_length=30),
		),
		migrations.AlterField(
			model_name='customuser',
			name='desc',
			field=models.TextField(),
		),
		migrations.AlterField(
			model_name='customuser',
			name='interests',
			field=models.TextField(),
		),
		migrations.AlterField(
			model_name='customuser',
			name='postal',
			field=models.CharField(blank=True, max_length=5, validators=[
				django.core.validators.RegexValidator(b'^[0-9]*',
				                                      message=b'Ce champs ne peut contenir que des chiffres.')]),
		),
	]
