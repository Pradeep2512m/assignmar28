import Areaperi

import pytest

def test_Area_of_Rectangle():
    length = 10
    breadth = 2
    result = Areaperi.Area_of_Rectangle(length,breadth)
    assert result == length*breadth

def test_perimeter_of_rectangle():
    length = 10
    breadth = 20
    result = Areaperi.perimeter_of_rectangle(length,breadth)
    assert result == 2*(length+breadth)

def test_Area_of_Circle():
    radius = 5
    result = Areaperi.Area_of_Circle(radius)
    assert result == 22/7*(radius**2)

def test_Area_of_square():
    sides= 10
    result = Areaperi.Area_of_square(sides)
    assert result == sides**2

def test_Area_of_triangle():
    base =20
    height = 3
    result = Areaperi.Area_of_triangle(base, height)
    assert result == 1/2*(base*height)