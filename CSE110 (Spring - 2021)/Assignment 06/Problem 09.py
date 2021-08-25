import math


def area_circumference_generator(radius):
    circumference = 2 * math.pi * radius
    area = math.pi * radius ** 2
    area_circumference = (area, circumference)
    return area_circumference


area, circumference = area_circumference_generator(2.5)
print(area_circumference_generator(2.5))
print(f"Area of the circle is {area} and circumference is {circumference}")
