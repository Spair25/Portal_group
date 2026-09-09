from django.urls import path
from portal_group import views

urlpatterns = [
    path('', views.MainView.as_view(), name='main'),
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('profile/', profile, name='profile'),
    path('profile/edit/', edit_profile, name='edit_profile'),
    path('logout/', logout_view, name='logout'),
]
