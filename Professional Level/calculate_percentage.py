'''
45.Calculate Percentage from Mark sheet
'''
subjects = {'Launguage':0,'Science':0,'Maths':0,'Programming':0,'Social Science':0}
for sub in subjects:
	subjects[sub] = int(input(f'Enter Marks of {sub}: '))
sum_sub = sum(subjects.values())
percentage = sum_sub // 5
print(f'Percentage from Mark sheet was: {percentage}%')