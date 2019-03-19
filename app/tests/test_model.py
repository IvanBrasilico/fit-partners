"""Tests and documents use of Model Classes
"""
import unittest

from app.models.club import Class, Club, Instructor, Member


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
        aclass = Class('gym')
        assert self.aclass.name == 'gym'

    def test_member(self):
        member = Member('Kirk')
        assert self.member.name == 'Kirk'
