# Before
# numbers = [1, 2, 2, 3, 4, 4, 5]
# unique_squares = set()
# for x in numbers:
#     unique_squares.add(x**2)
# print(unique_squares)

numbers = [1, 2, 2, 3, 4, 4, 5]
unique_squares = {x**2 for x in numbers}
print(unique_squares)