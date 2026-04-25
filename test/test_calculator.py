import pytest
from app.calculator import sumar, restar, multiplicar, dividir

# CASO EXITOSO
def test_suma_exitosa():
    """TC01 - Suma exitosa (caso feliz)"""
    assert sumar(5, 3) == 8

# CASO DE ERROR
def test_division_por_cero():
    """TC02 - División por cero (caso de error)"""
    with pytest.raises(ZeroDivisionError):
        dividir(10, 0)

# CASO BORDE
def test_resta_numeros_negativos():
    """TC03 - Resta con números negativos (caso borde)"""
    assert restar(-5, 3) == -8

# CASO EXITOSO
def test_multiplicacion_por_negativo():
    """TC04 - Multiplicación con número negativo"""
    assert multiplicar(4, -2) == -8
