# One Million: Make a list of the numbers from one to one million, and then
# use a for loop to print the numbers . (If the output is taking too long, stop it by
# pressing ctrl -C or by closing the output window .)

# Summing a Million: Make a list of the numbers from one to one million,
# and then use min() and max() to make sure your list actually starts at one and
# ends at one million . Also, use the sum() function to see how quickly Python can
# add a million numbers .

million = [number for number in range(1, 1_000_001)]

print(min(million))

print(max(million))

print(sum(million))