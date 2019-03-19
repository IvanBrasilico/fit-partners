"""Tests and documents use of Model Classes
"""
import unittest

from app.models.club import Class, ClassSchedule, Club, Instructor, \
    Member, WeekDay


class ClubTestCase(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_club(self):
        self.club = Club('test')
        assert self.club.name == 'test'

    def test_instructor(self):
        self.instructor = Instructor('spock')
        assert self.instructor.name == 'spock'

    def test_class(self):
        self.aclass = Class('gym')
        assert self.aclass.name == 'gym'

    def test_member(self):
        self.member = Member('Kirk')
        assert self.member.name == 'Kirk'

    def test_schedule(self):
        self.test_class()
        self.aclass.add_schedule(day=WeekDay.Monday, hour=17)
        schedules: ClassSchedule = self.aclass.get_schedules(WeekDay.Monday)
        assert schedules[0].hour == 17
        assert schedules[0].minute == 0
        assert schedules[0].duration == 30

    def test_instructor_classes(self):
        self.test_class()
        self.test_instructor()
        self.aclass.add_instructor(self.instructor)
        assert self.instructor in self.aclass.get_instructors()