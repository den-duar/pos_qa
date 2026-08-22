import pytest
from src.divisao import divisao

def test_divisao_positivos():
    assert divisao(10, 2) == 5 

def test_divisao_por_zero():
    with pytest.raises(ZeroDivisionError):
        divisao(10, 0)

def test_divisao_tipos_invalidos():
    with pytest.raises(TypeError):
        divisao(10, "2")

def test_divisao_nenhum_numero():
    with pytest.raises(ValueError):
        divisao()

def test_divisao_negativos():
    assert divisao(-10, -2) == 5    

def test_divisao_misturados_resultado_negativo():
    assert divisao(10, -2) == -5

def test_divisao_tipos_invalidos():
    with pytest.raises(TypeError):
        divisao(10, '2.5')

def test_divisao_float():
    assert divisao(10, 2.5) == 4.0