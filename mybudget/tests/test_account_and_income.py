from mixer.backend.django import mixer

from . import MyTests
from mybudget.apps.envelopes.models import Envelopes
from mybudget.apps.general.models import Incomes, Accounts


class IncomeAccountTest(MyTests):
    def setUp(self):
        self.account_one = mixer.blend(Accounts, name="Danik_card", current_amount=250)
        self.account_two = mixer.blend(Accounts, name="Chee_card", current_amount=75)
        self.income_one = mixer.blend(Incomes, name='Danik', amount=500, account=self.account_one)
        self.income_two = mixer.blend(Incomes, name='Chee', amount=100, account=self.account_two)
        self.envelope_one = mixer.blend(Envelopes, name='Food', current_amount=50, account=self.account_one)
        self.envelope_two = mixer.blend(Envelopes, name='Clothes', current_amount=50, account=self.account_two)


class IncomeTest(IncomeAccountTest):
    def test_incomes_summed(self):
        response = self.client.get('/envelopes/')
        self.assertEqual(response.context['available_amount'], 600)


class AccountsTest(IncomeAccountTest):
    def test_account_summed(self):
        response = self.client.get('/')
        self.assertEqual(response.context['account'], 325)

    def test_envelope_one_bind_correctly(self):
        response = self.client.post('/', {'name': 'Asda', 'amount': 25, 'envelope': self.envelope_one.id}, follow=False)
        self.assertRedirects(response, expected_url='/', status_code=302)
        envelope = Envelopes.objects.get(name='Food')
        account = Accounts.objects.get(name='Danik_card')
        self.assertEqual(envelope.current_amount, 25)
        self.assertEqual(account.current_amount, 225)

    def test_envelope_two_bind_correctly(self):
        response = self.client.post('/', {'name': 'M&S', 'amount': 50, 'envelope': self.envelope_two.id}, follow=False)
        self.assertRedirects(response, expected_url='/', status_code=302)
        envelope = Envelopes.objects.get(name='Clothes')
        account = Accounts.objects.get(name='Chee_card')
        self.assertEqual(envelope.current_amount, 0)
        self.assertEqual(account.current_amount, 25)


