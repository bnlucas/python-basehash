from .primes import modinv, next_prime
from .version import __version__

__all__ = ('base', 'base36', 'base52', 'base56', 'base58', 'base62', 'base94')


HASH_LENGTH = 6

GENERATOR = 1.618033988749894848

BASE36 = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
BASE52 = '0123456789BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz'
BASE56 = '23456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnpqrstuvwxyz'
BASE58 = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'
BASE62 = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
BASE94 = ('!"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ'
          '[\]^_`abcdefghijklmnopqrstuvwxyz{|}~')


class base(object):

    def __init__(self, alphabet, length=HASH_LENGTH, generator=GENERATOR):
        if len(set(alphabet)) != len(alphabet):
            raise ValueError('Supplied alphabet cannot contain duplicates.')

        self.alphabet = tuple(alphabet)
        self.base = len(alphabet)
        self.length = length
        self.generator = generator
        self.maximum = self.base ** self.length - 1
        self.prime = next_prime(int((self.maximum + 1) * self.generator))

    def encode(self, n):
        n = int(n)
        
        if n < 0:
            raise ValueError('Negative integer provided.')
        elif n == 0:
            return self.alphabet[0]

        key = []

        while n > 0:
            n, c = divmod(n, self.base)
            key.append(self.alphabet[c])

        key = reversed(key)

        return ''.join(key)

    def decode(self, key):
        key = reversed(key)
        return sum(self.alphabet.index(c) * self.base ** i
                    for i, c in enumerate(key))

    def hash(self, n):
        n = int(n)

        if n == 0:
            return ''.rjust(self.length, self.alphabet[0])

        if n > self.maximum:
            raise ValueError('Integer provided is too large for given length.')

        n = n * self.prime % self.base ** self.length

        return self.encode(n).rjust(self.length, self.alphabet[0])

    def unhash(self, key):
        if len(key) != self.length:
            raise ValueError('Key length does not match base length.')

        if key == ''.rjust(self.length, self.alphabet[0]):
            return 0

        m = self.maximum + 1

        return self.decode(key) * modinv(self.prime, m) % m


class base36(base):

    def __init__(self, length=HASH_LENGTH, generator=GENERATOR):
        super(base36, self).__init__(BASE36, length, generator)


class base52(base):

    def __init__(self, length=HASH_LENGTH, generator=GENERATOR):
        super(base52, self).__init__(BASE52, length, generator)


class base56(base):

    def __init__(self, length=HASH_LENGTH, generator=GENERATOR):
        super(base56, self).__init__(BASE56, length, generator)


class base58(base):

    def __init__(self, length=HASH_LENGTH, generator=GENERATOR):
        super(base58, self).__init__(BASE58, length, generator)


class base62(base):

    def __init__(self, length=HASH_LENGTH, generator=GENERATOR):
        super(base62, self).__init__(BASE62, length, generator)


class base94(base):

    def __init__(self, length=HASH_LENGTH, generator=GENERATOR):
        super(base94, self).__init__(BASE94, length, generator)
