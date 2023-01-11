from django.urls import path
from . import views

app_name = 'main_app'
urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about/', views.About.as_view(), name='about'),
]
