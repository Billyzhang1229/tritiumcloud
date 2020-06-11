from django.urls import path
from . import views

app_name = 'uniranking'
urlpatterns = [
    path('upload_uni_csv/', views.uni_csv_upload, name="uni_csv_upload"),
    ]