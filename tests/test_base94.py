from nose.tools import raises

from basehash import base94


def test_base94_encode():
    assert base94.encode(1234567890) == '0mE5{'


def test_base94_decode():
    assert base94.decode('0mE5{') == 1234567890


def test_base94_hash():
    assert base94.hash(1234567890, 10) == 'J<-l50[.:%'


def test_base94_unhash():
    assert base94.unhash('J<-l50[.:%') == 1234567890


def test_base94_maximum():
    assert base94.maximum(6) == 689869781055


@raises(ValueError)
def test_base94_hash_fail():
    assert base94.hash(689869781056, 6)
