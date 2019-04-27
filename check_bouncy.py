
def check_bouncy(number):
    number = str(number)
    increasing = True
    decreasing = True

    for index, digit in enumerate(number):
        if not (increasing or decreasing):
            return True
        if index + 1 == len(number):
            return not (increasing or decreasing)
        else:
            if digit < number[index + 1]:
                increasing = False
            if digit > number[index + 1]:
                decreasing = False


def bouncy_number(target):
    number = 0
    result = 0
    while number <= target:
        if check_bouncy(number):
            result += 1
        number += 1
    return result


def challenge():
    number = 1
    results = 0
    while True:
        if check_bouncy(number):
            results += 1
        if results / number >= 0.99:
            return number
        print(number, results, results/number*100)
        number += 1

print(challenge())



