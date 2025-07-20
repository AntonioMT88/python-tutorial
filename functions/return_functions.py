def compare_x_and_y(x, y) -> bool:
    if x > y:
        return True
    else:
        return False


first_number = int(input("Insert a number:"))
second_number = int(input("Insert a second number:"))

x_greater_than_y = compare_x_and_y(first_number, second_number)

if x_greater_than_y == True:
    print("X is greater than Y")
else:
    print("X is lower or equal than Y")

