
import pytest

from calculadora import soma, subtracao, multiplicacao, divisao

def test_soma():
    assert soma(4,9) == 13
    assert soma(12,4) == 16
    assert soma(9,6) == 15
    assert soma(4.2,2.9) == 7.1
    assert soma(4,-6) == -2
    assert soma(6,-4) == 2
    assert soma(-2,-2.2) == -4.2
    assert soma((4/2),(2/2)) == 6/2
    assert soma((4/2),(2/3)) == 16/6

def test_subtracao():
    assert subtracao(4,9) == -5
    assert subtracao(12,4) == 8
    assert subtracao(9,6) == 3
    assert subtracao(4,-6) == 10
    assert subtracao(6,-4) == 10
    assert subtracao((4/2),(2/2)) == 2/2

def test_multiplicacao():
    assert multiplicacao(4,9) == 36
    assert multiplicacao(12,4) == 48
    assert multiplicacao(9,6) == 54
    assert multiplicacao(4.2,2.9) == 12.18


def test_divisao():
    assert divisao(12,4) == 3
    assert divisao(9,3) == 3
    assert divisao(121,11) == 11
