from basehash import *
from basehash.base import HASH_LENGTH

# Base encode an integer/long
print base36.encode(200)
print base56.encode(200)
print base58.encode(200)
print base62.encode(200)
print base94.encode(200)

# Base decode encoded string.
print base36.decode('5K')
print base56.decode('5a')
print base58.decode('4T')
print base62.decode('3E')
print base94.decode('#-')

# Base hash an integer/long
# Takes an option param, length, which is defaulted to
# basehash.base.HASH_LENGTH
print base36.hash(200)
print base56.hash(200)
print base58.hash(200)
print base62.hash(200)
print base94.hash(200)

# Base unhash hashed string.
print base36.unhash('LUEREG')
print base56.unhash('byvT3s')
print base58.unhash('cCGYMV')
print base62.unhash('bcWuqW')
print base94.unhash('Z$_P7y')

# Get maximum number for hashing by `length`
print base36.maximum(HASH_LENGTH)
print base56.maximum(10)
print base58.maximum()
print base62.maximum(16)
print base94.maximum(HASH_LENGTH)
