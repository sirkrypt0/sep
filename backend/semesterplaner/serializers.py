from rest_framework import serializers
from .models import *


class TimeSlotSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'weekday',
            'time',
            'hall',
            'type'
        )
        model = TimeSlot


class LectureSerializer(serializers.ModelSerializer):
    timeslots = TimeSlotSerializer(source='timeslot_set', many=True, read_only=True)

    class Meta:
        fields = (
            'id',
            'title',
            'lp',
            'semester',
            'description',
            'timeslots',
        )
        depth = 1
        model = Lecture
