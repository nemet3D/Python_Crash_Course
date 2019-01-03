# Addition: One common problem when prompting for numerical input occurs
# when people provide text instead of numbers. When you try to convert
# the input to an int , you’ll get a TypeError. Write a program that
# prompts for two numbers. Add them together and print the result. Catch
# the TypeError if either input value is not a number, and print a
# friendly error message. Test your program by entering two numbers and
# then by entering some text instead of a number.

print("Give me two numbers, and I'll add them.")

while True:
    first_number = input("\nFirst number: ")

    try:
        first_number = int(first_number)
        print(first_number)
    except TypeError:
        print("Please input a number.")

    second_number = input("\nSecond number: ")
    try:
        second_number = int(second_number)
        print(second_number)
    except ValueError:
        print("Please input a number.")

    try:
        answer = first_number + second_number
        print(answer)
    except TypeError:
        print("Try again.")