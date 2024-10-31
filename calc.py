from decimal import Decimal, getcontext
from math import factorial

getcontext().prec = 100000

def calculate_e():
    e = Decimal(1)
    n = 0
    while True:
        n += 1
        term = Decimal(1) / Decimal(factorial(n))
        if e + term == e:
            break

        e += term
        if n % 100 == 0:
            print(f'{n} terms: {e:.10f}')
            
    return e

e = calculate_e()

# format
e_str = str(e).replace(".", "")
e_str = e_str[1:]
formatted = ' '.join(e_str[i:i+10] for i in range(0, len(e_str), 10))
print(formatted)
