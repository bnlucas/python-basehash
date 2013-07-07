from nose.tools import raises

from basehash import base58


base58 = base58()


def test_base58_encode_with_1234567890_2t6V2H():
    assert base58.encode(1234567890) == '2t6V2H'


def test_base58_decode_with_2t6V2H_1234567890():
    assert base58.decode('2t6V2H') == 1234567890


def test_base58_hash_with_1234567890_10_SUcKRGPB1j():
    assert base58.hash(1234567890, 10) == 'SUcKRGPB1j'


def test_base58_unhash_with_SUcKRGPB1j_1234567890():
    assert base58.unhash('SUcKRGPB1j') == 1234567890


def test_base58_maximum_value_with_6_38068692543():
    assert base58.maximum_value(6) == 38068692543


@raises(ValueError)
def test_base58_hash_fail_with_38068692544_6():
    assert base58.hash(38068692544, 6)
