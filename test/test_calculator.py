import pytest
from app.calculator import sumar, restar, multiplicar, dividir

# CASO EXITOSO
def test_suma_exitosa():
    """Suma exitosa"""
    assert sumar(5, 3) == 8

# CASO DE ERROR
def test_division_por_cero():
    """División por cero"""
    with pytest.raises(ZeroDivisionError):
        dividir(10, 0)

# CASO BORDE
def test_resta_numeros_negativos():
    """Resta con números negativos"""
    assert restar(-5, 3) == -8

# CASO EXITOSO
def test_multiplicacion_por_negativo():
    """Multiplicación con número negativo"""
    assert multiplicar(4, -2) == -8
