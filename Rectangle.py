#! /usr/bin/env python

from lab_python_oop.Geom_figures import GeometricFigures


class Rectangles(GeometricFigures):
    def __init__(self, width, height, color, name="Rectangle"):
        self.color = color
        self.width = width
        self.height = height
        self.name = name


    def area(self):
        return self.height * self.width

    def __repr__(self):
        return '{} -> Weight: {}, Height: {}, Colour: {}, Area: {}'.format(self.name, self.width, self.height,
                                                                            self.color, self.area())
