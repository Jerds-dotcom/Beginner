
list_ = [i for i in range(1, 11)] 
target = 6

def search(array, target):
	left = 0
	right = len(array) -1 
	while left <= right:
		mid = int((left + right) / 2)

		if array[mid] == target:
			return mid

		elif target < array[mid]: # 
			right = mid - 1 # 

		else:
			left = mid + 1 

	return 'Target not in the list'

search(list_, target)