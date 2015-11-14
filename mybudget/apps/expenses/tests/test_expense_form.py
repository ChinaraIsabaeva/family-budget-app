from mixer.backend.django import mixer

from mybudget.apps.envelopes.models import Envelopes
from mybudget.apps.general.models import Accounts
from mybudget.apps.expenses.models import Expenses
from mybudget.lib.init_test import MyTests


class ExpensesFormTests(MyTests):
    def setUp(self):
        self.account = mixer.blend(Accounts)
        self.envelope = mixer.blend(Envelopes)
        self.envelope.account = self.account
        self.envelope.current_amount = 100
        self.envelope.name = 'general'
        self.envelope.save()
        self.expense = mixer.blend(Expenses, name='clothes', amount=50, envelope=self.envelope, id=1)

    def test_expense_create(self):
        response = self.client.post('/', {'name': 'Asda', 'amount': 25, 'envelope': self.envelope.id}, follow=False)
        self.assertRedirects(response, expected_url='/', status_code=302)
        expenses = Expenses.objects.all()
        envelopes = Envelopes.objects.all()
        self.assertEqual(len(expenses), 2)
        self.assertEqual(envelopes[0].current_amount, 25)

    def test_expense_update(self):
        response = self.client.post('/expenses/1/update/', {'name': 'Danik shoes', 'amount': 25, 'envelope': self.envelope.id}, follow=False)
        self.assertRedirects(response, expected_url='/expenses/all/', status_code=302)
        expenses = Expenses.objects.all()
        envelopes = Envelopes.objects.all()
        self.assertEqual(expenses[0].amount, 25)
        self.assertEqual(expenses[0].name, 'Danik shoes')
        self.assertEqual(envelopes[0].current_amount, 75)

    def test_expense_by_envelope(self):
        response = self.client.post('/expenses/all/', {'envelope': self.envelope.id}, follow=False)
        self.assertRedirects(response, expected_url='/expenses/general/', status_code=302)
