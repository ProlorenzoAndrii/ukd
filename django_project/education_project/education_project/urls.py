from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path("", views.student_list, name="home"),
    path('students/create/', views.student_create, name='student_create'),
    path('students/', views.student_list, name='student_list'),
    path('students/<int:student_id>/delete/', views.student_delete, name='student_delete'),
]