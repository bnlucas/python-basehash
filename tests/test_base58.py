from nose.tools import raises

from basehash import base58


def test_base58_encode():
    assert base58.encode(1234567890) == '2t6V2H'


def test_base58_decode():
    assert base58.decode('2t6V2H') == 1234567890


def test_base58_hash():
    assert base58.hash(1234567890, 10) == 'SUcKRGPB1j'


def test_base58_unhash():
    assert base58.unhash('SUcKRGPB1j') == 1234567890


def test_base58_maximum():
    assert base58.maximum(6) == 38068692543


@raises(ValueError)
def test_base58_hash_fail():
    assert base58.hash(38068692544, 6)
