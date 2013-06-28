from primes import invmul, next_prime

# Default hash key length
HASH_LENGTH = 6

# Prime generator, default is the golden ratio.
GENERATOR = 1.618033988749894848


# Generates next prime from supplied `base` and `n`.
# The default `gen` is set to the golden ratio, golden primes.
def prime(base, n, gen=GENERATOR):
    return next_prime(int(base ** n * gen))


## Base encode number
# General encoder. Encodes `num` with `base` and `alphabet`
def base_encode(num, alphabet):
    if num <= 0:
        raise ValueError('Number must be greater than zero.')
    base = len(alphabet)
    if len(alphabet) != base:
        raise ValueError('The length of the supplied alphabet does '
                         'not match the given base.')
    key = []
    while num > 0:
        num, c = divmod(num, base)
        key.append(alphabet[c])
    return ''.join(reversed(key))


## Base decode key
# General decoder. Decodes `key` with `base` and `alphabet`
def base_decode(key, alphabet):
    key = reversed(key)
    base = len(alphabet)
    return sum([alphabet.index(c) * base ** i for i, c in enumerate(key)])


## Base hash number to x length
# General hasher. Hashes `num` with `length` and `base`
def base_hash(num, length, alphabet):
    base = len(alphabet)
    if num > (base ** length - 1):
        raise ValueError('Number is too large for given length. '
                         'Maximum is {b}^{l} - 1.'.format(b=base, l=length))
    num = num * prime(base, length) % base ** length
    return base_encode(num, alphabet)


## Base unhash key
# General unhasher. Unhashes `key` with `base` and `alphabet`
def base_unhash(key, alphabet):
    length = len(key)
    base = len(alphabet)
    m = base ** length
    return base_decode(key, alphabet) * invmul(prime(base, length), m) % m


## Base maximum of given `length`
# General maximum. Returns maximum number of `base` and `length`
def base_maximum(base, length):
    return base ** length - 1
