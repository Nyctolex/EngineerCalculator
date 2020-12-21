import math
import pandas as pd
import lab_calculator
import pyperclip
import pandas as pd
import sympy as sp
from sympy.printing.mathml import mathml
import re

CLIPBOARD_COPY = True
#Should the returned data should be copied to clipboard or not.
PRINT_VALUES = True
#Should the returned data should be printed or not.
KEYWORDS_FILTER = [" not rsqr"]
#Filtering wanted folders out of th main plot folder.

def print_or_copy(data, print_values=PRINT_VALUES, copy_values=CLIPBOARD_COPY):
    """
    Choosing the correct action according to the global values.
    """
    if PRINT_VALUES:
        print(data)
    if CLIPBOARD_COPY:
        pyperclip.copy(data)

def copy_table(file_display=False):
    """
    Copies wanted data to clipboard in a format of a table. Usfull for reports.
    """ 
    data = {"file": load_folders(),
        "a_0":load_a(0),
    	"Δa_0":load_d(0),
        "a_1":load_a(1),
        "Δa_1":load_d(1),
        "a_2":load_a(2),
        "Δa_2":load_d(2),
        "χ_red^2":load_chi(),
        "P_probability":load_p()}
    df =pd.DataFrame(data)
    print(df)
    if not file_display:
        data.pop("file")
        df =pd.DataFrame(data)
    df.to_clipboard( index=False)



def format_eq(equation):
    while ("  " in equation):
        equation = equation.replace("  ", " ")
    while ("--" in equation) or ("- -" in equation):
        equation = equation.replace("--", "+")
        equation = equation.replace("- -", "+")
    while ("++" in equation) or ("+ +" in equation):
        equation = equation.replace("++", "+")
        equation = equation.replace("+ +", "+")
    return equation


def total_error(errors_lst):
    total = 0.0
    for er in errors_lst:
        total += er**2
    total = math.sqrt(total)
    return lab_round(er)

def n_sigma_format(theory, theory_error, value, error_value):
    res = lab_calculator.n_sigma(theory, theory_error, value, error_value)
    txt = "N_σ=|({theo}−{val})|/√(({theo_error})^2+({val_er})^2 )={res}".format(theo=theory, val=value, theo_error=theory_error, val_er=error_value, res=res)
    txt = format_eq(txt)
    print_or_copy(txt)
    return txt

def replace_brackets(st):
    st = st.replace('{', '(')
    st = st.replace('}', ')')
    return st

def render_factorial(expression):
    expression = expression.replace('\frac', '\\frac')
    print(expression)
    while (len(re.findall(r'\\frac{.+?}{.+?}', expression)) != 0):
        factors = re.search(r'\\frac{.+?}{.+?}', expression)
        sub_ex = factors.group(0)
        part1 = re.search(r'\\frac{.+?}{', sub_ex).group(0)[len('\\frac'):-1]
        part2 = sub_ex[len('\\frac{')+len(part1)-1:]
        part1 = replace_brackets(part1)
        part2 = replace_brackets(part2)
        new_ex = "{part1}/{part2}".format(part1=part1, part2=part2)
        expression = expression.replace(sub_ex, new_ex)
    return expression

def spympy_to_word(expretion):
    res = sp.latex(expretion)
    res = render_factorial(res)
    res = replace_brackets(res)
    print_or_copy(res)

if __name__ == "__main__":
    x, y, f = sp.symbols('x y f')
    z = (x*(f**2)/y+f)**2 +y/x
    res = sp.latex(z)
    #print (res)
    form = """\sqrt{\left(- \frac{ΔL \left(v_{1}^{2} - v_{2}^{2}\right)}{2 L^{2} g}\right)^{2} + \left(\left(- \frac{Δg \left(v_{1}^{2} - v_{2}^{2}\right)}{2 L g^{2}}\right)^{2} + \left(\left(\frac{v_{1} Δv_{1}}{L g}\right)^{2} + \left(- \frac{v_{2} Δv_{2}}{L g}\right)^{2}\right)\right)}"""
    form = form.replace('\r', '\\r')
    render_factorial(form)