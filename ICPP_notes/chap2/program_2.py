# At this point in the book, iteration has not been introduced but a
# faster way uses list and for loops:

x = int(input("Please type an integer: "))
y = int(input("Please type an integer: "))
z = int(input("Please type an integer: "))

numbers = [x, y, z]
odds = []

for i in numbers:
    if i % 2 != 0:
        odds.append(i)

# check if any odds
if len(odds) == 0:
    print("All integers are even.")
else:
    max_odd = max(odds)
    print(max_odd, "is the largest odd.")