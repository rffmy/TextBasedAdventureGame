#  You can experiment here, it won’t be checked

planets = {'Venus', 'Earth', 'Jupiter'}

# initializing by default with None
planets_dict = dict.fromkeys(planets)
print(planets_dict)  # {'Jupiter': None, 'Venus': None, 'Earth': None}

# initializing with a value
value = 'planet'
planets_dict = dict.fromkeys(planets, value)
print(planets_dict)  # {'Earth': 'planet', 'Venus': 'planet', 'Jupiter': 'planet'}

# changing the value of 'Jupiter'
planets_dict['Jupiter'] = "giant " + planets_dict['Jupiter']
print(planets_dict)
 # {'Earth': 'planet', 'Venus': 'planet', 'Jupiter': 'giant planet'}
