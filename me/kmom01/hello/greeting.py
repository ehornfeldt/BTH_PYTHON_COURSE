#!/usr/bin/env python3

"""
Programmet skriver ut en hälsning till Jack Black
"""

#Hardcoded, this year
year = 2023

name = input("Skriv in ditt namn, tryck sedan enter: ")
age= input("Hur gammal är du? ")

year_born = year - int(age)

greeting = "Hej " + name + ", du är " + str(age) + " år gammal och är född " + str(year_born)

print(greeting) # Skriver ut ett sträng värde 