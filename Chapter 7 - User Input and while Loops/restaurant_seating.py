# Restaurant Seating: Write a program that asks the user how many people
# are in their dinner group. If the answer is more than eight, print a
# message say-ing they’ll have to wait for a table. Otherwise, report
# that their table is ready.

number_of_people = input("How many people are in their dinner group? ")
number_of_people = int(number_of_people)

if number_of_people < 9:
    print("\nYour table is ready")
else:
    print("\nYou will have to wait for a table.")