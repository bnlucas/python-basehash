from nose.tools import raises

from basehash import base


basex = base('0SYv2xCbfhzGK4AW8E6QUpnjdtMOIlr')


def test_custom_encode_with_1234567890_SKvdr0U():
    assert basex.encode(1234567890) == 'SKvdr0U'


def test_custom_decode_with_SKvdr0U_1234567890():
    assert basex.decode('SKvdr0U') == 1234567890


def test_custom_hash_with_1234567890_10_4QxzxC4CtG():
    assert basex.hash(1234567890, 10) == '4QxzxC4CtG'


def test_custom_unhash_with_4QxzxC4CtG_1234567890():
    assert basex.unhash('4QxzxC4CtG') == 1234567890


def test_custom_maximum_value_with_6_887503680():
    assert basex.maximum_value(6) == 887503680


@raises(ValueError)
def test_custom_hash_fail_with_887503681_6():
    assert basex.hash(887503681, 6)
