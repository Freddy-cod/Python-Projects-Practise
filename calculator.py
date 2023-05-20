import math


class Calculator:

    ''' A calculator that performs basic arithmetic given input values with an
    arithmetic operator as its first index .Computes factorials ,highest prime
    number given a value and fibonacci number . Inputs and
    are of type strings '''

    def add(self, values):
        ''' Performs addition given at least two values and an addition
        sign as its first value . Receives string and oupts strings .'''

        # Loop through values , change them into floats then add
        answer = sum([float(num) for num in values[1:].split()])
        return str(math.trunc(answer))

    def diff(self, values):
        ''' Performs subtration given at least two values and an subtraction
        sign as its first value . Receives string and oupts strings .'''

        # Loop through values , change them into floats and subtract
        numbers = [float(num) for num in values[1:].split()]
        answer = numbers[0] - sum(numbers[1:])

        return str(math.trunc(answer))

    def div(self, values):
        ''' Performs division given  two values and an division
        sign as its first value . Receives string and oupts strings .'''

        # Loop through values , change them into floats and divide
        numbers = [float(num) for num in values[1:].split()]
        answer = numbers[0]/numbers[1]
        return str(math.trunc(answer))

    def mult(self, values):
        ''' Performs multiplication given at least two values and an
        subtraction sign as its first value . Receives string and oupts
        strings .'''

        # Loops through values , change them into floats and multiply
        numbers = [float(num) for num in values[1:].split()]

        # Initiaze by 1 then loop through numbers while multiplying
        answer = 1
        for i in numbers:
            answer = i * answer
        return str(math.trunc(answer))

    def prime(self, values):
        """ Return highest prime number under a give value"""

        # Initialize
        prime = []
        # Take values after index 1 and store them in num
        num = values.split()[1:]
        num = int("".join(num))  # Change list to strings

        # Loop through numbers ,append in a list .
        for num in range(num):
            if num > 1:
                for i in range(2, num):
                    if (num % i) == 0:
                        break
                else:
                    prime.append(num)
        return str(max(prime))  # Return the highest prime

    def factorial(self, value):
        """ Return the factorial of a number ."""

        # Initialize , take all numbers after index 1
        fact = 1
        num = value.split()[1:]
        # Change list into a string
        num = int("".join(num)) + 1

        # Loop through numbers and return a factorial
        for i in range(1, num):
            fact = fact * i
        return str(fact)

    def fib(self, values):
        '''Return a highest fibonacci number under a given value'''

        # Store the first two values in first and second
        first = 0
        second = 1
        fib_values = []

        # Take numbers after index 1
        num = values.split()[1:]

        # Change list into a string
        num = int("".join(num))

        # Loop while adding two previous values to find fib
        for i in range(num):
            fib_values.append(first)
            temp = first
            first = second
            second = temp + second

        # Return highes fib number in a list
        return max([n for n in fib_values if n < num])

    def rvalue(self, value):
        '''Return the value given'''
        return value

    def rwhite_space(self, values):
        '''Removes tabs or whitespaces in values'''
        return values.strip()


def main():

    # Continue asking for input till user press enter
    user_input = input("Input(Enter to quit) :: ")
    while user_input != "":

        # Create a calculator object
        calc = Calculator()

        # If user input has + ,add values
        if user_input.split()[0] == "+":
            answer = calc.add(user_input)
            print(answer)

        # If user input has - ,subtract values
        elif user_input.split()[0] == "-":
            answer = calc.diff(user_input)
            print(answer)

        # If user input has / , divide values
        elif user_input.split()[0] == "/":
            answer = calc.div(user_input)
            print(answer)

        # If user input has * ,add multiply
        elif user_input.split()[0] == "*":
            answer = calc.mult(user_input)
            print(answer)

        # If user input has prime , find highest prime
        elif user_input.split()[0] == "prime":
            answer = calc.prime(user_input)
            print(answer)

        # If user input has factorial ,find factorial
        elif user_input.split()[0] == "factorial":
            answer = calc.factorial(user_input)
            print(answer)

        #  If user input has \t ,strip whitespaces
        elif user_input.split()[0] == "\t":
            answer = calc.rwhite_space(user_input)
            print(answer)
        # If user input has fibonnacci ,find fibonacci
        elif user_input.split()[0] == "fibonacci":
            answer = calc.fib(user_input)
            print(answer)

        else:
            # else just return the value
            answer = calc.rvalue(user_input)
            print(answer)

        user_input = input("Input(Press Enter to quit):: ")


main()
