states = {
    'Oregon' : 'OR',
    'Florida' : 'FL',
    'California' : 'CA',
    'New York': 'NY',
    'Michigan' : 'MI'
}

cities = {
    'CA' : 'San Francisco',
    'MI' : 'Detroit',
    'FL' : 'Jacksonville'
}

#Add new element to dict
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

print('-'*10)
print("NY State has: ",cities['NY'])
print("OR State has: ",cities['OR'])

print('-'*10)
print("Michigan has: ",cities[states['Michigan']])
print("Florida has: ",cities[states['Florida']])

print('-'*10)
for state,abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev}")

print('-'*10)
for abbrev,city in list(cities.items()):
    print(f"{abbrev} has city {city}")

print('-'*10)
for state,abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev}")
    print(f"and has city {cities[abbrev]}")

print('-'*10)
#Get will returns a value for the given key. If key is not available then returns default value None.
state = states.get('Texas')
if not state:
    print("Sorry there's no Texas")

#Get will return 'Does Not Exist' if 'TX' is not available.
city = cities.get('TX','Does Not Exist')
print(f"The city for the state 'TX' is {city}")