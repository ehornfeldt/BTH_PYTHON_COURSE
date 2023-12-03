#!/usr/bin/env python3

"""
Convert Swedish flight data to US standard
"""

#Ask user for height and convert to feet
height = input('Ange höjd i meter: ')
height = round(float(height) * 3.28084, 2)

print(height)

#Ask user for speed and convert to mph
speed = input('Ange hasighet i km/h: ')
speed = round(float(speed) * 0.62137 , 2)

print(speed)

#Ask user for temperature and convert to F
temp = input('Ange tempereturen i grader: ')
temp = round(float(temp) * 9 / 5 + 32, 2)

print(temp)
