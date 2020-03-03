from django.shortcuts import render
from django.views.generic import TemplateView
from rest_framework import generics

from .models import Lecture
from .serializers import LectureSerializer


class HomePageView(TemplateView):
    template_name = 'home.html'


class ListLecture(generics.ListCreateAPIView):
    queryset = Lecture.objects.all()
    serializer_class = LectureSerializer


class DetailLecture(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lecture.objects.all()
    serializer_class = LectureSerializer
