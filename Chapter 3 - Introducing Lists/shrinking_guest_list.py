# Shrinking Guest List: You just found out that your new dinner table won’t
# arrive in time for the dinner, and you have space for only two guests .
# • Start with your program from Exercise 3-6 . Add a new line that prints a
# message saying that you can invite only two people for dinner .
# • Use pop() to remove guests from your list one at a time until only two
# names remain in your list . Each time you pop a name from your list, print
# a message to that person letting them know you’re sorry you can’t invite
# them to dinner .
# • Print a message to each of the two people still on your list, letting them
# know they’re still invited .
# • Use del to remove the last two names from your list, so you have an empty
# list . Print your list to make sure you actually have an empty list at the end
# of your program .

guests = ['warren buffet', 'ronaldo', 'octavianus augustus']

print('Please join us for dinner Mr. ' + guests[0].title() + "!")
print('Please join us for dinner Mr. ' + guests[1].title() + "!")

replaced_guest = guests.pop(-1)
print('Unfortunately Mr. ' + replaced_guest.title() + " will not be able to join us.")

guests.append('Elon Musk')

print('\nPlease join us for dinner Mr. ' + guests[0].title() + "!")
print('Please join us for dinner Mr. ' + guests[1].title() + "!")
print('Please join us for dinner Mr. ' + guests[2].title() + "!")

print('\nWe have found a bigger dining table.')

guests.insert(0, 'leonardo daVinci')
guests.insert(1, 'emanuel macron')
guests.insert(-1, 'abraham lincoln')

print('\nPlease join us for dinner Mr. ' + guests[0].title() + "!")
print('Please join us for dinner Mr. ' + guests[1].title() + "!")
print('Please join us for dinner Mr. ' + guests[2].title() + "!")
print('Please join us for dinner Mr. ' + guests[3].title() + "!")
print('Please join us for dinner Mr. ' + guests[4].title() + "!")
print('Please join us for dinner Mr. ' + guests[5].title() + "!")

print('\nUnfortunately the new table will not arrive in time and I can only invite two people for dinner.')

not_invited = guests.pop()
print("\nMr. " + not_invited.title() + " I am sorry I can’t invite you to dinner anymore.")
not_invited = guests.pop()
print("Mr. " + not_invited.title() + " I am sorry I can’t invite you to dinner anymore.")
not_invited = guests.pop()
print("Mr. " + not_invited.title() + " I am sorry I can’t invite you to dinner anymore.")
not_invited = guests.pop()
print("Mr. " + not_invited.title() + " I am sorry I can’t invite you to dinner anymore.")

print('\nPlease join us for dinner Mr. ' + guests[0].title() + "!")
print('Please join us for dinner Mr. ' + guests[1].title() + "!")

del guests[0]
del guests[0]
print('\n' + str(guests))