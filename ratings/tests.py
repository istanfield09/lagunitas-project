"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""
import decimal

from django.test import TestCase, Client
from models import Rating


class SimpleTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        client = Client()
        response = client.post('/rating/add/', {"brewery_name": "Ian's Place",
                                            "beer_name": "Mmm Beer",
                                            "score" : 2.3,
                                            "notes" : "good"})

    def test_get_rating(self):
        client = Client()
        response = client.get('/rating/1/')
        self.assertEqual(response.status_code, 200)

    def test_404_get_rating(self):
        client = Client()
        response = client.get('/rating/34')
        self.assertEqual(response.status_code, 404)

    def test_delete_rating(self):
        client = Client()
        response = client.post('/rating/1/delete')
        self.assertEqual(response.status_code, 302)
        response = client.get('/rating/1/')
        self.assertEqual(response.status_code, 404)

    def test_edit_rating(self):
        client = Client()
        response = client.post('/rating/1/', {"brewery_name": "Woop",
                                              "beer_name": "Grog",
                                              "score": 4.4,
                                              "notes": "eh"})
        self.assertEqual(response.status_code, 302)
        response = client.get('/rating/1/')
        self.assertEqual(response.status_code, 200)

        rating_obj = response.context['form'].cleaned_data
        self.assertEqual(rating_obj['brewery_name'], "Woop")
        self.assertEqual(rating_obj['beer_name'], "Grog")
        self.assertEqual(rating_obj['score'], decimal.Decimal('4.4'))
        self.assertEqual(rating_obj['notes'], "eh")
