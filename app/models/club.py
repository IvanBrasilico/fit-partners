from collections import defaultdict
from datetime import date, datetime


class WeekDay:
    Monday = 0
    Tuesday = 1
    Wednesday = 2
    Thursday = 3
    Friday = 4
    Saturday = 5
    Sunday = 6


class GeoLoc():
    def __init__(self):
        self.lat: float = None
        self.long: float = None

    def setLatLong(self, lat, long):
        self.lat = lat
        self.long = long

    def is_close(self, other, max_radius: float, method='manhatan'):
        if method == 'manhatan':
            distance = self.manhatan_distance(other)
        else:
            distance = self.euclidean_distance(other)
        return distance <= max_radius

    def is_insquare(self, other, max_radius: float):
        return abs(other.lat - self.lat) <= max_radius and \
               abs(other.long - self.long) <= max_radius

    def manhatan_distance(self, other):
        return abs(other.lat - self.lat) + abs(other.long - self.long)

    def euclidean_distance(self, other):
        return abs(other.lat - self.lat) + abs(other.long - self.long)

    def get_closest(self, geolocs: list, max_radius: float):
        closest = []
        for geoloc in geolocs:
            distance = self.manhatan_distance(geoloc)
            print(geoloc, distance)
            if distance < max_radius:
                closest.append((distance, geoloc))
        closest.sort()
        distances = [item[0] for item in closest]
        closest = [item[1] for item in closest]
        return closest, distances


class Club(GeoLoc):
    def __init__(self, name: str):
        self.name = name

    def add_activity(self, activity):
        raise NotImplementedError()

    def add_instructor(self, instructor):
        raise NotImplementedError()

    def add_manager(self, person):
        raise NotImplementedError()

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class Person(GeoLoc):
    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class Instructor(Person):
    def __init__(self, name: str):
        super().__init__(name)


class Athlete(Person):
    def __init__(self, name: str):
        super().__init__(name)


class Activity:
    def __init__(self, name):
        self.name = name


class SessionSchedule:
    def __init__(self, session,
                 weekday: WeekDay, hour: int,
                 minute: int = 0, duration: int = 30):
        self.session = session
        self.weekday = weekday
        self.hour = hour
        self.minute = minute
        self.duration = duration


class Presence:
    def __init__(self, athlete: Athlete,
                 schedule: SessionSchedule,
                 when: datetime):
        self.athlete = athlete
        self.schedule = SessionSchedule
        self.when = when


class Session:
    def __init__(self,
                 activity: Activity,
                 instructor: Instructor):
        self.schedules = defaultdict(list)
        self.presences = []
        self.activity = activity
        self.instructor = instructor

    def _add_session_schedule(self, schedule: SessionSchedule):
        self.schedules[schedule.weekday].append(schedule)

    def add_schedule(self, weekday: WeekDay, hour: int,
                     minute: int = 0, duration: int = 30):
        self._add_session_schedule(
            SessionSchedule(self, weekday, hour, minute, duration)
        )

    def get_schedules(self, weekday: WeekDay = None):
        if weekday is not None:
            return self.schedules[weekday]
        return [schedule for schedule in self.schedules.values()]

    def get_today_schedule(self, date: date):
        nweekday = date.dayOfW

    def register_presence(self, athlete, schedule, when):
        self.presences.append(Presence(athlete, schedule, when))


class Relation:
    relations = []

    @classmethod
    def add(cls, elem0, elem1):
        cls.relations.append([elem0, elem1, True])

    @classmethod
    def get(cls, element, key=0):
        if key == 0:
            value = 1
        else:
            value = 0
        return [relation[value] for relation in cls.relations
                if relation[key] == element and relation[2] is True]

    @classmethod
    def active(cls, elem0, elem1):
        for relation in cls.relations:
            if relation[0] == elem0 and \
                    relation[1] == elem1:
                return relation[2]
        return False

    @classmethod
    def remove(cls, elem0, elem1):
        for relation in cls.relations:
            if relation[0] == elem0 and \
                    relation[1] == elem1:
                relation[2] = False
                return True
        return False
