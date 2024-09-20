def gcd(a, b):  #Greatest Common Divisor algorithm
    while b:
        a, b = b, a % b
    return a

print(gcd(91, 35))
