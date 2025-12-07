from django.test import TestCase, Client
from django.urls import reverse
from .models import CovidData

class CovidDataTests(TestCase):
    def setUp(self):
        # Create a sample record
        self.sample = CovidData.objects.create(
            country="USA",
            cases=100,
            deaths=10,
            recovered=50
        )
        self.client = Client()

    def test_model_creation(self):
        """Test that the CovidData model saves correctly"""
        self.assertEqual(self.sample.country, "USA")
        self.assertEqual(self.sample.cases, 100)
        self.assertEqual(self.sample.deaths, 10)
        self.assertEqual(self.sample.recovered, 50)

    def test_show_data_view(self):
        """Test that the /data/ view returns 200 and contains the sample"""
        url = reverse("show_data")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "USA")
        self.assertContains(response, "100")

    def test_extract_data_view(self):
        """Test that /extract/ inserts a new record"""
        url = reverse("extract_data")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)  # redirect to /data/
        self.assertEqual(CovidData.objects.count(), 2)  # one sample + one new