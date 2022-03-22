from django.test import TestCase
from .forms import PoemForm


class TestPoemForm(TestCase):

    def test_post_title_is_required(self):
        form = PoemForm(({'title': ''}))
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors.keys())
        self.assertEqual(form.errors['title'][0], 'This field is required.')
