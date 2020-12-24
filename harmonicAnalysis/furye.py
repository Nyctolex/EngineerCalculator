import sympy as sp
x, n = sp.symbols('x n')

def trigo_to_sign(f):
    f = f.subs(sp.cos(sp.pi*n), (-1)**n)
    f = f.subs(sp.sin(sp.pi*n), 0)
    f = sp.simplify(f)
    return f

def inner_mul(f1, f2, symb=x):
    return (1/sp.pi)*sp.integrate(f1*f2, (symb, -sp.pi, sp.pi), conds='none')

def get_a0(f, symb=x):
    f = inner_mul(f, 1, symb)
    f = trigo_to_sign(f)
    return f

def get_an(f, symb=x):
    f = inner_mul(f, sp.cos(n*x), symb)
    f = trigo_to_sign(f)
    return f

def get_bn(f, symb=x):
    f = inner_mul(f, sp.sin(n*x), symb)
    f = trigo_to_sign(f)
    return f

def get_furye_intro(f, symb=x):
    a0 = get_a0(f, symb)
    an = get_an(f, symb)
    bn = get_bn(f, symb)
    return (a0, an, bn)

f = x+1
print(get_furye_intro(f))
# x = sp.Symbol('x')
# y = sp.Symbol('y')
# z = 2*x*y
# for sy in z.free_symbols:
#     print(sp.diff(z, sy))

#print (z.subs(x, 2))