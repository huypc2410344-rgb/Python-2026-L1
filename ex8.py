def extract_even(l):
    return [item for item in l if item % 2 == 0]

my_list = [1, 4, 5, -1, 10]
print(f"Original list: {my_list}")

even_list = extract_even(my_list)
print(f"List with only even numbers: {even_list}")