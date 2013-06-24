from base import *

BASE56 = tuple('23456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnpqrstuvwxyz')

def encode(num):
	return base_encode(num, 56, BASE56)

def decode(key):
	return base_decode(key, 56, BASE56)

def hash(num, length=HASH_LENGTH):
	return base_hash(num, length, 56, BASE56)

def unhash(key):
	return base_unhash(key, 56, BASE56)

def maximum(length=HASH_LENGTH):
	return base_maximum(56, length)