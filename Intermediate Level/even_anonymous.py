'''
30.Filtering Even number of list using anonymous function
'''
num_list = [i for i in range(0,11)]
print(list(filter(lambda num: num%2 == 0,num_list)))