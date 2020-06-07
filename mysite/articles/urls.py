from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('discover/', views.AllUserPostsView.as_view(), name="alluserpostsview"),
    path('<int:pk>/', views.PostsDetailView.as_view(), name="postsdetailview"),
    path('create/', views.create_post_view, name='createpostview'),
    path('category/', views.TagListView.as_view(), name='tagview'),
    path('category/<tagname>/', views.TagDeatailView.as_view(), name="tagdetailview")
    ]