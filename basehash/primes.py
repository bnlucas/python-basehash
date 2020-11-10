from random import randrange

from six.moves import xrange, reduce

try:
    from gmpy2 import is_prime as gmpy2_is_prime, next_prime as gmpy2_next_prime
    GMPY2 = True
except ImportError:
    GMPY2 = False


PRIMES_LE_31 = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31)
PRIMONIAL_31 = 200560490130


def modinv(n, m):
    '''
    returns the modular inverse of n mod m.
    '''
    g, _g = n, m
    x, _x = 1, 0

    while _g:
        q = g // _g
        g, _g = _g, (g - q * _g)
        x, _x = _x, (x - q * _x)

    if g > 1:
        raise ValueError('There is no inverse for {} mod {}'.format(n, m))

    if x < 0:
        x = x + m

    return x


def gcd(*n):
    try:
        from math import gcd
    except ImportError:
        # Python 3.4 and earlier
        from fractions import gcd

    return abs(reduce(gcd, n))


def isqrt(n):
    '''
    integer square root.

    - In number theory, the integer square root (isqrt) of a positive integer n
      is the positive integer m which is the greatest integer less than or equal
      to the square root of n.

    '''
    if n < 0:
        raise ValueError('Square root is not defined for negative numbers.')

    if n < 2:
        return 2

    a = 1 << ((1 + n.bit_length()) >> 1)

    while True:
        b = (a + n // a) >> 1

        if b >= a:
            return a

        a = b


def is_square(n):
    '''
    Determine if n is square based on the integer square root: isqrt(n)
    '''
    s = isqrt(n)
    return s * s == n


def factor(n, p=2):
    '''
    Compute n-1 = 2^s * d for strong psuedoprime and strong lucas psuedoprime.
    '''
    s = 0
    n -= 1

    while not n % p:
        s += 1
        n //= p

    return s, n


def jacobi(a, p):
    if (not p & 1) or (p < 0):
        raise ValueError('p must be a positive odd number.')

    if (a == 0) or (a == 1):
        return a

    a = a % p
    t = 1

    while a != 0:
        while not a & 1:
            a >>= 1
            if p & 7 in (3, 5):
                t = -t

        a, p = p, a
        if (a & 3 == 3) and (p & 3) == 3:
            t = -t

        a = a % p

    if p == 1:
        return t

    return 0


def selfridge(n):
    d = 5
    s = 1
    ds = d * s

    while True:
        if gcd(ds, n) > 1:
            return ds, 0, 0

        if jacobi(ds, n) == -1:
            return ds, 1, (1 - ds) // 4

        d += 2
        s *= -1
        ds = d * s


def lucas_sequence(n, u1, v1, u2, v2, d, q, m):
    k = q
    while m > 0:
        u2 = (u2 * v2) % n
        v2 = (v2 * v2 - 2 * q) % n
        q = (q * q) % n

        if m & 1:
            t1, t2 = u2 * v1, u1 * v2
            t3, t4 = v2 * v1, u2 * u1 * d
            u1, v1 = t1 + t2, t3 + t4

            if u1 & 1:
                u1 = u1 + n

            if v1 & 1:
                v1 = v1 + n

            u1, v1 = (u1 // 2) % n, (v1 // 2) % n
            k = (q * k) % n

        m = m >> 1

    return u1, v1, k


def trial_division(n):
    return all(n % i for i in xrange(3, isqrt(n) + 1, 2))


def strong_pseudoprime(n, base=2, s=None, d=None):
    if not n & 1:
        return False

    if not s or not d:
        s, d = factor(n, 2)

    x = pow(base, d, n)

    if x == 1:
        return True

    for i in xrange(s):
        if x == n - 1:
            return True

        x = pow(x, 2, n)

    return False


def small_strong_pseudoprime(n):
    for i in [2, 13, 23, 1662803]:
        if not strong_pseudoprime(n, i):
            return False

    return True


def lucas_pseudoprime(n):
    if not n & 1:
        return False

    d, p, q = selfridge(n)
    if p == 0:
        return n == d

    u, v, k = lucas_sequence(n, 0, 2, 1, p, d, q, (n + 1) >> 1)
    return u == 0


def strong_lucas_pseudoprime(n):
    if not n & 1:
        return False

    d, p, q = selfridge(n)
    if p == 0:
        return n == d

    s, t = factor(n + 2)

    u, v, k = lucas_sequence(n, 1, p, 1, p, d, q, t >> 1)

    if (u == 0) or (v == 0):
        return True

    for i in xrange(1, s):
        v = (v * v - 2 * k) % n
        k = (k * k) % n
        if v == 0:
            return True

    return False


def baillie_psw(n, limit=100):
    if n == 2:
        return True

    if not n & 1:
        return False

    if n < 2 or is_square(n):
        return False

    if gcd(n, PRIMONIAL_31) > 1:
        return n in PRIMES_LE_31

    bound = min(limit, isqrt(n))
    for i in xrange(3, bound, 2):
        if not n % i:
            return False

    return strong_pseudoprime(n, 2) \
        and strong_pseudoprime(n, 3) \
        and strong_lucas_pseudoprime(n)


def is_prime(n):
    if GMPY2:
        return gmpy2_is_prime(n)

    if int(n) != n:
        return ValueError('Non-integer provided.')

    if gcd(n, 510510) > 1:
        return (n in (2, 3, 5, 7, 11, 13, 17))

    if n < 2000000:
        return trial_division(n)

    if n.bit_length() <= 512:
        if not small_strong_pseudoprime(n):
            return False

    return baillie_psw(n)


def next_prime(n):
    if GMPY2:
        return gmpy2_next_prime(n)

    if n < 2:
        return 2

    if n < 5:
        return [3, 5, 5][n - 2]

    gap = [1, 6, 5, 4, 3, 2, 1, 4, 3, 2, 1, 2, 1, 4, 3, 2, 1, 2, 1, 4, 3, 2, 1,
           6, 5, 4, 3, 2, 1, 2]

    n += (1 + (n & 1))

    if n % 3 == 0 or n % 5 == 0:
        n += gap[n % 30]

    while not is_prime(n):
        n += gap[n % 30]

    return n
