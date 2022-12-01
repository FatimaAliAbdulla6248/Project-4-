from django.urls import path
from . import views

urlpatterns = [
  # New url pattern below
path('accounts/signup/', views.signup, name='signup'),
]