from django.urls import path
from . import views

urlpatterns = [
    path('api/match/', views.MatchGetList.as_view()),
    path('api/match/create', views.MatchCreate.as_view()),
    path('api/match/human/<str:pk>', views.MatchGetHuman.as_view())
]