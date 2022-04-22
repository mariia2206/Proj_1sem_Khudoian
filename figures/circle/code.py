import math
default_radius = 5
__all__ = ['circle_perimetr', 'circle_area']


def circle_perimetr(radius=default_radius):
    return 2 * math.pi * radius


def circle_area(radius=default_radius):
    return math.pi * radius ** 2