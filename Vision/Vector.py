#!/usr/bin/env python
__name__ = "Vector"
import copy

class Vector(object):

    def __init__(self, x, y, z = 0):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)

    def __repr__(self):
        stringy = '<%s, %s, %s>' % (self.x, self.y, self.z)
        return stringy

    def __add__(self, other):
        a = self.x + other.x
        b= self.y + other.y
        c = self.z + other.z
        return Vector(a, b, c)

    def __sub__(self, other):
        a = self.x - other.x
        b= self.y - other.y
        c = self.z - other.z
        return Vector(a, b, c)

    def __mul__(self, scalar):
        a = self.x * scalar
        b = self.y * scalar
        c = self.z * scalar
        return Vector(a, b, c)

    def __rmul__(self, scalar):
        a = self.x * scalar
        b = self.y * scalar
        c = self.z * scalar
        return Vector(a, b, c)

    def __div__(self, scalar):
        a = self.x / scalar
        b = self.y / scalar
        c = self.z / scalar
        return Vector(a, b, c)

    def __rdiv__(self, scalar):
        a = self.x / scalar
        b = self.y / scalar
        c = self.z / scalar
        return Vector(a, b, c)
    
    def mag(self, squared = True):
        magnitude = self.x **2 + self.y ** 2 + self.z ** 2
        if not squared:
            magnitude = magnitude ** .5
        return magnitude

    def normalize(self):
        vec = copy.copy(self)
        return vec /  vec.mag(False)

    def cross(self, other):
        a =self.y * other.z - self.z * other.y
        b =self.z * other.x - self.x * other.z
        c =self.x * other.y - self.y * other.x
        return Vector(a, b, c)
    
    def dot(self, other):
        a = self.x * other.x
        b = self.y * other.y
        c = self.z * other.z
        return a + b + c

    def triple_scalar(self, otherV, otherW):
        return self.dot(otherV.cross(otherW))
    
a = Vector(1, 2, 3)
b = Vector(2, -7, 8)
c = Vector(5, 8, -1)
