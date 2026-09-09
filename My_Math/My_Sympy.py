import sympy as sy
from sympy import symbols
from sympy.plotting import plot

x = sy.symbols('x')
y,i,n,a,b = sy.symbols('y i n a b')

f= x**2 + 1

print(f.subs(x , 2))

print(sy.expand((x+y)**3))

print(sy.simplify((x + x * y) / x))

print(sy.limit(sy.sin(x) / x , x , 0))

print(sy.diff(x**4 + x**3 + x , x))

print(sy.integrate(6 * x**5 + 2 * x ** 2 + x , x))

print(sy.solveset(x-1,x))

plot(x**2 , (x,-5,5))

plot(1 /  (1 + sy.exp(-x)) ,(x , -1 , 1))