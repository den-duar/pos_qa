import pytest
from src.multiplicacao import multiplicacao

def test_multiplicacao_positivos():
    assert multiplicacao(2, 3, 4) == 24

def test_multiplicacao_tipos_invalidos():
    with pytest.raises(TypeError):
        multiplicacao(2, 3.5, 4)

def test_multiplicacao_nenhum_numero():
    assert multiplicacao() == 0

def test_multiplicacao_negativos():
    assert multiplicacao(-2, -3, -4) == -24

def test_multiplicacao_misturados_resultado_positivo():
    assert multiplicacao(-2, 3, -4) == 24

def test_multiplicacao_misturados_resultado_negativo():
    assert multiplicacao(-2, 3, 4) == -24