# Write a program that examines three variables — x, y, and z — and prints the 
# largest odd number among them. If none of them are odd, it should print a 
# message to that effect.
 
x = int(input("Please type an integer: "))
y = int(input("Please type an integer: "))
z = int(input("Please type an integer: "))

# First check if all are even.
if x % 2 == 0 and y % 2 == 0 and z % 2 == 0:
    print("All integers are even.")
elif x % 2 != 0: 
# if above condition fails, at least one is odd so check x
# if x is odd, we have to examine y and z.
    if y % 2 == 0 and z % 2 == 0: # x is only odd
        print(x, "is largest odd.")
    elif y % 2 != 0 and z % 2 == 0: # x and y only odds
        if x > y:
            print(x, "is largest odd.")
        else: 
            print(y, "is largest odd.")        
    elif y % 2 == 0 and z % 2 != 0: # x and z are only odds
        if x > z:
            print(x, "is largest odd.")
        else: 
            print(z, "is largest odd.") 
    else: #all are odd
        if x > y and x > z:
            print(x, "is the largest odd.")
        elif y > z:
            print(y, "is the largest odd.")
        else: 
            print(z, "is the largest odd.")
    
elif y % 2 != 0: # at least one is odd, x is even, so check y
    if z % 2 == 0:
        print(y, "is the largest odd.")
    elif y > z:
        print(y, "is the largest odd.")
    else: 
        print(z, "is the largest odd.")
else: # we know at least one is odd and x and y are both even, hence z
    print(z, "is largest odd.")
