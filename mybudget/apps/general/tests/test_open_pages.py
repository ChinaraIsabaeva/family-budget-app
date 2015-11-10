from mybudget.lib.init_test import MyTests


class OpenPagesTests(MyTests):

    def test_open_main_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='home.html')

    def test_open_dashboard(self):
        response = self.client.get('/envelopes/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='envelopes/envelopes.html')

    def test_open_expenses(self):
        response = self.client.get('/expenses/all/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='expenses/expenses.html')