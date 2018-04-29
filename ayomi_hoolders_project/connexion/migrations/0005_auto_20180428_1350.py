# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
	dependencies = [
		('connexion', '0004_auto_20180428_1349'),
	]

	operations = [
		migrations.AlterField(
			model_name='customuser',
			name='birth_date',
			field=models.DateField(null=True),
		),
	]
