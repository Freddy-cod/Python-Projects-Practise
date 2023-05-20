
def sum_10(isbn):
    '''Multiply each digit with the of the ISBN number and
    sum up the the products'''
    products = []
    for index_, isbn_num in enumerate(isbn[::-1], 1):
        if isbn_num == "X":
            products.append(index_ * 10)
        else:
            products.append(index_ * int(isbn_num))
    return sum(products)


def sum_13(isbn):
    '''Aggregates the ISBN number with alternating
    ones and threes (1313131313131), multiply them and
    sum their products'''
    products = []
    for isbn_num, one_threes in zip(isbn, '1313131313131'):
        products.append(int(isbn_num) * int(one_threes))
    return sum(products)


def isbn13(numbers):
    '''Verify ISBN'''
    if len(numbers) == 13:
        if sum_13(numbers) % 10 == 0 :
            return 'Valid'
        else:
            return 'Invalid'
    elif sum_10(numbers) % 11 == 0:
        # Convert a valid ISBN-10 to ISBN-13 by tacking 978
        # and change last digit
        check = sum_13('978' + numbers[:-1]) % 10
        return '978' + numbers[:-1] + str(10 - check)
    return 'Invalid'


# Tests 

print(isbn13("9780316066525"))
print(isbn13("0330301824"))
print(isbn13("0316066524"))