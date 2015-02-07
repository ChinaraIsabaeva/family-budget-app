from mixer.backend.django import mixer

from . import MyTests
from mybudget.apps.budget.models import Expenses, Envelopes, Accounts


class ExpensesFormTests(MyTests):
    def setUp(self):
        self.account = mixer.blend(Accounts)
        self.envelope = mixer.blend(Envelopes)
        self.envelope.account = self.account
        self.envelope.current_amount = 50
        self.envelope.save()

    def test_expense_create(self):
        response = self.client.post('/', {'name': 'food', 'amount': 25, 'envelope': self.envelope.id}, follow=False)
        self.assertRedirects(response, expected_url='/expenses/', status_code=302)
        expenses = Expenses.objects.all()
        envelopes = Envelopes.objects.all()
        self.assertEqual(len(expenses), 1)
        self.assertEqual(envelopes[0].current_amount, 25)


class EnvelopeFormTest(MyTests):
    def setUp(self):
        self.account = mixer.blend(Accounts)

    def test_envelope_form_create(self):
        response = self.client.post('/envelopes/',
                                    {'name': 'food',
                                    'monthly_replenishment': 300,
                                    'cash': False,
                                    'account': self.account.id},
                                    follow=False)
        self.assertRedirects(response, expected_url='/envelopes/', status_code=302)
        envelopes = Envelopes.objects.all()
        self.assertEqual(len(envelopes), 1)




