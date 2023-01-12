from django.urls import path
from . import views

# app_name = 'main_app'
urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    # path('', views.homepage, name='home'),
    path('about/', views.About.as_view(), name='about'),
    path('accounts/signup/', views.signup, name='signup'),
]
