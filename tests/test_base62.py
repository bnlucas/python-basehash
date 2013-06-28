from nose.tools import raises

from basehash import base62


def test_base62_encode():
    assert base62.encode(1234567890) == '1LY7VK'


def test_base62_decode():
    assert base62.decode('1LY7VK') == 1234567890


def test_base62_hash():
    assert base62.hash(1234567890, 10) == 'RERZ0NM8Na'


def test_base62_unhash():
    assert base62.unhash('RERZ0NM8Na') == 1234567890


def test_base62_maximum():
    assert base62.maximum(6) == 56800235583


@raises(ValueError)
def test_base62_hash_fail():
    assert base62.hash(56800235584, 6)
