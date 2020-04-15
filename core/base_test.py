from django.test import TestCase, Client


class MyTests(TestCase):

    def setUp(self):
        self.client = Client()
