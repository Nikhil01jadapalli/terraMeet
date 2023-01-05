from django.urls import path
from .views import RegisterView,MeetingView, LoginView
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)


urlpatterns = [
    path('register', RegisterView.as_view(), name="register"),
    path('login', LoginView.as_view(), name="login"),
    path('meeting/',MeetingView.as_view(),name='meeting')

]
