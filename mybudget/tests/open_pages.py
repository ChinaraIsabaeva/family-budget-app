from . import MyTests


class OpenPagesTests(MyTests):

    def test_open_main_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='home.html')

