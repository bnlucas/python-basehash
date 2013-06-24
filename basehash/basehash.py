# Default hash key length
HASH_LENGTH = 6

# Generates next prime from supplied `base` and `n`.
# The default `ratio` is set to the golden ratio, golden primes.
def prime(base, n, ratio=1.618033988749894848):
	def next_prime(num):
		def is_prime(x):
			if x == 2:
				return True
			if not(x & 1):
				return False
			return pow(2, x-1, x) == 1
		if (num % 2 == 0) and (num != 2):
			num += 1
		while True:
			if is_prime(num):
				break
			num += 2
		return num
	return next_prime(int(base ** n * ratio))


# Get the multiplicative inverse of given prime and modulus.
def mulinv(x, mod):
	if mod <= 0:
		raise ValueError('Modulus must be greater than zero.')
	a = abs(x)
	b = mod
	c = f = 1
	d = e = 0
	while b > 0:
		q, r = divmod(a, b)
		g = c - q * d
		h = e - q * f
		a = b
		b = r
		c = d
		d = g
		e = f
		f = h
	if a != 1:
		raise ValueError('{x} has no multiplicative '
			'inverse modulo {m}'.format(x=x, m=mod))
	return c * -1 if x < 0 else c * 1


## Base encode number
# General encoder. Encodes `num` with `base` and `alphabet`
def base_encode(num, base, alphabet):
	if num <= 0:
		raise ValueError('Number must be greater than zero.')
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
def base_decode(key, base, alphabet):
	key = reversed(key)
	return sum([alphabet.index(c) * base ** i for i, c in enumerate(key)])


## Base hash number to x length
# General hasher. Hashes `num` with `length` and `base`
def base_hash(num, length, base, alphabet):
	if num > (base ** length - 1):
		raise ValueError('Number is too large for given length. '
			'Maximum is {base}^length - 1'.format(base=base))
	num = num * prime(base, length) % base ** length
	return base_encode(num, base, alphabet)


## Base unhash key
# General unhasher. Unhashes `key` with `base` and `alphabet`
def base_unhash(key, base, alphabet):
	length = len(key)
	m = base ** length
	return base_decode(key, base, alphabet) * mulinv(prime(base, length), m) % m


## Base maximum of given `length`
# General maximum. Returns maximum number of `base` and `length`
def base_maximum(base, length):
	return base ** length - 1
