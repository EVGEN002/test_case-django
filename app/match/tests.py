from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from rest_framework.test import APIRequestFactory

# Create your tests here.

from .models import Match, Gender

client = Client()
factory = APIRequestFactory()

class MatchTest(TestCase):
    def setUp(self) -> None:
        self.gender = [Gender.objects.create(gender='male'), Gender.objects.create(gender='female')]
        self.match = Match.objects.create(
            first_name='testFirst', 
            second_name='testSecond', 
            age=99, 
            gender=self.gender[0]
        )

    def test_get_match_list(self):
        response = client.get('/api/match/')
        self.assertEqual(response.status_code, 200)
        data = response.json()['results'][0]
        self.assertEqual(data['first_name'], 'testFirst')
        self.assertEqual(data['second_name'], 'testSecond')
        self.assertEqual(data['age'], 99)
        self.assertEqual(data['gender'], 1)