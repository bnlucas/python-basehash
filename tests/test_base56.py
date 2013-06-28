from nose.tools import raises

from basehash import base56


def test_base56_encode():
    assert base56.encode(1234567890) == '4FXvzC'


def test_base56_decode():
    assert base56.decode('4FXvzC') == 1234567890


def test_base56_hash():
    assert base56.hash(1234567890, 10) == 'SbTrfJ3VLu'


def test_base56_unhash():
    assert base56.unhash('SbTrfJ3VLu') == 1234567890


def test_base56_maximum():
    assert base56.maximum(6) == 30840979455


@raises(ValueError)
def test_base56_hash_fail():
    assert base56.hash(30840979456, 6)
