from django.test import TestCase

class Testing(TestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/mywatchlist/html/")
        self.assertEqual(response.status_code, 200)

    def test_url_exists_at_correct_location(self):
        response = self.client.get("/mywatchlist/xml/")
        self.assertEqual(response.status_code, 200)
        
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/mywatchlist/json/")
        self.assertEqual(response.status_code, 200)