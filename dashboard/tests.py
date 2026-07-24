from django.test import TestCase
from django.urls import reverse


class HomeViewTests(TestCase):
    def test_home_page_displays_dashboard_message(self):
        response = self.client.get(reverse("home"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Recipe Dashboard is running.")