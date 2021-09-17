from django.db.models.base import Model
from rest_framework import generics
from rest_framework.response import Response
from .serializers import HumanSerializer

from faker import Faker
fake = Faker()
fake_age = fake.random_int(0, 100)


from .models import Gender, Human

class HumanGetPost(generics.CreateAPIView):
    http_method_names = ['get', 'post', 'head']
    serializer_class = HumanSerializer
    queryset = Human.objects.all()

    def get(self, request):
        human_list = Human.objects.all()
        page = self.paginate_queryset(human_list)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        return Response(human_list.values())

    def post(self, request):
        serializer = HumanSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class HumanDeletePutGetId(generics.CreateAPIView):
    http_method_names = ['get', 'delete', 'put', 'head']
    serializer_class = HumanSerializer
    queryset = Human.objects.all()

    def get(self, request, pk):
        human_id = Human.objects.filter(pk=pk)
        return Response(human_id.values())

    def delete(self, reqeust, pk):
        human_id = Model.delete(Human.objects.get(pk=pk))
        return Response(human_id)

    def put(self, request, pk):
        human_id = Human.objects.get(pk=pk)
        serializer = HumanSerializer(human_id, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class DeleteAll(generics.CreateAPIView):
    http_method_names = ['delete', 'head']

    def delete(self, request):
        return Response(Human.objects.all().delete())

class CreateAll(generics.CreateAPIView):
    http_method_names = ['post', 'head']

    def post(self, request):
        Human.objects.create(first_name=fake.first_name(), second_name=fake.last_name(), age=fake_age, gender=Gender.objects.all()[fake.random_element(elements=(0, 1))])
        return Response(Human.objects.all().values())

