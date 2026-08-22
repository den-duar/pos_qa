import pytest
from src.subtracao import subtracao

def test_subtracao_positivos():
    assert subtracao(10, 5, 2) == 3

def test_subtracao_tipos_invalidos():
    with pytest.raises(TypeError):
        subtracao(10, 5.5, 2)

def test_subtracao_nenhum_numero():
    with pytest.raises(ValueError):
        subtracao()

def test_subtracao_resultado_negativo():
    assert subtracao(5, 10) == -5

def test_subtracao_misturados():
    assert subtracao(10, -5, 2) == 13

