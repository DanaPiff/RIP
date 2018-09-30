#! /usr/bin/env python
# -*- coding:utf-8 -*-
from abc import ABCMeta, abstractmethod


class GeometricFigures(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def area(self):
        pass
