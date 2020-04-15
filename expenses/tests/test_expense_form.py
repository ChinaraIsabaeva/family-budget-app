from mixer.backend.django import mixer

from envelopes import Envelopes
from core.models import Accounts
from expenses.models import Expenses
from core.base_test import MyTests


class ExpensesFormTests(MyTests):
    def setUp(self):
        self.account = mixer.blend(Accounts)
        self.envelope = mixer.blend(Envelopes)
        self.envelope.account = self.account
        self.envelope.current_amount = 100
        self.envelope.name = 'core'
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
