from django.test import TestCase
from django.urls import reverse


class HomeViewTests(TestCase):
    def test_home_page_displays_dashboard_summary(self):
        response = self.client.get(reverse("home"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "dashboard/home.html")
        self.assertContains(response, "<h1>Recipe Dashboard</h1>", html=True)
        self.assertContains(response, "Recently Cooked")
        self.assertContains(response, "Chicken Alfredo")
        self.assertContains(response, "Cooked on July 21, 2026")
        self.assertContains(response, "Suggested Next Meal")
        self.assertContains(response, "Beef Tacos with Spanish Rice")
        self.assertContains(response, "Last cooked on June 30, 2026")
        self.assertContains(
            response,
            "This meal has not been cooked recently and fits a familiar weeknight dinner.",
        )
