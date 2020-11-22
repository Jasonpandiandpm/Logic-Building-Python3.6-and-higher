'''
35.Binary Search
'''
mylist = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
target = int(input("Enter the number from 0 t0 19: "))

def binary_search(arr,x):
	first = 0
	last = len(arr)-1
	mid = first + last//2
	while True:
		if arr[mid] == x:
			print(f'The {target} is found at index: {mid}')
			break
		elif x < arr[mid]:
			first = 0
			last = mid - 1
			mid = first + last//2			
		elif x > arr[mid]:
			last = 0
			first = mid + 1
			mid = first + last//2
binary_search(mylist,target)