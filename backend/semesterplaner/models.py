from django.db import models
from datetime import *
import calendar
# Create your models here.


class Lecturer(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Lecture(models.Model):
    SEMESTER_CHOICES = [(x, x) for x in range(1, 7)]

    title = models.CharField(max_length=200)
    lp = models.IntegerField(default=6)
    semester = models.IntegerField(choices=SEMESTER_CHOICES, default=1)
    lecturer = models.ForeignKey(Lecturer, on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return self.title


class TimeSlot(models.Model):
    TIME_CHOICES = [
        (time(9, 00), '9:00'),
        (time(9, 15), '9:15'),
        (time(11, 00), '11:00'),
        (time(13, 30), '13:30'),
        (time(15, 15), '15:15'),
        (time(17, 00), '17:00')
    ]
    WEEKDAY_CHOICES = [(i, calendar.day_name[i]) for i in range(5)]
    TYPE_CHOICES = [
        (0, 'Lecture'),
        (1, 'Exercise')
    ]
    DURATION_CHOICES = [(45 * i, 45 * i) for i in range(1, 9)]

    weekday = models.IntegerField(choices=WEEKDAY_CHOICES, default=0)
    time = models.TimeField(choices=TIME_CHOICES, verbose_name='Starting time')
    duration = models.IntegerField(choices=DURATION_CHOICES, default=90)
    lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE)
    hall = models.CharField(max_length=20, default='HS 1')
    type = models.IntegerField(choices=TYPE_CHOICES, default=0)