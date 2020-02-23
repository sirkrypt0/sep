from django.db import models
from datetime import *
# Create your models here.


class Lecturer(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Lecture(models.Model):
    SEMESTER_CHOICES = [
        (x, x) for x in range(1, 7)
    ]

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
    WEEKDAY_CHOICES = [
        (0, 'Monday'),
        (1, 'Tuesday'),
        (2, 'Wednesday'),
        (3, 'Thursday'),
        (4, 'Friday')
    ]
    TYPE_CHOICES = [
        (0, 'Lecture'),
        (1, 'Exercise')
    ]
    weekday = models.IntegerField(choices=WEEKDAY_CHOICES, default=0)
    time = models.TimeField(choices=TIME_CHOICES, verbose_name='Starting time')
    lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE)
    hall = models.CharField(max_length=20, default='HS 1')
    type = models.IntegerField(choices=TYPE_CHOICES, default=0)