# Finger exercise: Write a program that asks the user to input 10 integers,
# and then prints the largest odd number that was entered. If no odd number
# was entered, it should print a message to that effect.

count = 10

while count != 0:
    current = int(input("Please type an integer: "))
    # initialize current_max
    if count == 10:
        current_max = current
    # if current-max is even
    if current % 2 == 0:
        count -= 1
    elif current_max % 2 == 0 and current %2 !=0:
        current_max = current
    elif current >= current_max:
        current_max = current
        count -= 1
    else:
        count -= 1
if current_max % 2 == 0:
    print("All integers entered were even")
else:
    print(current_max, "is the largest odd integer.")