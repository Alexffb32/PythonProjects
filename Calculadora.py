import math
import cmath
def calculate():
    expression = input("Enter an expression: ")
    result = eval(expression, {"__builtins__": None}, {"math": math, "cmath": cmath})
    print("Result:", result)
calculate()
