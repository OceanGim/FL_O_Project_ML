from django.urls import path, include
from user import views

app_name = "user"

urlpatterns = [
    path('searchuser/', views.searchuser, name="searchuser"),
]
