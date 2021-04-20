# Calculate Area and Perimeter after radius input from user

import math


def calculations(radius):
    perimeter = 2 * math.pi * radius
    area = math.pi * radius ** 2        # OR area = math.pi * pow(radius,2)
    return (perimeter, area)            # tuple


rad = float(input('Give me a radius: '))
calcTuple = calculations(rad)
print(f' The perimeter is approximately {calcTuple[0]:.2f}')
print(f' The area is approximately {calcTuple[1]:.2f}')
