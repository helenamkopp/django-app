
from django.urls import path
from app import views

urlpatterns = [
    path('', views.home, name='home'),
    path('view_student/<int:pk>/', views.view_student, name='view_student')
]