import pytest
from src.potencia import potencia

def test_potencia_positivos():
    assert potencia(2, 3) == 8

def test_potencia_zero_expoente():
    assert potencia(5, 0) == 1

def test_potencia_zero_base():
    assert potencia(0, 5) == 0

def test_potencia_negativos():
    assert potencia(-2, 3) == -8

def test_potencia_negativo_expoente():
    assert potencia(2, -2) == 0.25

def test_potencia_tipos_invalidos():
    with pytest.raises(TypeError):
        potencia(2, "3")

def test_potencia_nenhum_numero():
    with pytest.raises(TypeError):
        potencia()