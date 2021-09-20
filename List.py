# LIST####################################################################################3
# a = [2, "Disha", '123']
# print(a)
# print(a[0:2])
# print(a[::-1])  # Slicing reverse

# List comprehension: shorter syntax when you want to create a new list based on the values of an existing list.
# to add in list: append, insert, extend
# to remove item in list: remove, pop, del, clear

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even = []
odd = []

for data in a:
    if data % 2 == 0:
        even.append(data)
    else:
        odd.append(data)

print(even)
print(odd)
