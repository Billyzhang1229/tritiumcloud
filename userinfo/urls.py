from django.urls import path
from . import views

app_name = 'userinfo'
urlpatterns = [
    path('', views.HomeView.as_view(), name="homeview"),
    path('user/<slug:slug>/', views.UserProfileView.as_view(), name="userprofileview"),
]