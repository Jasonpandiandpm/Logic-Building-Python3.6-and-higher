'''
11.Swapping Two Elements of a List.
'''

mylist = [1,2,3,4,5,6]
print(f'Before Swapping: {mylist}')
temp = mylist[0]
mylist[0] = mylist[1]
mylist[1] = temp
print(f'After Swapping: {mylist}')