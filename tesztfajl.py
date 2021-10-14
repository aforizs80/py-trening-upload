numbers= [11, 24, 26, 44]
def calculate_average(numbers):
    if len(numbers) == 0:
        return 0
    result = 0
    for number in numbers:
        result += number
    return result / len(numbers)
