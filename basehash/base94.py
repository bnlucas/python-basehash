from base import *

BASE94 = tuple('!"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	'[\]^_`abcdefghijklmnopqrstuvwxyz{|}~')

def encode(num):
	return base_encode(num, 94, BASE94)

def decode(key):
	return base_decode(key, 94, BASE94)

def hash(num, length=HASH_LENGTH):
	return base_hash(num, length, 94, BASE94)

def unhash(key):
	return base_unhash(key, 94, BASE94)

def maximum(length=HASH_LENGTH):
	return base_maximum(94, length)