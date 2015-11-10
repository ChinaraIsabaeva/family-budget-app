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
        self.envelope.current_amount = 50
        self.envelope.save()

    def test_expense_create(self):
        response = self.client.post('/', {'name': 'food', 'amount': 25, 'envelope': self.envelope.id}, follow=False)
        self.assertRedirects(response, expected_url='/', status_code=302)
        expenses = Expenses.objects.all()
        envelopes = Envelopes.objects.all()
        self.assertEqual(len(expenses), 1)
        self.assertEqual(envelopes[0].current_amount, 25)
