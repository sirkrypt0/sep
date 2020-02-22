from rest_framework import serializers
from .models import Lecture


class LectureSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'title',
            'lp',
            'semester',
            'hall',
            'description'
        )
        model = Lecture
