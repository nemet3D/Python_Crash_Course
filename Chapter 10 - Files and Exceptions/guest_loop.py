# Guest Book: Write a while loop that prompts users for their name. When
# they enter their name, print a greeting to the screen and add a line
# recording their visit in a file called guest_book.txt. Make sure each
# entry appears on a new line in the file.

filename = "guest_name.txt"
prompt = 'Enter your name please: '

active = True
while active:
    guest_input = input(prompt)

    if guest_input == 'quit':
        active = False
    else:
        print(guest_input)
        with open(filename, 'a') as file_object:
            file_object.write(guest_input.title() + "\n")