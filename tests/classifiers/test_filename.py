from src.classifiers.filename import FilenameClassifier
from fastapi import UploadFile
from io import BytesIO
import pytest


@pytest.mark.parametrize(
    "filename, expected",
    [
        ("drivers_license.jpg", "drivers_licence"),
        ("bank_statement.jpg", "bank_statement"),
        ("invoice.jpg", "invoice"),
        ("aiwhgbipawebg.txt", "unknown file"),
    ],
)
def test_filename_classifier(filename, expected):
    classifier = FilenameClassifier(UploadFile(filename=filename, file=BytesIO(b"")))

    result = classifier.classify()

    assert result == expected