def loadKeys(filename='keys.txt'):
    keys = {}
    with open(filename, 'r') as stored_keys:
        keys = eval(stored_keys.readline())
    return keys


def saveKeys(keys, filename='keys.txt'):
    with open(filename, 'w+') as stored_keys:
        stored_keys.write(str(keys))


def gcd(x, y):
    while (y):
        x, y = y, x % y
    return x


def egcd(a, b):
    s, t = 0, 1  # init s0, t0 (sb, tb)
    u, v = 1, 0  # init s1, t1 (sa, ta)
    while a != 0:
        q = b // a

        # Euclide (gcd)
        r = b % a
        a, b = r, a
        sr, tr = s - u * q, t - v * q  # sr,st = s%u, t%v
        s, t, u, v = u, v, sr, tr  # increase index

    gcd = b
    return gcd, s, t


def modinv(a, m):
    gcd, x, _ = egcd(a, m)
    if gcd != 1:
        return None  # modular inverse does not exist
    else:
        return x % m


# if __name__ == "__main__":
#     number, prime = 11, 19
#     factors = (3, 3)
#     print(isPrimitiveRoot(number, prime, factors))
