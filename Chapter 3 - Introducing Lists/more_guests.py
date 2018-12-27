# More Guests: You just found a bigger dinner table, so now more space is
# available. Think of three more guests to invite to dinner.
# • Start with your program from Exercise 3-4 or Exercise 3-5. Add a print
# statement to the end of your program informing people that you found a
# bigger dinner table.
# • Use insert() to add one new guest to the beginning of your list
# • Use insert() to add one new guest to the middle of your list
# • Use append() to add one new guest to the end of your list
# • Print a new set of invitation messages, one for each person in your list

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
