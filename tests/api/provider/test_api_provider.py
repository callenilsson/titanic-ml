"""Test API provider endpoints."""
from fastapi import status
from fastapi.testclient import TestClient
from titanic.api.provider.api import app

api = TestClient(app)


def test_get_predict_survival():
    """Verify API predicts survival given input parameters."""
    # setup
    query = "/titanic/survived?personClass=upper&nameTitle=Mrs&sex=female&age=28\
&siblingsSpouses=2&cabinLetter=A&cabinNumber=40&embarked=cherbourg&ticketPrice=80.2"

    # when
    response = api.get(query)

    # then
    assert response.status_code == status.HTTP_200_OK
    assert isinstance(response.json()["survived"], float)


def test_get_predict_survival2():
    """Verify API sends back unprocessable entity when input data is wrong.

    The last parameter "ticketPrice" has been set to true, which should not
    be accepted.
    """
    # setup
    query = "/titanic/survived?personClass=upper&nameTitle=Mrs&sex=female&age=28\
&siblingsSpouses=2&cabinLetter=A&cabinNumber=40&embarked=cherbourg&ticketPrice=true"

    # when
    response = api.get(query)

    # then
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
