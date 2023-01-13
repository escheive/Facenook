from django.urls import path
from . import views

app_name = 'main_app'
urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    # path('', views.Home, name='home'),
    # path('', views.homepage, name='home'),
    path('profile/<int:user_id>/', views.Profile.as_view(), name='profile'),
    path('about/', views.About.as_view(), name='about'),
    path('accounts/signup/', views.signup, name='signup'),
]
