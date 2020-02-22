from django.db import models

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
    hall = models.CharField(max_length=20, default='HS 1')
    description = models.TextField()

    def __str__(self):
        return self.title
