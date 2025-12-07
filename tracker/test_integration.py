
from django.test import TestCase, Client
from django.urls import reverse
from .models import CovidData

class TrackerIntegrationTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_extract_and_display_flow(self):
        # Step 1: Call the extract view
        response = self.client.get(reverse("extract_data"))
        self.assertEqual(response.status_code, 302)  # Redirect to /data/

        # Step 2: Follow redirect and check data
        response = self.client.get(reverse("show_data"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "USA")

        # Step 3: Check database state
        self.assertEqual(CovidData.objects.count(), 1)
        entry = CovidData.objects.first()
        self.assertGreater(entry.cases, 0)