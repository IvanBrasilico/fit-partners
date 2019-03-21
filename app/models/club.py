from collections import defaultdict


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


class ClassSchedule:
    def __init__(self, aclass, instructor,
                 weekday: WeekDay, hour: int,
                 minute: int = 0, duration: int = 30):
        self.aclass= aclass
        self.instructor = instructor
        self.weekday = weekday
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


class Person(GeoLoc):
    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class Club(GeoLoc):
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
