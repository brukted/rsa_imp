# Iterative version of euclid's algorithm
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def pulverize(a, b):
    # Base Case
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = pulverize(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y


def multiplicative_inverse(a, mod):
    gcd, s, t = pulverize(a, mod)
    if gcd != 1:
        return None
    else:
        return s % mod
