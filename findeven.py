LIST = [2, 1, 3, 4, 6, 8, 10, 9, 12, 20]

def is_even(x):
    return x % 2 == 0

even_numbers = [x for x in LIST if is_even(x)]
print("Even numbers:", even_numbers)

    