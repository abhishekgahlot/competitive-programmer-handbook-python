# Bubble Sort O(n^2)
arr = [1, 3, 8, 2, 9, 2, 5, 6]
for i,j in enumerate(arr):
	for a,b in enumerate(arr[:-1]):
		if arr[a] > arr[a+1]:
			arr[a], arr[a+1] = arr[a+1], arr[a]
print arr

# Merge Sort
arr = [1, 3, 8, 2, 9, 2, 5, 6]
def merge_sort(arr):
  if len(arr) <= 1:
    return arr
  middle = len(arr) // 2
  left = arr[:middle]
  right = arr[middle:]
  sleft = merge_sort(left)
  sright = merge_sort(right)
  return merge(sleft, sright)

def merge(left, right):
  result = []
  while (left and right):
    if left[0] < right[0]:
      result.append(left[0])
      left.pop(0)
    else:
      result.append(right[0])
      right.pop(0)
  if left:
    result += left
  if right:
    result += right
  return result

# Counting Sort
def counting_sort(arr, max_val):
    count_arr = [0] * (max_val + 1)
    for num in arr:
        count_arr[num] += 1    
    for i in range(1, len(count_arr)):
        count_arr[i] += count_arr[i - 1]
    output_arr = [0] * len(arr)
    i = len(arr) - 1
    while i >= 0:
        curr_ele = arr[i]
        count_arr[curr_ele] -= 1
        new_pos = count_arr[curr_ele]
        output_arr[new_pos] = curr_ele
        i -= 1
    return output_arr

# Sorting functions in Python
arr = [1, 3, 8, 2, 9, 2, 5, 6]
print(sorted(arr), arr)
print(arr.sort(), arr)

# Binary Search
arr = [1, 2, 2, 3, 5, 6, 8, 9]
def binary_search(arr, elem, prim_index = 0):
	mid = len(arr) / 2
	mid_elem = arr[mid]
	if mid_elem == elem:
		return mid + prim_index
	if mid_elem > elem:
		return binary_search(arr[:mid], elem, prim_index)
	if mid_elem < elem:
		return binary_search(arr[mid:], elem, prim_index+mid)

print binary_search(arr, 9)
print binary_search(arr, 5)
print binary_search(arr, 3)


# Upper Bound and Lower Bound Python
