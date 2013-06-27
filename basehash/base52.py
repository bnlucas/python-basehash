from base import *

BASE52 = tuple('0123456789BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz')

def encode(num):
<<<<<<< HEAD
  return base_encode(num, 52, BASE52)

def decode(key):
	return base_decode(key, 52, BASE52)

def hash(num, length=HASH_LENGTH):
	return base_hash(num, length, 52, BASE52)

def unhash(key):
	return base_unhash(key, 52, BASE52)

def maximum(length=HASH_LENGTH):
	return base_maximum(52, length)
=======
	return base_encode(num, BASE52)

def decode(key):
	return base_decode(key, BASE52)

def hash(num, length=HASH_LENGTH):
	return base_hash(num, length, BASE52)

def unhash(key):
	return base_unhash(key, BASE52)

def maximum(length=HASH_LENGTH):
	return base_maximum(52, length)
>>>>>>> Overhaul.
