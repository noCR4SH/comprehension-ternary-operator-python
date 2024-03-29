# Before
# user_input = input("Enter your name: ")
# if user_input:
#     name = user_input
# else:
#     name = "Guest"
# print(f"Hello, {name}")

user_input = input("Enter your name: ")
name = user_input if user_input else 'Guest'
print(f"Hello, {name}")