import math
import os
import pyperclip
from copy import deepcopy
#import pandas as pd
import sympy as sp
OUT_FOLDER = r"C:\Users\chris-chen\Documents\TAU\Year B\Semester A\lab\דוחות\צמיגות\output"
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

def value_resolution(val):
    val = abs(val)
    resolution=0
    if (val < 10) and (int(val*100)%10 == 0) and (val - round(val, 2) == 0):
        return 1
    if val >= 10:
        resolution = 0
        while (int(val/10.0) > 10):
            resolution -= 1
            val = int(val/10.0)
        return resolution
    resolution = 1
    while(int(val*10) < 10):
        resolution += 1
        val = val*10
    return resolution

def max_resolution(error_lst):
    error_res = []
    for er in error_lst:
        error_res.append(value_resolution(er))
    return max(error_res)

def lab_round(val, error_value=None):
    if error_value == None:
        error_value = val
    if type(error_value) == list:
        resolution = max_resolution(error_value)
    else:
        resolution = value_resolution(error_value)
    return round(val, resolution)

def result_format(sign, res, er):
    er = labFormat.lab_round(er)
    res = labFormat.lab_round(res, er)
    res_for = "{sign} = {res} ± {er}".format(sign=sign, res=res, er=er)
    print_or_copy(res_for)

def relative_error(val, er):
    er = abs(er)
    rel = lab_round(er/val)
    rel = lab_round(rel*100.0)
    return rel

def calculate_n_sigma(theory, theory_error, value, error_value):
    theory_error = lab_round(theory_error)
    error_value = lab_round(error_value)
    theory = lab_round(theory, theory_error)
    value = lab_round(value, error_value)
    res = abs(theory - value)/math.sqrt(theory_error**2 + error_value**2)
    res = lab_round(res, [theory_error, error_value])
    return res 

def geo_avg_value(value_lst):
    pass

def get_geo_avg_formula(expression_lst):
    geo_avg = None
    for expression in expression_lst:
        print(sp.srepr(expression))

        if geo_avg is None:
            geo_avg = sp.Pow(expression, 2, evaluate=False)
        else:    
            geo_avg = sp.Add(geo_avg, sp.Pow(expression, 2, evaluate=False), evaluate=True)
    return(sp.sqrt(geo_avg))

def get_error_formula(formula, error_dict):
    """
    getting a total error of a formula according to its derevatives
    """
    expression_lst = []
    for symbol in formula.free_symbols:
        sub_ex = sp.Mul(sp.diff(formula, symbol), error_dict[symbol], evaluate=True)
        sub_ex = sp.simplify(sub_ex)
        expression_lst.append(sub_ex)
    return get_geo_avg_formula(expression_lst)

def get_ruler_error(value):
    return lab_round(value/math.sqrt(12))

def sub_formula(expression, value_dict, round_result=False):
    """
    substuting given values in formula.
    """
    values= [(k, v) for k, v in value_dict.items()]
    result = expression.subs(values)
    if round_result:
        result = lab_round(result)
    return result

def get_val_and_error(formula, error_dict, value_dict):
    """
    returning the value of a formula after substituting values and its error.
    """
    error_expression = get_error_formula(formula, error_dict)
    error_value = lab_round(sub_formula(error_expression, value_dict)) 
    value = lab_round(sub_formula(formula, value_dict), error_value)
    return (value, error_value)

if __name__ == "__main__":
    pass