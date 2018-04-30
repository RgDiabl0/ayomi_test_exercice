# coding=utf-8
from django.core.urlresolvers import reverse
from django.test import TestCase


class ViewsTest(TestCase):
	def test_index_view(self):
		url = reverse("index")
		resp = self.client.get(url)

		self.assertEqual(resp.status_code, 200)

	def test_profil_view(self):
		url = reverse("profile")
		resp = self.client.get(url)

		# Test should redirect to index because there isn't an user passed as parameter
		self.assertEqual(resp.status_code, 302)
