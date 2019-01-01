# Sandwiches: Write a function that accepts a list of items a person
# wants on a sandwich. The function should have one parameter that
# collects as many items as the function call provides, and it should
# print a summary of the sandwich that is being ordered. Call the
# function three times, using a different number of arguments each time.

def sandwich_items(*items):
    """Summarize the sandwich we are about to make."""
    print("\nMaking a sandwich with the following items:")
    for item in items:
        print("- " + item)

sandwich_items('pepperoni')
sandwich_items('mushrooms', 'pepperoni', 'olives')