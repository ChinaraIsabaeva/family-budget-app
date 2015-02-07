from django.test import TestCase
from django.test import Client


class MyTests(TestCase):

    def setUp(self):
        self.client = Client()

