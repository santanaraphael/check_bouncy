import sys


def check_bouncy(number):
    """
    Checks if the number is bouncy.
    :param number: Integer number which needs to be checked if its bouncy or not;
    :return: True if the number is bouncy or False if its not.
    """

    number = str(number)  # We need to work with numbers as strings, to check each individual digit.

    if not number.isdigit():
        raise TypeError('The number argument must be an integer type.')

    increasing = True     # We first assume the number is both increasing and decreasing
    decreasing = True

    for index, digit in enumerate(number):
        if not (increasing or decreasing):  # It means it is bouncy!
            return True
        if index + 1 == len(number):        # We've reached the end of the number, so we just use the last state
            return not (increasing or decreasing)
        else:
            if digit < number[index + 1]:   # When something proves us otherwise, we change the respective
                increasing = False          # field to False
            if digit > number[index + 1]:
                decreasing = False


def bouncy_number(target):
    """
    Returns the amount of bouncy numbers from 0 up to the target number
    :param target: Integer target number;
    :return: The amount of bouncy numbers in that range.
    """

    if not str(target).isdigit():
        raise TypeError('The number argument must be an integer type.')

    number = 0  # We start on the number zero, just for simplicity, but in fact, we could start at the first
    result = 0  # bouncy number, which is 101.
    while number <= target:
        if check_bouncy(number):
            result += 1
        number += 1
    return result


def challenge(ratio=0.99):
    """
    It returns the least number for which the proportion of bouncy numbers is exactly a ratio.
    :param ratio: The ratio in its decimal form (e.g. 99% = 0.99)
    :return: The least number which satisfies the condition.
    """

    if float(ratio) >= 1:
        raise ValueError('The final ratio must be a decimal ratio smaller than 1.')
    number = 1   # We use 1 as the starting point there to avoid a division by zero in the algorithm,
    results = 0  # we could choose any number less or equal than 101, but we choose 1 for the beauty of code.
    while True:
        if check_bouncy(number):
            results += 1

        print('Up to the number {} there are {} bouncy numbers, the ratio is {}%.'
              .format(number, results, results/number*100))

        if results / number == float(ratio):
            return number
        number += 1

if __name__ == '__main__':
    if len(sys.argv) == 2:
        challenge(ratio=sys.argv[1])
    else:
        challenge()
