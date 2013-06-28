from nose.tools import raises

from basehash import base36


def test_base36_encode():
    assert base36.encode(1234567890) == 'KF12OI'


def test_base36_decode():
    assert base36.decode('KF12OI') == 1234567890


def test_base36_hash():
    assert base36.hash(1234567890, 10) == 'FT9Q9O71KI'


def test_base36_unhash():
    assert base36.unhash('FT9Q9O71KI') == 1234567890


def test_base36_maximum():
    assert base36.maximum(6) == 2176782335


@raises(ValueError)
def test_base36_hash_fail():
    assert base36.hash(2176782336, 6)
