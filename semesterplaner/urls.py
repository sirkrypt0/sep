from django.urls import path

from . import views

urlpatterns = [
    path('', views.ListLecture.as_view()),
    path('<int:pk>/', views.DetailLecture.as_view()),
]