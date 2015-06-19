from nose.tools import raises

from basehash import base


bhx = base('0SYv2xCbfhzGK4AW8E6QUpnjdtMOIlr')
bh6 = base('0SYv2xCbfhzGK4AW8E6QUpnjdtMOIlr', 6)
bh10 = base('0SYv2xCbfhzGK4AW8E6QUpnjdtMOIlr', 10)


def test_custom_encode_with_1234567890_SKvdr0U():
    assert bhx.encode(1234567890) == 'SKvdr0U'


def test_custom_decode_with_SKvdr0U_1234567890():
    assert bhx.decode('SKvdr0U') == 1234567890


def test_custom_hash_with_1234567890_10_4QxzxC4CtG():
    assert bh10.hash(1234567890) == '4QxzxC4CtG'


def test_custom_unhash_with_4QxzxC4CtG_1234567890():
    assert bh10.unhash('4QxzxC4CtG') == 1234567890


def test_custom_maximum_value_with_6_887503680():
    assert bh6.maximum == 887503680


@raises(ValueError)
def test_custom_hash_fail_with_887503681_6():
    assert bh6.hash(887503681)
