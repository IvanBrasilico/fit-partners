"""Tests and documents use of Model Classes
"""
import unittest

from app.models.club import Athlete, Relation, Class, ClassSchedule, \
    Club, Instructor, WeekDay


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

    def test_athlete(self):
        self.athlete = Athlete('Kirk')
        assert self.athlete.name == 'Kirk'

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

    def test_club_is_close(self):
        radius = 1.5
        self.test_club()
        self.test_athlete()
        self.club.setLatLong(1., 1.)
        assert self.club.lat == 1.
        assert self.club.long == 1.
        self.athlete.setLatLong(1.5, 2.)
        assert self.athlete.is_close(self.club, radius) is True
        self.athlete.setLatLong(2.5, 2.)
        assert self.athlete.is_close(self.club, radius) is False
        self.athlete.setLatLong(1., 1.)
        assert self.athlete.is_close(self.club, radius) is True
        self.athlete.setLatLong(1., 3.)
        assert self.athlete.is_close(self.club, radius) is False

    def test_club_is_insquare(self):
        radius = 1.
        self.test_club()
        self.test_athlete()
        self.club.setLatLong(1., 1.)
        assert self.club.lat == 1.
        assert self.club.long == 1.
        self.athlete.setLatLong(1.5, 2.)
        assert self.athlete.is_insquare(self.club, radius) is True
        self.athlete.setLatLong(2.5, 2.)
        assert self.athlete.is_insquare(self.club, radius) is False
        self.athlete.setLatLong(1., 1.)
        assert self.athlete.is_insquare(self.club, radius) is True
        self.athlete.setLatLong(1., 3.)
        assert self.athlete.is_insquare(self.club, radius) is False

    def test_closest_clubs(self):
        clubs = []
        clubs.append(Club('closer.5'))
        clubs.append(Club('closer1.6'))
        clubs.append(Club('farfaraway3'))
        clubs.append(Club('closer1'))
        clubs.append(Club('closer1.5'))
        lats = [1., 1.6, 3., 1., 2.5]
        longs = [1.5, 2., 2., 2., 1]
        for club, lat, long in zip(clubs, lats, longs):
            club.setLatLong(lat, long)
        athlete = Athlete('lost')
        athlete.setLatLong(1., 1.)
        closest_clubs, distances = athlete.get_closest(clubs, max_radius=2.)
        print(closest_clubs, distances)
        assert len(closest_clubs) == len(clubs) - 1
        previous_distance = 0
        for ind in range(len(closest_clubs)):
            assert distances[ind] >= previous_distance
            previous_distance = distances[ind]
        assert closest_clubs[0] == clubs[0]
        assert closest_clubs[1] == clubs[3]
        assert closest_clubs[2] == clubs[4]
        assert closest_clubs[3] == clubs[1]

    def test_instructor_athletes(self):
        instructor = Instructor('Ulisses')
        instructor2 = Instructor('Menelau')
        athlete1 = Athlete('Aquiles')
        athlete2 = Athlete('Ajax')
        Relation.add(instructor, athlete1)
        Relation.add(instructor, athlete2)
        Relation.add(instructor2, athlete2)
        assert Relation.active(instructor, athlete1) is True
        assert Relation.active(instructor, athlete2) is True
        athletes = Relation.get(instructor, key=0)
        assert len(athletes) == 2
        instructors = Relation.get(athlete1, key=1)
        assert len(instructors) == 1
        instructors = Relation.get(athlete2, key=1)
        assert len(instructors) == 2
        assert Relation.remove(instructor, athlete1) is True
        assert Relation.active(instructor, athlete1) is False
        athletes = Relation.get(instructor, key=0)
        assert len(athletes) == 1

    def test_instructor_calendar(self):
        pass

    def test_athlete_calendar(self):
        pass
