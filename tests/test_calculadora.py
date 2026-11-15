# tests/test_calculadora.py
import pytest
from app.calculadora import sumar, restar, multiplicar, dividir


@pytest.mark.parametrize(
    "operacion, a, b, esperado",
    [
        pytest.param(sumar, 2, 3, 5, id="sumar-positivos"),
        pytest.param(sumar, -1, 1, 0, id="sumar-signos-mixtos"),
        pytest.param(sumar, 0, 0, 0, id="sumar-ceros"),
        pytest.param(sumar, -6, -3, -9, id="sumar-dos-negativos"),
        pytest.param(restar, 5, 2, 3, id="restar-positivos"),
        pytest.param(restar, 1, -1, 2, id="restar-signos-mixtos"),
        pytest.param(restar, 0, 0, 0, id="restar-ceros"),
        pytest.param(restar, -6, -3, -3, id="restar-dos-negativos"),
        pytest.param(multiplicar, 2, 3, 6, id="multiplicar-positivos"),
        pytest.param(multiplicar, -1, 5, -5, id="multiplicar-signos-mixtos"),
        pytest.param(multiplicar, 0, 10, 0, id="multiplicar-cero"),
        pytest.param(multiplicar, -6, -3, 18, id="multiplicar-dos-negativos"),
        pytest.param(dividir, 10, 2, 5.0, id="dividir-positivos"),
        pytest.param(dividir, 5, -1, -5.0, id="dividir-signos-mixtos"),
        pytest.param(dividir, -6, -3, 2.0, id="dividir-dos-negativos"),
    ],
)
def test_operaciones_con_enteros(operacion, a, b, esperado):
    assert operacion(a, b) == esperado


def test_dividir_por_cero():
    with pytest.raises(ZeroDivisionError):
        dividir(1, 0)


@pytest.mark.parametrize(
    "operacion, a, b, esperado",
    [
        pytest.param(sumar, 0.1, 0.2, 0.3, id="sumar"),
        pytest.param(restar, 0.3, 0.1, 0.2, id="restar"),
        pytest.param(multiplicar, 0.1, 0.2, 0.02, id="multiplicar"),
        pytest.param(dividir, 0.3, 0.1, 3.0, id="dividir"),
    ],
)
def test_operaciones_con_decimales(operacion, a, b, esperado):
    assert operacion(a, b) == pytest.approx(esperado)
