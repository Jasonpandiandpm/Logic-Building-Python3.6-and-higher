'''
41.Transpose of a matrix
'''
new = []
m = [[1,2,3],[4,5,6],[7,8,9]]
	# [1, 2, 3]
	# [4, 5, 6]
	# [7, 8, 9]
transpose = [[m[j][i] for j in range(len(m))] for i in range(len(m))] 
for i in transpose:
	print(i)
	# [1, 4, 7]
	# [2, 5, 8]
	# [3, 6, 9]