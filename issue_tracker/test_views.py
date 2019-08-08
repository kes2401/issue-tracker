from django.test import TestCase
from .views import index
from django.urls import reverse


class TestViews(TestCase):

    def test_get_index_page(self):
        page = self.client.get(reverse('index'))
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'index.html')