from basehash import HASH_LENGTH, base36, base52, base56, base58, base62, base94

base36 = base36()
base52 = base52()
base56 = base56()
base58 = base58()
base62 = base62()
base94 = base94()


# Base encode an integer/long
print base36.encode(200)
print base52.encode(200)
print base56.encode(200)
print base58.encode(200)
print base62.encode(200)
print base94.encode(200)

# Base decode encoded string.
print base36.decode('5K')
print base52.decode('3r')
print base56.decode('5a')
print base58.decode('4T')
print base62.decode('3E')
print base94.decode('#-')

# Base hash an integer/long
# Takes an option param, length, which is defaulted to
# basehash.base.HASH_LENGTH
print base36.hash(200)
print base52.hash(200)
print base56.hash(200)
print base58.hash(200)
print base62.hash(200)
print base94.hash(200)

# Base unhash hashed string.
print base36.unhash('LUEREG')
print base52.unhash('bXmcJ8')
print base56.unhash('byvT3s')
print base58.unhash('cCGYMV')
print base62.unhash('bcWuqW')
print base94.unhash('Z$_P7y')

# Get maximum number for hashing by `length`
print base36.maximum(HASH_LENGTH)
print base52.maximum(25)
print base56.maximum(10)
print base58.maximum()
print base62.maximum(4)
print base94.maximum(50)
