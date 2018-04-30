# coding=utf-8
from django.test import TestCase

from connexion.models import CustomUser


class ModelsTest(TestCase):
	def test_customuser_creation(self):
		password = "test"
		username = "auvalade"
		first_name = "Aurélien"
		last_name = "Valade"
		email = "aurelien.valade@hoolders.com"
		birth_date = "2016-03-07"
		home_phone_number = "+33233467189"
		mobile_phone_number = "+33633467189"
		address = "dxtyhdxtgyh"
		city = "dxtyhdxtgyh"
		postal = "92140"
		website = "aurelienvalade.com"
		desc = "Je suis Aurélien Valade"
		linkedin = "http://linkedin.fr/auvalade"
		facebook = "http://facebook.fr/auvalade"
		twitter = "http://twitter.fr/auvalade"
		interests = "social"

		test_user = CustomUser.objects.create_user(username=username, first_name=first_name, last_name=last_name,
		                                           email=email,
		                                           password=password, birth_date=birth_date,
		                                           home_phone_number=home_phone_number,
		                                           mobile_phone_number=mobile_phone_number, address=address, city=city,
		                                           postal=postal, website=website, desc=desc, linkedin=linkedin,
		                                           facebook=facebook, twitter=twitter,
		                                           interests=interests).clean_fields()

		self.assertTrue(isinstance(test_user, CustomUser))

		return test_user

# VALIDATORS NOT WORKING...

# Haven't successfully done the email validation on the django side
# def test_customuser_creation_wrong_email(self):
# 	base_user = self.test_customuser_creation()
# 	user = base_user
#
# 	user.email = "test"
# 	user.clean_fields()
#
# 	self.assertFalse(isinstance(user, CustomUser))
#
# def test_customuser_creation_wrong_birthdate(self):
# 	base_user = self.test_customuser_creation()
# 	user = base_user
#
# 	try:
# 		user.birth_date = "07/03/2016"
# 	except ValidationError:
# 		user = ""
#
# 	self.assertFalse(isinstance(user, CustomUser))
#
# def test_customuser_creation_wrong_home_number(self):
# 	base_user = self.test_customuser_creation()
# 	user = base_user
#
# 	try:
# 		user.home_phone_number = "test"
# 	except ValidationError:
# 		user = ""
#
# 	self.assertFalse(isinstance(user, CustomUser))
#
# 	user = base_user
#
# 	try:
# 		user.home_phone_number = "0233948758"
# 	except ValidationError:
# 		user = ""
#
# 	self.assertFalse(isinstance(user, CustomUser))
#
# def test_customuser_creation_wrong_postal(self):
# 	base_user = self.test_customuser_creation()
# 	user = base_user
#
# 	try:
# 		user.postal = "test"
# 	except ValidationError:
# 		user = ""
#
# 	self.assertFalse(isinstance(user, CustomUser))
#
# def test_customuser_creation_wrong_website(self):
# 	base_user = self.test_customuser_creation()
# 	user = base_user
#
# 	try:
# 		user.website = "test"
# 	except ValidationError:
# 		user = ""
#
# 	self.assertFalse(isinstance(user, CustomUser))
#
# def test_customuser_creation_wrong_linkedin(self):
# 	base_user = self.test_customuser_creation()
# 	user = base_user
#
# 	try:
# 		user.facebook = "http://www.facebook.com/auvalade"
# 	except ValidationError:
# 		user = ""
#
# 	self.assertFalse(isinstance(user, CustomUser))
