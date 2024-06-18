from django.urls import path
from .views import LandingPageView, UserLoginView, UserLogOutView, UserRegisterView

urlpatterns = [
    path('', LandingPageView.as_view(), name='landing'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogOutView.as_view(), name='logout'),
]