import sympy as sym

# Define variables and function
x, y = sym.symbols('x y')
f = sym.sin(x*y)

# Define the center of expansion
a, b = 1, 2

# Define the order of the expansion
order = 2

# Calculate the Taylor series expansion
taylor_series = sym.series(f, (x, a), (y, b), n=order).removeO()

# Print the result
print(taylor_series)
