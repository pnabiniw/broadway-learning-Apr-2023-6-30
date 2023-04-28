### Slicing examples

a = [1, 2, 3, 4, 5, 6, 7, 8]
print(a[2:7])  # => this gives [3, 4, 5, 6, 7]
print(a[0:7])
print(a[:7])  # => this gives value from 0 to 6th index like above
print(a[2:])  # => this gives all the elements of the list from 2nd index onward

# Slicing in negative indexing
print(a[-5: -2])  # gives elements from -5 index to -3 index
print(a[2: -3])   # gives elements from 2 index to -4 index



# List operations

l1 = [1, 2, 3]
l2 = [4, 5, 6]
add = l1 + l2   # We can use addition operator

broadcast = l1 * 3   # It gives result [1,2,3,1,2,3,1,2,3]. Its also called broadcast

print(1 in l1)  # Membership check. It gives True
print(6 not in l2)  # Membership check. It gives False

# List Methods
vowels = ['a', 'e', 'i', 'o']
vowels.append('u')   # This gives ['a', 'e', 'i', 'o', 'u']
print(vowels)

l1 = ["python", "is"]
l2 = ["an", "awesome"]
l1.extend(l2)
print(l1)  # it gives ["python", "is", "an", "awesome", "language"]


l1 = [1, 2, 3, 4, 3]
l1.insert(2, 7)  # inserts element 7 at index 2
l1.remove(3)   # It removes the element provided in the parameter. In this case 3.

value = l1.pop()  # It pops out value from the last of the list
print(value)
value = l1.pop(3)  # It pops out the element at provided index. In this case at index 3
print(value)
l1.clear()  # Clears the list


vowels = ["a", "e", "i", "o", "u", "e", "u"]
print(vowels.index("e"))  # It gives result 1
print(vowels.index("e", 2, 6))  # It searches "e" in the range 2 to 6. Thus returns 5

print(vowels.count("e"))  # returns 2 because "e" occurs 2 times in the list vowels

l = [5, 4, 1, 2, 6, 7]
l.sort()  # This sorts the elements in ascending order
print(l)
l.sort(reverse=True)  # This sorts the elements in descending order
print(l)
