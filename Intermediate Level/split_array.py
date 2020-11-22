'''
50.Split the array and add the first part to the end
'''

array = ['a','b','c','d','e','f']
div = (len(array)//2)
arrary_1 = array[div:] + array[:div]
print(arrary_1)