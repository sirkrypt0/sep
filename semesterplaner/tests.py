from django.test import TestCase
from .models import *

# Create your tests here.


class LecturerModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Lecturer.objects.create(name='Tester')

    def test_name_content(self):
        lecturer = Lecturer.objects.get(id=1)
        expected_name = f'{lecturer.name}'
        self.assertEquals(expected_name, 'Tester')


class LectureModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Lecturer.objects.create(name='Tester')
        Lecture.objects.create(title='Test_lecture',
                               lp=6,
                               semester=2,
                               lecturer_id=1,
                               hall='HS 2',
                               description='Test description')

    def test_title_content(self):
        lecture = Lecture.objects.get(id=1)
        expected_title = f'{lecture.title}'
        self.assertEquals(expected_title, 'Test_lecture')

    def test_lp_content(self):
        lecture = Lecture.objects.get(id=1)
        expected_lp = lecture.lp
        self.assertEquals(expected_lp, 6)

    def test_semester_content(self):
        lecture = Lecture.objects.get(id=1)
        expected_semester = lecture.semester
        self.assertEquals(expected_semester, 2)

    def test_lecturer_content(self):
        lecture = Lecture.objects.get(id=1)
        expected_lecturer = lecture.lecturer.name
        self.assertEquals(expected_lecturer, 'Tester')

    def test_hall_content(self):
        lecture = Lecture.objects.get(id=1)
        expected_hall = lecture.hall
        self.assertEquals(expected_hall, 'HS 2')

    def test_description_content(self):
        lecture = Lecture.objects.get(id=1)
        expected_description = lecture.description
        self.assertEquals(expected_description, 'Test description')
