from django.urls import path
from . import views
urlpatterns=[
    # path('', views.Welcome, name= "webpage"),
    # path('Home/', views.HomePage, name ="webpage"),
    # path('project/<str:pk>/',views.projects, name="webpage"),
    # path('admin/', admin.site.urls),
    # path('', include('App1.urls'))
    path('', views.webpage1,name="projects"),
    path('webpage2/', views.webpage2, name = "projects"),
]