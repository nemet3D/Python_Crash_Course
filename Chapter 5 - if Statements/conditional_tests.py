# Conditional Tests: Write a series of conditional tests . Print a
# statement describing each test and your prediction for the results of
# each test . Your code should look something like this:
# car = 'subaru'
# print("Is car == 'subaru'? I predict True.")
# print(car == 'subaru')
# print("\nIs car == 'audi'? I predict False.")
# print(car == 'audi')
# • Look closely at your results, and make sure you understand why each
# line evaluates to True or False .
# • Create at least 10 tests . Have at least 5 tests evaluate to True and
# another 5 tests evaluate to False .

car = 'Subaru'
print("\nIs the car == 'subaru'? I predict True.")
print(car.lower() == 'subaru')
print("Is the car == 'audi'? I predict False.")
print(car == 'audi')

pizza = 'diavola'
print("\nIs the pizza == 'diavola'? I predict True.")
print(pizza == 'diavola')
print("Is car == 'salami'? I predict False.")
print(pizza == 'salami')

team = '1860'
print("\nIs the team == '1860'? I predict True.")
print(team == '1860')
print("Is the team == 'FC Bayern'? I predict False.")
print(team == 'FC Bayern')

season = 'winter'
print("\nIs the season == 'winter'? I predict True.")
print(season == 'winter')
print("Is the season == 'summer'? I predict False.")
print(season == 'summer')

year = 2018
print("\nIs the year == 2018? I predict True.")
print(year == '2018')
print("Is the year == 2019? I predict False.")
print(year == 2019)