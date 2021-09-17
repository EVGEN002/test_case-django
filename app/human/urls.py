from django.urls import path
from . import views
from rest_framework import routers

urlpatterns = [
    path('api/human/', views.HumanGetPost.as_view()),
    path('api/human/<str:pk>', views.HumanDeletePutGetId.as_view()),
    path('api/human/delete_all', views.DeleteAll.as_view()),
    path('api/human/create_all', views.CreateAll.as_view())
]