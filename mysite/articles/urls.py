from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('discover/', views.AllUserPostsView.as_view(), name="alluserpostsview"),
    path('<int:pk>/', views.PostsDetailView.as_view(), name="postsdetailview"),
]