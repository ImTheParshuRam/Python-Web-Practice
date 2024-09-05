from django.urls import path
from . import views
urlpatterns=[
    path('', views.Welcome, name= "webpage"),
    path('Home/', views.HomePage, name ="webpage"),
    path('project/<str:pk>/',views.projects, name="webpage"),
]