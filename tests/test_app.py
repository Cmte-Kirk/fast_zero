from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_zero.app import app


def test_read_root_deve_retornar_ok_e_ola_mundo():
    cliente = TestClient(app)  # Arrange (organização)

    response = cliente.get('/')  # Act (acao)

    # Assert (verificacao)
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Olá mundo!'}
