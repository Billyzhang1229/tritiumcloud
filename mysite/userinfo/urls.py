from django.urls import path
from . import views

app_name = 'userinfo'
urlpatterns = [
    path('', views.HomeView.as_view()),
    path('<slug:slug>/', views.UserProfileView.as_view()),
]