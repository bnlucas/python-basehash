from base import *

BASE58 = tuple('123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz')

def encode(num):
	return base_encode(num, 58, BASE58)

def decode(key):
	return base_decode(key, 58, BASE58)

def hash(num, length=HASH_LENGTH):
	return base_hash(num, length, 58, BASE58)

def unhash(key):
	return base_unhash(key, 58, BASE58)

def maximum(length=HASH_LENGTH):
	return base_maximum(58, length)