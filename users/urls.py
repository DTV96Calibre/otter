from django.urls import path

from . import views

app_name = 'users'
urlpatterns = [
	path('index/', views.index, name='index'),
    path('@<handle>/', views.profile, name='profile'),
    path('@<handle>/likes/', views.likes, name='likes'),
    path('@<handle>/following/', views.following, name='following'),
    path('@<handle>/followers/', views.followers, name='followers'),
]
