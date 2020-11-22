'''
44.Union,Intersection,Difference,symmetric difference of two sets
'''
a = {1,2,3,4,5}
b = {1,2,4,6}
print(f'set A: {a}')
print(f'set B: {b}')
print(f'A Union B: {a.union(b)}')
print(f'A Intersection B: {a.intersection(b)}')
print(f'Difference of A-B: {a-b}')
print(f'Difference of B-A: {b-a}')
print(f'Symmetric Difference A and B: {a^b}')
print(f'Symmetric Difference B and A: {b^a}')