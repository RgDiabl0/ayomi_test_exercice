# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):
	dependencies = [
		('connexion', '0007_auto_20180429_0001'),
	]

	operations = [
		migrations.RenameField(
			model_name='customuser',
			old_name='phone_number_regex',
			new_name='mobile_phone_number',
		),
	]
