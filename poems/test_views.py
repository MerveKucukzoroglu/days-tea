from django.test import TestCase
from .models import Post


class TestViews(TestCase):

    def test_get_index_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test__get_post_list_page(self):
        response = self.client.get('/poem_list/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'poem_list.html')
