'''
18.How to Solve a Quadratic Equation.
'''
import cmath
a,b,c=1,4,2

dis = (b**2) - (4*a*c)

ans1 =(-b-cmath.sqrt(dis))/(2*a)
ans2 =(-b+cmath.sqrt(dis))/(2*a)
print(f'The roots are: {ans1},{ans2}')