# For loop

fruit_list = ["Apple", "Banana", "Coconut", "Raspberry", "Strawberry"]

print("Printing all elements in the list...")
for fruit in fruit_list:
    print(fruit)

print("\nPrinting all elements in the list with else clause execution...")
for fruit in fruit_list:
    print(fruit)
else:
    print("No more elements!")

print("\nPrinting all elements in the list except for Banana...")
for fruit in fruit_list:
    if fruit == "Banana":
        continue
    print(fruit)

print("\nPrinting all elements in a range of values...")
for x in range(10):
    print(x)

print("\nPrinting all numbers in the list. Break the loop if there is any non number element")
number_list = [1, 2, 3, "a", 4, 5]
for x in number_list:
    if type(x) is int:
        print(x)
    else:
        print(f"Found not number element: {x}")
        print("For Loop will be terminated immediately")
        break


