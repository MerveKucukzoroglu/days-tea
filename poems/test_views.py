from django.test import TestCase
from .models import Post


class TestIndexViews(TestCase):
    def test_get_index_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')


class TestPostListViews(TestCase):
    def test_get_post_list_page(self):
        response = self.client.get('/poem_list/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'poem_list.html')


class TestProfileViews(TestCase):
    def test_profile_page(self):
        response = self.client.get('/profile')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profile.html')


class TestPublishPoemViews(TestCase):
    def test_can_publish_poem(self):
        response = self.client.get('/publish')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'publish.html')
