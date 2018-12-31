# Pizza Toppings: Write a loop that prompts the user to enter a series
# of pizza toppings until they enter a 'quit' value. As they enter each
# topping, print a message saying you’ll add that topping to their
# pizza.

prompt = ("\nEnter your pizza toppings:")
prompt += ("\n(Press 'quit' to stop. ")

active = True

while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message.title())