#  You can experiment here, it won’t be checked
'''
class City:
    all_cities = []

    def __init__(self, name, year):
        self.name = name
        self.year = year

ny = City("New York", 1624)
ny.all_cities.append("New York")

stockholm = City("Stockholm", 1187)
stockholm.all_cities = ["Stockholm"]

print(City.all_cities)
'''

import os
# print(os.getcwd())
print(os.path.isdir(os.getcwd()))

