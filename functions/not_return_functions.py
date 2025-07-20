def print_even_numbers(numbers):
    for elem in numbers:
        if elem % 2 == 0:
            print(elem)

number_list = [1, 2, 3, 4, 5]
print_even_numbers(number_list)
