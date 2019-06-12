"""Tests and documents use of Model Classes
"""
import unittest

from app.models.club import Athlete, Relation, \
    Club, Instructor, WeekDay, Activity, Session, SessionSchedule


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

    def test_activity(self):
        self.activity = Activity('gym')
        assert self.activity.name == 'gym'

    def test_session(self):
        self.test_activity()
        self.test_instructor()
        self.session = Session(self.activity, self.instructor)
        assert self.session.instructor == self.instructor
        assert self.session.activity == self.activity

    def test_athlete(self):
        self.athlete = Athlete('Kirk')
        assert self.athlete.name == 'Kirk'

    def test_schedule(self):
        self.test_session()
        self.session.add_schedule(weekday=WeekDay.Monday, hour=17)
        schedules: SessionSchedule = self.session.get_schedules(WeekDay.Monday)
        assert schedules[0].hour == 17
        assert schedules[0].minute == 0
        assert schedules[0].duration == 30

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
        instructor = Instructor('schwaznegger')
        activity = Activity('Jazz')
        session = Session(activity, instructor)
        session.add_schedule(WeekDay.Monday, 21, 30)
        session.add_schedule(WeekDay.Wednesday, 21)
        session.add_schedule(WeekDay.Friday, 21)
        schedules = session.get_schedules()
        assert len(schedules) == 3

    def test_athlete_calendar(self):
        pass

    def test_instructor_sessions(self):
        pass

    def test_instructor_activities(self):
        pass

    def test_activity_instuctors(self):
        pass

    def test_athlete_history(self):
        pass

    def test_activities_close(self):
        # Option to filter activities, show clubs and instructors
       pass
