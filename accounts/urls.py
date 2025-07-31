from django.urls import path 
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('success/', views.success_view, name='registration_successful'),
    path('login/', views.login_view, name='login'),
]