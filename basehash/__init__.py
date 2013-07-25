from random import shuffle

from primes import invmul, next_prime

__all__ = ('base', 'base36', 'base52', 'base56', 'base58', 'base62', 'base94',
           'generate_alphabet')

__version__ = '2.1.0'


HASH_LENGTH = 6

GENERATOR = 1.618033988749894848

BASE36 = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
BASE52 = '0123456789BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz'
BASE56 = '23456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnpqrstuvwxyz'
BASE58 = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'
BASE62 = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
BASE94 = ('!"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ'
          '[\]^_`abcdefghijklmnopqrstuvwxyz{|}~')


def generate_alphabet(alphabet, randomize=10):
    alphalist = list(alphabet)
    for i in xrange(randomize):
        shuffle(alphalist)
    return ''.join(alphalist)


class InvalidAlphabet(Exception):

    def __init__(self, alphabet):
        if isinstance(alphabet, ('list', 'tuple')):
            alphabet = ''.join(alphabet)
        super(InvalidAlphabet, self).__init__(
            '{a} contains duplicate characters.'.format(a=alphabet))


class base(object):

    def __init__(self, alphabet, length=HASH_LENGTH, generator=GENERATOR):
        if len(set(alphabet)) != len(alphabet):
            raise InvalidAlphabet(alphabet)
        self.alphabet = tuple(alphabet)
        self.base = len(self.alphabet)
        self.hash_length = length
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

    def hash(self, num, length=None):
        if length is None:
            length = self.hash_length

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

    def maximum(self, length=None):
        if length is None:
            length = self.hash_length

        return self.maximum_value(length)

    def maximum_value(self, length=None):
        if length is None:
            length = self.hash_length

        length = int(length)
        return self.base ** length - 1

    def prime(self, num):
        num = int(num)
        return next_prime(int(self.base ** num * self.generator))


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
