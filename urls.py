from django.contrib import admin
from django.urls import path
from api import views as api_views






urlpatterns = [
   
    path("", api_views.Login.as_view(), name="login"),
    # path("logout/", api_views.Logout.as_view(), name="logout"),
    path('dashboard/', api_views.Dashboard.as_view(), name='dashboard_view'),

    
]
