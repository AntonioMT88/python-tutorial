# While loop

print("Printing all values from 10 down to 6...")
x = 10
while x > 5:
    print(x)
    x = x - 1
else:
    print("Value of 5 was reached. While loop will be terminated immediately!")

print("Print all even values from 10 to 0...")
x = 10
while x >= 0:
    if x % 2 == 0:
        print(x)
    x = x - 1


