# if else condition

# Basic if else example
x = int(input("Insert a number:"))
if x % 2 == 0:
    print("Your number is even")
else:
    print("Your number is odd")

# elif example
x = int(input("\nInsert a number greater than 0:"))
if x == 0:
    print("Invalid value!")
elif x > 0:
    print("You inserted a positive number!")
else:
    print("You inserted a negative number!")
