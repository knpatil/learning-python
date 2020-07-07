
# input()

number = input("Enter some number: ")
number = int(number)

if number % 2 == 0:
    print(f"The number {number} is Even.") # f= format
else:
    print(f"The number {number} is Odd.")


# while loop
num = 1
while num <= 10:
    print(num)
    num += 1   # num = num + 1

# input : quit
prompt = "\n\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program."
message = ""

while message != 'quit':
    message = input(prompt)
    print(f"\n{message}")
    if message == "stop":
        print("breaking the loop")
        break

# continue
# print all the odd numbers between 1 to 10
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)

# infinite loops
x = 1
while x <= 5:
    print(x)
    x += 1

# you want to create infinite loop on purpose
while True:
    user_input = input("Tell me something about you (quit to end the program): ")
    print(user_input)
    if user_input == 'quit':
        break

#
# using while loop with some data structures: list, dict to process some data
#
unconfirmed_users = ['alice','brian', 'scott']
confirmed_users = []

while unconfirmed_users:  # as long as list is not empty, the loop will run
    current_user = unconfirmed_users.pop()
    print(f"Verifying user {current_user} ...")
    confirmed_users.append(current_user)

print("The following users have been confirmed: ")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

#
# while loop with dictionaries
#
# Poll about a favorite mountain
#
responses = {}   # empty dictionary
# set some flag to indicate if polling is active or not
polling_active = True
while polling_active:
    name = input("\nWhat is your name? ")
    response = input("What is your favorite mountain? ")
    # store this in in our dictionary
    responses[name] = response

    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat == 'no':
        polling_active = False

# polling is complete, print the result
print("\n-----Poll Results--------")
for name, response in responses.items():  # reading a dictionary
    print(f"{name}'s favorite mountain is {response}.")








