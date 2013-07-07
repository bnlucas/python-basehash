from nose.tools import raises

from basehash import base52


base52 = base52()


def test_base52_encode_with_1234567890_3DrByB():
    assert base52.encode(1234567890) == '3DrByB'


def test_base52_decode_with_3DrByB_123456789():
    assert base52.decode('3DrByB') == 1234567890


def test_base52_hash_with_1234567890_10_QqhsMHZ7Pf():
    assert base52.hash(1234567890, 10) == 'QqhsMHZ7Pf'


def test_base52_unhash_with_QqhsMHZ7Pf_1234567890():
    assert base52.unhash('QqhsMHZ7Pf') == 1234567890


def test_base52_maximum_value_with_6_19770609663():
    assert base52.maximum_value(6) == 19770609663


@raises(ValueError)
def test_base52_hash_fail_with_19770609664_6():
    assert base52.hash(19770609664, 6)
