import math


class Vector():
    '''This is a two dimensional Vector class initialised by x and y
    data types . It performs addition , subtraction ,scalar multiplication
    computes length and comparison between two values . All methods excepts
    length() make use of operator overloading .'''

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __add__(self, other):
        ''' Adds two vectors together , but first checks
        if the other vector is of the same type with our class
        else we add other vector to x and y of self '''

        if isinstance(other, self.__class__):
            return Vector(self.x + other.x, self.y + other.y)
        return Vector(self.x + other, self.y + other)

    def __sub__(self, other):
        ''' Subtracts two vectors , but first checks
        if the other vector is of the same type with our class
        else we subtract other vector from x and y of self '''

        if isinstance(other, self.__class__):
            return Vector(self.x - other.x, self.y - other.y)
        return Vector(self.x - other, self.y - other)

    def __mul__(self, other):
        ''' Adds two vectors together , but first checks
        if the other vector is of the same type with our class
        else we add other vector to x and y of self '''

        if isinstance(other, self.__class__):
            return Vector(self.x * other.x, self.y * other.y)
        return Vector(self.x * other, self.y * other)

    def __rmul__(self, other):
        '''Reflected multiplication so vector * other also works.'''
        return self.__mul__(other)

    def length(self):
        ''' Computes the lenght of a vector using pythagoras theorem '''
        return math.sqrt(self.x**2 + self.y**2)

    def __cmp__(self, other):
        ''' Compares the x and y values of vectors, returns true if same else
        returns false .'''
        if self.x == other.x and self.y == other.y:
            return True
        return False


print('VECTORS EXAMPLES')
vector1 = Vector(10, 15)
vector2 = Vector(5, 5)
v = vector1 + vector2
print(v.x, v.y)  # Example to perform methods on the objects made from Vector