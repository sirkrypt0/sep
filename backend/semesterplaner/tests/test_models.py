from datetime import time
from django.test import TestCase

# Create your tests here.
from semesterplaner.models import Lecturer, Lecture, TimeSlot


class LecturerModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Lecturer.objects.create(name='Tester')

    def test_name_content(self):
        lecturer = Lecturer.objects.first()
        expected_name = f'{lecturer.name}'
        self.assertEqual(expected_name, 'Tester')


class LectureModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Lecturer.objects.create(name='Tester')
        Lecture.objects.create(title='Test_lecture',
                               lp=6,
                               semester=2,
                               lecturer_id=Lecturer.objects.first().pk,
                               description='Test description')

    def test_title_content(self):
        lecture = Lecture.objects.first()
        expected_title = f'{lecture.title}'
        self.assertEqual(expected_title, 'Test_lecture')

    def test_lp_content(self):
        lecture = Lecture.objects.first()
        expected_lp = lecture.lp
        self.assertEqual(expected_lp, 6)

    def test_semester_content(self):
        lecture = Lecture.objects.first()
        expected_semester = lecture.semester
        self.assertEqual(expected_semester, 2)

    def test_lecturer_content(self):
        lecture = Lecture.objects.first()
        expected_lecturer = lecture.lecturer.name
        self.assertEqual(expected_lecturer, 'Tester')

    def test_description_content(self):
        lecture = Lecture.objects.first()
        expected_description = lecture.description
        self.assertEqual(expected_description, 'Test description')


class TimeSlotModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Lecturer.objects.create(name='Tester')
        Lecture.objects.create(title='Test_lecture',
                               lp=6,
                               semester=2,
                               lecturer_id=Lecturer.objects.first().pk,
                               description='Test description')
        TimeSlot.objects.create(weekday=0,
                                time=time(9, 00),
                                duration=45,
                                lecture_id=Lecture.objects.first().pk,
                                hall='HS 2',
                                type=0)

    def test_weekday_content(self):
        timeslot = TimeSlot.objects.first()
        expected_weekday = timeslot.weekday
        self.assertEqual(expected_weekday, 0)

    def test_time_content(self):
        timeslot = TimeSlot.objects.first()
        expected_time = timeslot.time
        self.assertEqual(expected_time, time(9, 00))

    def test_duration_content(self):
        timeslot = TimeSlot.objects.first()
        expected_duration = timeslot.duration
        self.assertEqual(expected_duration, 45)

    def test_lecture_content(self):
        timeslot = TimeSlot.objects.first()
        expected_lecture = timeslot.lecture.title
        self.assertEqual(expected_lecture, 'Test_lecture')

    def test_hall_content(self):
        timeslot = TimeSlot.objects.first()
        expected_hall = timeslot.hall
        self.assertEqual(expected_hall, 'HS 2')

    def test_type_content(self):
        timeslot = TimeSlot.objects.first()
        expected_type = timeslot.type
        self.assertEqual(expected_type, 0)
