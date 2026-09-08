from django.urls import path
from portal_group import views

urlpatterns = [
    path('', views.MainView.as_view(), name='main'),
]
