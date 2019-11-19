# Bubble Sort O(n^2)
arr = [1, 3, 8, 2, 9, 2, 5, 6]
for i,j in enumerate(arr):
	for a,b in enumerate(arr[:-1]):
		if arr[a] > arr[a+1]:
			arr[a], arr[a+1] = arr[a+1], arr[a]
print arr

# Merge Sort