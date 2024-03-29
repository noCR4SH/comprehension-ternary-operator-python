# Before
# sentence = "Look at those flying geese!"
# vowels = set()
# for char in sentence:
#     if char in 'aeiouAEIOU':
#         vowels.add(char)
# print(vowels)

sentence = "Look at those flying geese!"
vowels = {char for char in sentence if char in 'aeiouAEIOU'}
print(vowels)