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

		test = CustomUser.objects.create_user(username=username, first_name=first_name, last_name=last_name,
		                                      email=email,
		                                      password=password, birth_date=birth_date,
		                                      home_phone_number=home_phone_number,
		                                      mobile_phone_number=mobile_phone_number, address=address, city=city,
		                                      postal=postal, website=website, desc=desc, linkedin=linkedin,
		                                      facebook=facebook, twitter=twitter, interests=interests)

		self.assertTrue(isinstance(test, CustomUser))
