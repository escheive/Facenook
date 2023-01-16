from django.urls import path
from . import views

app_name = 'main_app'
urlpatterns = [
    path('', views.home, name='home'),
    # path('profile_list/', views.ProfileList.as_view(), name='profile_list'),
    # path('profile/<int:user_id>/', views.MyProfile.as_view(), name='profile'),
    path('profile_list/', views.profile_list, name='profile_list'),
    path('view_profile/<int:pk>/', views.view_profile, name='view_profile'),
    path('about/', views.About.as_view(), name='about'),
    path('accounts/signup/', views.signup, name='signup'),
    path('post/', views.CreatePost.as_view(), name='create'),
    path('explore/', views.explore, name='explore')
]
