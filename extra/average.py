def calculate_average(*numbers):
    total = 0
    elements_number = 0
    for number in numbers:
        total += number
        elements_number += 1

    return total / elements_number


print(calculate_average(1, 2, 3, 4, 5, 6, 7, 8))
print(calculate_average(10, 20, 30))