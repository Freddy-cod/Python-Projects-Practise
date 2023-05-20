
# Store ones , tens and hundrends
ones = {
    0: '', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six',
    7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve',
    13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen',
    17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}
tens = {
    2: 'twenty', 3: 'thirty', 4: 'forty', 5: 'fifty', 6: 'sixty',
    7: 'seventy', 8: 'eighty', 9: 'ninety'}
illions = {
    1: 'thousand', 2: 'million', 3: 'billion', 4: 'trillion', 5: 'quadrillion',
    6: 'quintillion', 7: 'sextillion', 8: 'septillion', 9: 'octillion',
    10: 'nonillion', 11: 'decillion'}


def say_number(number):
    """
    Convert an integer in to it's word representation.

    say_number(number: integer) -> string
    """
    if number < 0:
        return _join('negative', say_the_number(-number))
    if number == 0:
        return 'zero'
    return say_the_number(number)


def say_the_number(number):
    '''Convert an integer in to it's word representation'''
    if number < 20:
        return ones[number]
    if number < 100: 
        return _join(tens[number // 10], ones[number % 10])
    if number < 1000:
        return _divide(number, 100, 'hundred')
    for illions_number, illions_name in illions.items():
        if number < 1000**(illions_number + 1):
            break
    return _divide(number, 1000**illions_number, illions_name)


def _divide(dividend, divisor, magnitude):
    '''Perform division for hundrends and illions'''
    return _join(
        say_the_number(dividend // divisor),
        magnitude,
        say_the_number(dividend % divisor),
    )


def _join(*args):
    '''Join values'''
    return ' '.join(filter(bool, args))


# References
#Test 
print(say_number(889988))


