from src.classifiers.contents import FileContentsClassifier
from fastapi import UploadFile
from io import BytesIO
import pytest


@pytest.mark.asyncio
async def test_filename_classifier():
    classifier = FileContentsClassifier(
        UploadFile(filename="a_doc.csv", file=BytesIO(b"invoice,,total,1,2,3"))
    )

    result = await classifier.classify()

    assert result == "invoice"
