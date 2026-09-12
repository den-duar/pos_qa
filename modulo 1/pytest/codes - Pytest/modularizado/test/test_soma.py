import pytest
from src.soma import soma

def test_soma_positivos():
    assert soma(1, 2, 3) == 6

def test_soma_tipos_invalidos():
    with pytest.raises(TypeError):
        soma(1, 2.5, 3)

def test_soma_nenhum_numero():
    with pytest.raises(ValueError):
        soma()

def test_soma_negativos():
    assert soma(-1, -2, -3) == -6

def test_soma_misturados():
    assert soma(-1, 2, -3) == -2