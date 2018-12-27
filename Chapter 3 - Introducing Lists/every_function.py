# Every Function: Think of something you could store in a list . For example,
# you could make a list of mountains, rivers, countries, cities, languages, or any-
# thing else you’d like . Write a program that creates a list containing these items
# and then uses each function introduced in this chapter at least once .

cities = ['NYC', 'Munich', 'Berlin', 'London']

print('The number of cities in our lists is: ' + str(len(cities)) + '.')

print(cities[-1])

cities.pop()
print(cities[-1])

cities.pop()
print(cities[-1])

cities.pop()
print(cities[-1])