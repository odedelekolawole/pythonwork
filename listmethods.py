list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 =['Banana', 'Apple', 'Mango', 'Oranges']
list1.extend(list2)
print(list1)


# Append Method
list2.append('Cherry')
print(list2)
print(len(list2))

list2.insert(1, 'Cherry')
print(list2)

list2.insert(3, 'Pawpaw')
print(list2)

# Removing element
list2.remove('Banana')
print(list2)

# list2.clear()
# print(list2)

print(list2.index('Apple'))
print(list2.index('Mango'))


print(list2)
print(list2.count('Cherry'))


animals = ['Cat', 'Dog', 'Dog', 'Goat']
print(animals.count('Dog'))
animals.reverse()
print(animals)


# list3 = [4, 3, 5, 1 , 2]
# list3.sort()
# print(list3)

animals2 = animals.copy()
print(animals2)

animals2.pop()
print(animals2)


# Removing Item
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
alphabet.pop(1)
del alphabet[0]
# del alphabet
print(alphabet)