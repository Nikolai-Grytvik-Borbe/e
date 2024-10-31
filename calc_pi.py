from decimal import Decimal, getcontext
import math

getcontext().prec = 30000000  # High precision

def calculate_pi():
    val = Decimal(0)
    n = 0
    factor = Decimal(2).sqrt() * Decimal(2) / Decimal(9801)  # Properly compute the constant factor with Decimal
    while True:
        # Calculate the nth term in Ramanujan's series
        term = (Decimal(math.factorial(4 * n)) * (1103 + 26390 * n)) / (
            Decimal(math.factorial(n)) ** 4 * Decimal(396) ** (4 * n)
        )
        val += term
        
        # Check for convergence
        if term < Decimal("1e-10"):
            break
        
        if n % 2 == 0:  # Adjusted print frequency for testing
            print(f"{n} terms computed")
        
        n += 1

    # Apply the factor to get the final value of pi
    return Decimal(1) / (factor * val)


pi = calculate_pi()
with open("pi.txt", "w") as file:
    file.write(str(pi))

