from nose.tools import raises

from basehash import base56


base56 = base56()


def test_base56_encode_with_1234567890_4FXvzC():
    assert base56.encode(1234567890) == '4FXvzC'


def test_base56_decode_with_4FXvzC_1234567890():
    assert base56.decode('4FXvzC') == 1234567890


def test_base56_hash_with_1234567890_10_SbTrfJ3VLu():
    assert base56.hash(1234567890, 10) == 'SbTrfJ3VLu'


def test_base56_unhash_with_SbTrfJ3VLu_1234567890():
    assert base56.unhash('SbTrfJ3VLu') == 1234567890


def test_base56_maximum_value_with_6_30840979455():
    assert base56.maximum_value(6) == 30840979455


@raises(ValueError)
def test_base56_hash_fail_with_30840979456_6():
    assert base56.hash(30840979456, 6)
