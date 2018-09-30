#! /usr/bin/env python

from lab_python_oop.Rectangle import Rectangles
from lab_python_oop.Square import Squares
from lab_python_oop.Circle import Circles

rec = Rectangles(3, 2, "blue")
print(rec.__repr__())
circle = Circles(5, "green")
print(circle.__repr__())
sq = Squares(5, "red")
print(sq.__repr__())
