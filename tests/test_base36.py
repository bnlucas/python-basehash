from nose.tools import raises

from basehash import base36


base36 = base36()


def test_base36_encode_with_1234567890_KF12OI():
    assert base36.encode(1234567890) == 'KF12OI'


def test_base36_decode_with_KF12OI_1234567890():
    assert base36.decode('KF12OI') == 1234567890


def test_base36_hash_with_1234567890_10_FT9Q9O71KI():
    assert base36.hash(1234567890, 10) == 'FT9Q9O71KI'


def test_base36_unhash_with_FT9Q9O71KI_1234567890():
    assert base36.unhash('FT9Q9O71KI') == 1234567890


def test_base36_maximum_value_with_6_2176782335():
    assert base36.maximum_value(6) == 2176782335


@raises(ValueError)
def test_base36_hash_fail_with_2176782336_6():
    assert base36.hash(2176782336, 6)
