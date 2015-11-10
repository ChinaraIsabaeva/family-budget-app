from mixer.backend.django import mixer

from mybudget.apps.envelopes.models import Envelopes
from mybudget.apps.general.models import Accounts
from mybudget.lib.init_test import MyTests


class EnvelopeFormTest(MyTests):
    def setUp(self):
        self.account = mixer.blend(Accounts)

    def test_envelope_form_create(self):
        response = self.client.post('/envelopes/create/',
                                    {'name': 'food',
                                    'monthly_replenishment': 300,
                                    'cash': False,
                                    'account': self.account.id},
                                    follow=False)
        self.assertRedirects(response, expected_url='/envelopes/', status_code=302)
        envelopes = Envelopes.objects.all()
        self.assertEqual(len(envelopes), 1)

