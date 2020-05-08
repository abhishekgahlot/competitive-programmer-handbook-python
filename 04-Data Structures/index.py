# Data Structures

# Arrays
arr = [1, 2, 3, 4, 5, 6]
arr.pop()
arr.pop()
print(arr)

arr.append(1)
print(arr)

# Set
s = set([1, 2, 3, 4, 5, 2])
print(s)

s.remove(5)
print(s)

s.add(6)
print(s)

print(len(s))

# Map or Object
dictionary = {}
dictionary[1] = 2
dictionary[2] = 3

print(dictionary)
print(dictionary.keys())
print(dictionary.values())
print(dictionary.items())

for i,j in dictionary.items():
	print(i,j)

print(2 in dictionary)
print(3 in dictionary)

