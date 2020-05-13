# Bubble Sort O(n^2)
arr = [1, 3, 8, 2, 9, 2, 5, 6]
for i, j in enumerate(arr):
    for a, b in enumerate(arr[:-1]):
        if arr[a] > arr[a + 1]:
            arr[a], arr[a + 1] = arr[a + 1], arr[a]
print(arr)

# Merge Sort
arr = [1, 3, 8, 2, 9, 2, 5, 6]

# Counting Sort


# Sorting functions in Python
arr = [1, 3, 8, 2, 9, 2, 5, 6]
print(sorted(arr), arr)
print(arr.sort(), arr)

# Binary Search
arr = [1, 2, 2, 3, 5, 6, 8, 9]


def binary_search(arr, elem, prim_index=0):
    mid = int(len(arr) / 2)
    mid_elem = arr[mid]
    if mid_elem == elem:
        return mid + prim_index
    if mid_elem > elem:
        return binary_search(arr[:mid], elem, prim_index)
    if mid_elem < elem:
        return binary_search(arr[mid:], elem, prim_index + mid)


print(binary_search(arr, 9))
print(binary_search(arr, 5))
print(binary_search(arr, 3))

# Upper Bound and Lower Bound Python
