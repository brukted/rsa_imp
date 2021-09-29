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


def encrypt(public_key, num):
    e, n = public_key
    return pow(num, e, n)


def decrypt(private_key, num):
    d, n = private_key
    return pow(num, d, n)


def gen_key(p, q):
    n = p * q
    r = (p - 1) * (q - 1)
    e = 0
    # finds an e such that e mod r = 1
    for i in range(2, 1000):
        if gcd(r, i) == 1:
            e = i
            break
    d = multiplicative_inverse(e, r)  # de = 1 (mod(p-1)(q-1))
    return (e, n), (d, n)


def main():
    public_key, private_key = gen_key(13, 17)
    print("Public key", public_key)
    print("Private key", private_key)

    k = 77
    en = encrypt(public_key, k)
    de = decrypt(private_key, en)

    print(k)
    print(en)
    print(de)


if __name__ == '__main__':
    main()
