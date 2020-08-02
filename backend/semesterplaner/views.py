from rest_framework import generics

from .models import Lecture
from .serializers import LectureSerializer


class ListLecture(generics.ListCreateAPIView):
    queryset = Lecture.objects.all()
    serializer_class = LectureSerializer


class DetailLecture(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lecture.objects.all()
    serializer_class = LectureSerializer
