from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('lectures/', views.ListLecture.as_view()),
    path('lectures/<int:pk>/', views.DetailLecture.as_view()),
]