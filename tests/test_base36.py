from nose.tools import raises

from basehash import base36


bh36 = base36()
bh6 = base36(6)
bh10 = base36(10)


def test_base36_encode_with_1234567890_KF12OI():
    assert bh36.encode(1234567890) == 'KF12OI'


def test_base36_decode_with_KF12OI_1234567890():
    assert bh36.decode('KF12OI') == 1234567890


def test_base36_hash_with_1234567890_10_FT9Q9O71KI():
    assert bh10.hash(1234567890) == 'FT9Q9O71KI'


def test_base36_unhash_with_FT9Q9O71KI_1234567890():
    assert bh10.unhash('FT9Q9O71KI') == 1234567890


def test_base36_maximum_value_with_6_2176782335():
    assert bh6.maximum == 2176782335


@raises(ValueError)
def test_base36_hash_fail_with_2176782336_6():
    assert bh6.hash(2176782336)
