from nose.tools import raises

from basehash import base52


bh52 = base52()
bh6 = base52(6)
bh10 = base52(10)


def test_base52_encode_with_1234567890_3DrByB():
    assert bh52.encode(1234567890) == '3DrByB'


def test_base52_decode_with_3DrByB_123456789():
    assert bh52.decode('3DrByB') == 1234567890


def test_base52_hash_with_1234567890_10_QqhsMHZ7Pf():
    assert bh10.hash(1234567890) == 'QqhsMHZ7Pf'


def test_base52_unhash_with_QqhsMHZ7Pf_1234567890():
    assert bh10.unhash('QqhsMHZ7Pf') == 1234567890


def test_base52_maximum_value_with_6_19770609663():
    assert bh6.maximum == 19770609663


@raises(ValueError)
def test_base52_hash_fail_with_19770609664_6():
    assert bh6.hash(19770609664)
