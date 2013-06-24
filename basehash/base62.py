from base import *

BASE62 = tuple('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz')

def encode(num):
	return base_encode(num, 62, BASE62)

def decode(key):
	return base_decode(key, 62, BASE62)

def hash(num, length=HASH_LENGTH):
	return base_hash(num, length, 62, BASE62)

def unhash(key):
	return base_unhash(key, 62, BASE62)

def maximum(length=HASH_LENGTH):
	return base_maximum(62, length)