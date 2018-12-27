# Dinner Guests: Working with one of the programs from Exercises 3-4
# through 3-7 (page 46), use len() to print a message indicating the number
# of people you are inviting to dinner .

guests = ['warren buffet', 'ronaldo', 'octavianus augustus']

print('Please join me for dinner Mr. ' + guests[0].title() + "!")
print('Please join me for dinner Mr. ' + guests[1].title() + "!")
print('Please join me for dinner Mr. ' + guests[2].title() + "!")

print('\nOur total number of guests tonight is: ' + str(len(guests)) + '.')