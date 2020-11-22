'''
7.How to check given Element exists in List or not.
'''
mylist = [1,2,3,4,5,6,7,8,9,10]
search = int(input("Search the element inside the list: "))

if search in mylist:
    print(f'{search} is exist in the list')
else:
    print(f'{search} does not exists in the list.')