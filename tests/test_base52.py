from nose.tools import raises

from basehash import base52


def test_base52_encode():
    assert base52.encode(1234567890) == '3DrByB'


def test_base52_decode():
    assert base52.decode('3DrByB') == 1234567890


def test_base52_hash():
    assert base52.hash(1234567890, 10) == 'QqhsMHZ7Pf'


def test_base52_unhash():
    assert base52.unhash('QqhsMHZ7Pf') == 1234567890


def test_base52_maximum():
    assert base52.maximum(6) == 19770609663


@raises(ValueError)
def test_base52_hash_fail():
    assert base52.hash(19770609664, 6)
