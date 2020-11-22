'''
42.Addition of Two matrix
'''
a = [[3,1,1],[1,1,1],[1,1,1]]
b = [[1,1,1],[1,1,1],[3,1,1]]
add = [[(a[i][j] + b[i][j]) for j in range(len(b))] for i in range(len(a))]
for i in add:
	print(i)