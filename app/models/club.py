from collections import defaultdict


class WeekDay:
    Monday = 0
    Tuesday = 1
    Wednesday = 2
    Thursday = 3
    Friday = 4
    Saturday = 5
    Sunday = 6


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


class Club:
    def __init__(self, name: str):
        self.name = name


class Instructor:
    def __init__(self, name: str):
        self.name = name


class Member:
    def __init__(self, name: str):
        self.name = name
