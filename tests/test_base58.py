from nose.tools import raises

from basehash import base58


bh58 = base58()
bh6 = base58(6)
bh10 = base58(10)


def test_base58_encode_with_1234567890_2t6V2H():
    assert bh58.encode(1234567890) == '2t6V2H'


def test_base58_decode_with_2t6V2H_1234567890():
    assert bh58.decode('2t6V2H') == 1234567890


def test_base58_hash_with_1234567890_10_SUcKRGPB1j():
    assert bh10.hash(1234567890) == 'SUcKRGPB1j'


def test_base58_unhash_with_SUcKRGPB1j_1234567890():
    assert bh10.unhash('SUcKRGPB1j') == 1234567890


def test_base58_maximum_value_with_6_38068692543():
    assert bh6.maximum == 38068692543


@raises(ValueError)
def test_base58_hash_fail_with_38068692544_6():
    assert bh6.hash(38068692544)
