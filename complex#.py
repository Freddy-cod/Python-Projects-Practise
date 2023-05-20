class MyComplex(Vector):
    '''This a subclass inheriting from Vector class .This class accepts
    a real number in form of "x' and an imaginary number or imaginary part
    in form of "y" .'''

    def __init__(self, x, y):
        '''X and Y are instance variable or properties of an object self .'''
        self.x = x
        self.y = y

    def __mul__(self, other):
        '''Multiplication of complex numbers '''
        return MyComplex(self.x * other.x - self.y * other.y,
                         self.x * other.x + self.y * other.y)

    def __str__(self):
        '''This returns a readable string when the object is printed .'''
        if self.y >= 0:
            return f'{self.x} + {self.y}i'
        return f'{self.x} - {self.y}i'

    def conjugate(self):
        '''This method reverses the operator sign to make it a conjugate . Two signs
        are applicable , addition and subtration . '''
        return MyComplex(self.x, -self.y)


# An instance of MyComplex when printed returns a complex number
print("COMPLEX NUMBERS EXAMPLES")
comp_num = MyComplex(2, 3)
print(comp_num)
comp_num2 = MyComplex(3, 2)

# Addition of x values and y values of the instances
# The add method is inherited from the super class Vector
added = comp_num + comp_num2
print(added.x, added.y)

# The added values are turned into an imaginary number .
added_complex = MyComplex(added.x, added.y)
print(added_complex)
