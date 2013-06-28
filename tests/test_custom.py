from nose.tools import raises

from basehash.base import *

ALPHA = tuple('0SYv2xCbfhzGK4AW8E6QUpnjdtMOIlr')


def encode(num):
    return base_encode(num, ALPHA)


def decode(key):
    return base_decode(key, ALPHA)


def hash(num, length=HASH_LENGTH):
    return base_hash(num, length, ALPHA)


def unhash(key):
    return base_unhash(key, ALPHA)


def maximum(length=HASH_LENGTH):
    return base_maximum(len(ALPHA), length)


def test_custom_encode():
    assert encode(1234567890) == 'SKvdr0U'


def test_custom_decode():
    assert decode('SKvdr0U') == 1234567890


def test_custom_hash():
    assert hash(1234567890, 10) == '4QxzxC4CtG'


def test_custom_unhash():
    assert unhash('4QxzxC4CtG') == 1234567890


def test_custom_maximum():
    assert maximum(6) == 887503680


@raises(ValueError)
def test_custom_hash_fail():
    assert hash(887503681, 6)
