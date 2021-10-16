from http import HTTPStatus

import pytest
from fastapi.testclient import TestClient

from api_pedidos.api import app


@pytest.fixture
def cliente():
    return TestClient(app)


def test_quando_verificar_integridade_devo_ter_como_retorno_codigo_de_status_200(
        cliente):
    cliente = TestClient(app)
    resposta = cliente.get("/healthcheck")
    assert resposta.status_code == HTTPStatus.OK


def test_quando_verificar_integridade_formato_de_retorno_deve_ser_json(
        cliente):
    cliente = TestClient(app)
    resposta = cliente.get("/healthcheck")
    assert resposta.headers["Content-Type"] == "application/json"


def test_quando_verificar_integridade_deve_conter_informacoes(cliente):
    cliente = TestClient(app)
    resposta = cliente.get("/healthcheck")
    assert resposta.json() == {
        "status": "ok"
    }
