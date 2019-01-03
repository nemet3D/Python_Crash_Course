# Programming Poll: Write a while loop that asks people why they like
# programming. Each time someone enters a reason, add their reason to a
# file that stores all the responses.

filename = "programming_pool.txt"
prompt = 'While do you like programming? '

active = True
while active:
    user_answer = input(prompt)

    if user_answer == 'quit':
        active = False
    else:
        print(user_answer)
        with open(filename, 'a') as file_object:
            file_object.write(user_answer.title() + "\n")