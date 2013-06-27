from base import *

BASE36 = tuple('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ')

def encode(num):
	return base_encode(num, BASE36)

def decode(key):
	return base_decode(key, BASE36)

def hash(num, length=HASH_LENGTH):
	return base_hash(num, length, BASE36)

def unhash(key):
	return base_unhash(key, BASE36)

def maximum(length=HASH_LENGTH):
	return base_maximum(36, length)