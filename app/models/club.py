from collections import defaultdict
from typing import List, Type


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

    def is_close(self, other, radius: float):
        return abs(other.lat - self.lat) <= radius and \
               abs(other.long - self.long) <= radius

    def manhatan_distance(self, other):
        return abs(other.lat - self.lat) + abs(other.long - self.long)

    def get_closest(self, geolocs: list, max_radius: float):
        distances = []
        closest = []
        for geoloc in geolocs:
            distance = self.manhatan_distance(geoloc)
            if distance < max_radius:
                distances.append(distance)
                closest.append(geoloc)
        #TODO: Order by distance
        return closest, distances

class ClassSchedule:
    def __init__(self, class_id,
                 day: WeekDay, hour: int,
                 minute: int = 0, duration: int = 30):
        self.class_id = class_id
        self.day = day
        self.hour = hour
        self.minute = minute
        self.duration = duration


class Class:
    def __init__(self, name: str):
        self.name = name
        self.schedules = defaultdict(list)
        self.instructors = []

    def add_class_schedule(self, day: WeekDay,
                           class_schedule: ClassSchedule):
        self.schedules[day].append(class_schedule)

    def add_schedule(self, day: WeekDay, hour: int,
                     minute: int = 0, duration: int = 30):
        self.add_class_schedule(day, ClassSchedule(self, day, hour, minute, duration))

    def get_schedules(self, weekday):
        return self.schedules[weekday]

    def add_instructor(self, instructor):
        self.instructors.append(instructor)

    def get_instructors(self):
        return self.instructors


class Club(GeoLoc):
    def __init__(self, name: str):
        self.name = name


class Instructor(GeoLoc):
    def __init__(self, name: str):
        self.name = name


class Athlete(GeoLoc):
    def __init__(self, name: str):
        self.name = name
