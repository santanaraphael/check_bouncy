
def check_bouncy(number):
    number = str(number)
    increasing = 0
    decreasing = 0

    for index, digit in enumerate(number):
        if index + 1 == len(number):
            return not (increasing == len(number) - 1 or decreasing == len(number) - 1)
        else:
            if digit >= number[index + 1]:
                increasing += 1
            if digit <= number[index + 1]:
                decreasing += 1


def bouncy_number(target):
    return None


def challenge():
    return None
