from primes import invmul, next_prime

__all__ = ('base', 'base36', 'base52', 'base56', 'base58', 'base62', 'base94')

__version__ = '2.0.1.1'


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

    def __init__(self, alphabet, generator=GENERATOR):
        self.alphabet = tuple(alphabet)
        self.base = len(self.alphabet)
        self.generator = generator

    def encode(self, num):
        num = int(num)
        if num <= 0:
            raise ValueError('Number must be greater than zero.')
        key = []
        while num > 0:
            num, c = divmod(num, self.base)
            key.append(self.alphabet[c])
        return ''.join(reversed(key))

    def decode(self, key):
        key = reversed(key)
        return sum([self.alphabet.index(c) * self.base ** i
                    for i, c in enumerate(key)])

    def hash(self, num, length=HASH_LENGTH):
        num = int(num)
        if num == 0:
            return ''.rjust(length, self.alphabet[0])

        if num > (self.base ** length - 1):
            raise ValueError('Number is too large for given length. Maximum is '
                             '{b}^{l} - 1.'.format(b=self.base,
                                                   l=length))

        num = num * self.prime(length) % self.base ** length

        return self.encode(num).rjust(length, self.alphabet[0])

    def unhash(self, key):
        length = len(key)

        if key == ''.rjust(length, self.alphabet[0]):
            return 0

        m = self.base ** length
        return self.decode(key) * invmul(self.prime(length), m) % m

    def maximum(self, length=HASH_LENGTH):
        return self.maximum_value(length)

    def maximum_value(self, length=HASH_LENGTH):
        length = int(length)
        return self.base ** length - 1

    def prime(self, num):
        num = int(num)
        return next_prime(int(self.base ** num * self.generator))


class base36(base):

    def __init__(self, generator=GENERATOR):
        super(base36, self).__init__(BASE36, generator)


class base52(base):

    def __init__(self, generator=GENERATOR):
        super(base52, self).__init__(BASE52, generator)


class base56(base):

    def __init__(self, generator=GENERATOR):
        super(base56, self).__init__(BASE56, generator)


class base58(base):

    def __init__(self, generator=GENERATOR):
        super(base58, self).__init__(BASE58, generator)


class base62(base):

    def __init__(self, generator=GENERATOR):
        super(base62, self).__init__(BASE62, generator)


class base94(base):

    def __init__(self, generator=GENERATOR):
        super(base94, self).__init__(BASE94, generator)
