from mixer.backend.django import mixer

from mybudget.apps.envelopes.models import Envelopes
from mybudget.apps.general.models import Accounts
from mybudget.lib.init_test import MyTests


class EnvelopeFormTest(MyTests):
    def setUp(self):
        self.account = mixer.blend(Accounts)
        self.envelope = mixer.blend(Envelopes)
        self.envelope.name = 'clothes'
        self.envelope.monthly_replenishment = 150
        self.envelope.save()

    def test_envelope_form_create(self):
        response = self.client.post('/envelopes/create/',
                                    {'name': 'food',
                                    'monthly_replenishment': 300,
                                    'cash': False,
                                    'account': self.account.id},
                                    follow=False)
        self.assertRedirects(response, expected_url='/envelopes/all/', status_code=302)
        envelopes = Envelopes.objects.all()
        self.assertEqual(len(envelopes), 2)

    def test_envelope_update(self):
        response = self.client.post('/envelopes/1/update/',
                                    {'name': self.envelope.name,
                                     'monthly_replenishment': 100,
                                     'account': self.account.id}, follow=False)
        self.assertRedirects(response, expected_url='/envelopes/all/', status_code=302)
        envelopes = Envelopes.objects.all()
        self.assertEqual(envelopes[0].monthly_replenishment, 100)

    def test_select_by_envelope(self):
        response = self.client.post('/envelopes/select/', {'envelope': self.envelope.id}, follow=False)
        self.assertRedirects(response, expected_url='/expenses/clothes/', status_code=302)

