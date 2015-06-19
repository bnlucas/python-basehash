from nose.tools import raises

from basehash.primes import *


def test_modinv_with_2717683_mod_4():
    modinv(2717683, 4)


@raises(ValueError)
def test_modinv_with_200_mod_2():
    modinv(200, 2)


def test_isqrt_with_2717683():
    assert isqrt(2717683) == 1648


@raises(ValueError)
def test_isqrt_with_neg_1():
    isqrt(-1)


def test_is_square_with_20():
    assert not is_square(20)


def test_is_square_with_25():
    assert is_square(25)


def test_factor_with_21_and_2():
    assert factor(21, 2) == (2, 5)


def test_jacobi_with_5_and_2717683():
    assert jacobi(5, 2717683) == -1


@raises(ValueError)
def test_jacobi_with_5_and_2717684():
    jacobi(5, 2717684)


def test_selfridge_with_2717683():
    assert selfridge(2717683) == (5, 1, -1)


@raises(ValueError)
def test_selfridge_with_2717684():
    selfridge(2717684)


def test_lucas_sequence_with_2717683_0_2_1_1_5_neg_1_1358842():
    assert lucas_sequence(2717683, 0, 2, 1, 1, 5, -1, 1358842) == (0, 2717681, 2717682)


def test_strong_pseudoprime_with_3_and_2():
    assert strong_pseudoprime(3, 2)


def test_strong_pseudoprime_with_4_and_3():
    assert not strong_pseudoprime(4, 3)


def test_lucas_pseudoprime_with_2717683():
    assert lucas_pseudoprime(2717683)


def test_lucas_pseudoprime_with_2717684():
    assert not lucas_pseudoprime(2717684)


def test_strong_lucas_pseudoprime_with_2717683():
    assert strong_lucas_pseudoprime(2717683)


def test_strong_lucas_pseudoprime_with_2717684():
    assert not strong_lucas_pseudoprime(2717684)


def test_baillie_psw_with_2717683():
    assert baillie_psw(2717683)


def test_baillie_psw_with_2717684():
    assert not baillie_psw(2717684)


def test_next_prime_with_2717711():
    assert next_prime(2717683) == 2717711
