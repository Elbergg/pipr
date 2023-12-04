from planets import Planet
import pytest
import math


def test_create_planet():
    planet = Planet(1, 1, 1, "Earth")
    assert planet.name() == 'Earth'


def test_location():
    planet = Planet(1, 1, 1, "Earth")
    assert planet.x() == 1
    assert planet.y() == 1
    assert planet.z() == 1

def test_print_planet():
    planet = Planet(1, 1, 1, "Earth")
    assert str(planet) == "Planet Earth has coordinates 1, 1, 1"


def test_distance():
    planet1 = Planet(0, 0, 0, "Earth")
    planet2 = Planet(1, 1, 1, "Mars")
    assert planet1.distance(planet2) == math.sqrt(3)


def test_distance_negative_coords():
    planet1 = Planet(0, 0, 0, "Earth")
    planet2 = Planet(-1, -1, -1, "Mars")
    assert planet1.distance(planet2) == math.sqrt(3)
    

