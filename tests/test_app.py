from io import BytesIO

import pytest
from src.app import app, allowed_file

from fastapi.testclient import TestClient


@pytest.fixture
def test_client():
    return TestClient(app)


@pytest.mark.parametrize(
    "filename, expected",
    [
        ("file.pdf", True),
        ("file.png", True),
        ("file.jpg", True),
        ("file.txt", False),
        ("file", False),
    ],
)
def test_allowed_file(filename, expected, app_settings):
    app_settings({"ALLOWED_EXTENSIONS": "pdf,png,jpg"})

    result = allowed_file(filename)

    assert result == expected


def test_no_file_in_request(test_client):
    """No file gets caught by the request validation"""
    response = test_client.post("/file-classification")
    assert response.status_code == 422


def test_no_selected_file(test_client):
    """No filename gets caught by the request validation"""
    data = {"file": ("", BytesIO(b""))}  # Empty filename
    response = test_client.post("/file-classification", files=data)
    assert response.status_code == 422


def test_not_supported_file_type(test_client, app_settings):
    app_settings({"ALLOWED_EXTENSIONS": "pdf,png,jpg"})
    data = {"file": ("test.xyv", BytesIO(b"some content"))}

    response = test_client.post("/file-classification", files=data)

    assert response.status_code == 400
    assert "unsupported" in response.json()["detail"]


def test_success(test_client, mocker, app_settings):
    app_settings({"ALLOWED_EXTENSIONS": "pdf,png,jpg"})
    mocker.patch("src.services.classify.classify_file", return_value="test_class")

    data = {"file": ("file.pdf", BytesIO(b"dummy content"))}
    response = test_client.post("/file-classification", files=data)
    assert response.status_code == 200
    assert response.json() == {"file_class": "test_class"}


def test_csv_invoice(test_client, app_settings):
    app_settings({"ALLOWED_EXTENSIONS": "csv"})
    data = {"file": ("a_doc.csv", BytesIO(b"invoice,total\n1,2"))}

    response = test_client.post("/file-classification", files=data)

    assert response.status_code == 200
    assert response.json() == {"file_class": "invoice"}
