'''
21.Find largest among three numbers
'''
a =int(input("Enter number a:"))
b =int(input("Enter number b:"))
c =int(input("Enter number c:"))
if a > b and a > c:
    print(f'A is larger: {a}')
elif b > a and b > c:
    print(f'B is larger: {b}')
else:
    print(f'C is larger: {c}')
