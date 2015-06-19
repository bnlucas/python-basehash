from nose.tools import raises

from basehash import base62


bh62 = base62()
bh6 = base62(6)
bh10 = base62(10)


def test_base62_encode_with_1234567890_1LY7VK():
    assert bh62.encode(1234567890) == '1LY7VK'


def test_base62_decode_with_1LY7VK_1234567890():
    assert bh62.decode('1LY7VK') == 1234567890


def test_base62_hash_with_1234567890_10_RERZ0NM8Na():
    assert bh10.hash(1234567890) == 'RERZ0NM8Na'


def test_base62_unhash_with_RERZ0NM8Na_1234567890():
    assert bh10.unhash('RERZ0NM8Na') == 1234567890


def test_base62_maximum_value_with_6_56800235583():
    assert bh6.maximum == 56800235583


@raises(ValueError)
def test_base62_hash_fail_with_56800235584_6():
    assert bh6.hash(56800235584)
