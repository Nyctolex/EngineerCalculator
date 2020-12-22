import sympy as sp
from all_symbols import *
from sympy.parsing.sympy_parser import parse_expr
from sympy.parsing.sympy_parser import standard_transformations, implicit_multiplication_application

def delta_prase(expression):
    """
    Replaces Δ*symbol expretion to Δsymbol.
    """
    Δ = sp.Symbol('Δ')
    for key in string_to_symbol_dict:
        if 'd' not in key:
            symbol = string_to_symbol_dict[key]
            delta = error_dict[symbol]
            expression = expression.subs(symbol*Δ, delta)
    return(expression)

def prase_string(str_equation):
    """
    converts a string equation to sympy equation.
    """
    transformations = (standard_transformations + (implicit_multiplication_application,))
    expression = parse_expr(str_equation, transformations=transformations)
    expression = delta_prase(expression)
    return expression