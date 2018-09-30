#! /usr/bin/env python
# -*- coding:utf-8 -*-


from lab_python_oop.Geom_figures import GeometricFigures
from math import pi


class Circles(GeometricFigures):
    def __init__(self, radius, color, name="Circle"):
        self.color = color
        self.radius = radius
        self.name = name


    def area(self):
        return pi*self.radius**2

    def __repr__(self):
        return '{} -> Radius: {}, Color: {}, Area: {}'.format(self.name, self.color, self.radius,  self.area())


