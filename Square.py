#! /usr/bin/env python

from lab_python_oop.Rectangle import Rectangles


class Squares(Rectangles):
    def __init__(self, width, color, name="Square"):
        self.width = width
        self.name = name
        self.color = color

    def area(self):
        return self.width ** 2

    def __repr__(self):
        return '{} -> Weight: {}, Color: {}, Area: {}'.format(self.name, self.width, self.color, self.area())
