# Guest: Write a program that prompts the user for their name. When they
# respond, write their name to a file called guest.txt.

guest_input = input("Enter your name please: ")

filename = "guest_name.txt"

with open(filename, 'a') as file_object:
    file_object.write(guest_input.title() + "\n")