from .serializers import MatchSerializer
from rest_framework import generics
from rest_framework.response import Response
from django.http import JsonResponse
import requests
from faker import Faker
fake = Faker()
fake_age = fake.random_int(0, 100)

from .models import Match, Gender

class MatchGetList(generics.CreateAPIView):
    http_method_names = ['get', 'head']
    serializer_class = MatchSerializer
    queryset = Match.objects.all()
    
    def get(self, request):
        match_list = Match.objects.all()

        page = self.paginate_queryset(Match.objects.all())
        
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        return Response(match_list.values())

class MatchCreate(generics.CreateAPIView):
    http_method_names = ['post', 'head']

    def post(self, request):
        Match.objects.create(first_name=fake.first_name(), second_name=fake.last_name(), age=fake_age, gender=Gender.objects.all()[fake.random_element(elements=(0, 1))])
        
        return Response(Match.objects.all().values())

class MatchGetHuman(generics.CreateAPIView):
    http_method_names = ['get', 'head']

    def get(self, request, pk):
        r = requests.get(f'http://127.0.0.1:8000/api/human/{pk}')
        person = r.json()[0]
        if r.status_code == 200:
            Match.objects.create(id=pk, first_name = person['first_name'], second_name = person['second_name'], age = person['age'], gender =  Gender.objects.all()[person['gender_id'] - 1])

            return JsonResponse(person)