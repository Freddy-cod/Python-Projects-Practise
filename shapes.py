from math import pi # Import math

class Sphere:
    '''Makes a sphere by initializing its radius'''
    def __init__(self, radius):
        self.radius = radius

    def get_radius(self):
        '''Returns radius of the sphere'''
        return self.radius

    def surfaceArea(self):
        '''Computes the surface area of the sphere'''
        return 4 * pi * self.radius ** 2

    def volume(self):
        '''Computes the volume of the sphere'''
        return 4 * pi * self.radius ** 3 / 3


class Cube:
    '''Makes a cube after initializing its length'''
    def __init__(self, length):
        self.length = length

    def getLength(self):
        '''Return the length of a cube'''
        return self.length

    def area(self):
        '''Returns the area of a cube'''
        return 6 * self.length ** 2

    def volume(self):
        '''Returns the volume of a cube'''
        return self.length ** 3
