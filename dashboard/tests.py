from django.test import TestCase
from django.urls import reverse


class HomeViewTests(TestCase):
    def test_home_page_uses_dashboard_template(self):
        response = self.client.get(reverse("home"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "dashboard/home.html")
        self.assertContains(response, "<h1>Recipe Dashboard</h1>", html=True)
