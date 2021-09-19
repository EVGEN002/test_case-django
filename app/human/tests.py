
from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from rest_framework.test import APIRequestFactory

# Create your tests here.

from .models import Human, Gender

User = get_user_model()
client = Client()
factory = APIRequestFactory()

class HumanTest(TestCase):
    def setUp(self) -> None:
        self.user = User.objects.create(username='testuser', password='password')
        self.gender = Gender.objects.create(gender='male')
        self.human = Human.objects.create(
            first_name='testFirst', 
            second_name='testSecond', 
            age=99, 
            gender=self.gender
        )

    def test_get_human_list(self):
        response = client.get('/api/human/')
        data = response.json()['results'][0]
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['first_name'], 'testFirst')
        self.assertEqual(data['second_name'], 'testSecond')
        self.assertEqual(data['age'], 99)
        self.assertEqual(data['gender'], 1)

    def test_get_human_by_id(self):
        response = client.get('/api/human/1')
        self.assertEqual(response.status_code, 200)
        data = response.json()[0]
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['first_name'], 'testFirst')
        self.assertEqual(data['second_name'], 'testSecond')
        self.assertEqual(data['age'], 99)
        self.assertEqual(data['gender_id'], 1)

    def test_post_human(self):
        response = client.post('/api/human/', {'first_name': 'postFirst', 'second_name': 'postSecond', 'age': 99, 'gender': 1})
        data = response.json()
        self.assertEqual(data['first_name'], 'postFirst')
        self.assertEqual(data['second_name'], 'postSecond')
        self.assertEqual(data['age'], 99)
        self.assertEqual(data['gender'], 1)
        self.assertEqual(response.status_code, 200)

    def test_put_human(self):
        response = client.put('/api/human/1', {"first_name": "putFirst", "second_name": "putSecond", "age": 100, "gender": 1},  content_type='application/json')
        data = response.json()
        self.assertEqual(data['first_name'], 'putFirst')
        self.assertEqual(data['first_name'], 'putFirst')
        self.assertEqual(data['age'], 100)
        self.assertEqual(data['gender'], 1)

    def test_delete_human(self):
        response = client.delete('/api/human/1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()[0], 1)