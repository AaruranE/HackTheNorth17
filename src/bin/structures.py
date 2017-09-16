from enum import Enum
import inspect


class Team(Enum):
    A = 1
    B = 1


class Zone:

    def __init__(self, x, y, radius):
        if x is None or y is None or radius is None:
            raise ValueError("All zone parameters must be numeric")
        if radius <= 0:
            raise ValueError("Radius must be positive.")
        self.x = x
        self.y = y
        self.radius = radius

    def contains(self, other_zone):
        distance_squared = (self.x - other_zone.x)**2 + (self.y - other_zone.y)**2
        return distance_squared <= self.radius **2


class Thing:

    def __init__(self, team, zone, moving):
        self.x = zone.x
        self.y = zone.y
        self.zone = zone
        self.team = team
        self.moving = moving

    def x(self):
        return self.x

    def y(self):
        return self.y

    def within(self, thing2):
        return self.zone.contains(thing2.zone)

class Flag(Thing):
    def __init__(self, team, zone):
        self.team = team
        self.x = zone.x
        self.y = zone.y
        self.moving = False

    


class Person(Thing):
    def __init__(self, team, zone):
        self.health = 3
        self.team = Team

    def within(self, thing):
        if not inspect.isinstance(thing, Person):
            pass
        elif self.team == thing.team:
            pass
        elif self.flag.isCaptured()









