from django.urls import path
from . import views

app_name = 'main_app'
urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    # path('profile_list/', views.ProfileList.as_view(), name='profile_list'),
    path('profile_list/', views.profile_list, name='profile_list'),
    path('profile/<int:user_id>/', views.ViewProfile.as_view(), name='profile'),
    path('about/', views.About.as_view(), name='about'),
    path('accounts/signup/', views.signup, name='signup'),
    path('post/', views.CreatePost.as_view(), name='create'),
]
