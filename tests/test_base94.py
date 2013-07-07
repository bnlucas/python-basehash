from nose.tools import raises

from basehash import base94


base94 = base94()


def test_base94_encode_with_1234567890_0mE5():
    assert base94.encode(1234567890) == '0mE5{'


def test_base94_decode_with_0mE5_1234567890():
    assert base94.decode('0mE5{') == 1234567890


def test_base94_hash_with_1234567890_10_Jl50():
    assert base94.hash(1234567890, 10) == 'J<-l50[.:%'


def test_base94_unhash_with_Jl50_1234567890():
    assert base94.unhash('J<-l50[.:%') == 1234567890


def test_base94_maximum_value_with_6_689869781055():
    assert base94.maximum_value(6) == 689869781055


@raises(ValueError)
def test_base94_hash_fail_with_689869781056_6():
    assert base94.hash(689869781056, 6)
