import pytest
from src.soma import soma

def test_soma_positivos():
    assert soma(1, 2, 3) == 6

def test_soma_negativos():
    with pytest.raises(ValueError):
        soma(1, -2, 3)

def test_soma_tipos_invalidos():
    with pytest.raises(TypeError):
        soma(1, 2.5, 3)