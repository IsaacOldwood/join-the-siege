from fastapi import FastAPI, UploadFile, HTTPException

from classifiers.filename import FilenameClassifier
from src.utils import allowed_file
from src.services import classify as classify_service

app = FastAPI()


@app.post("/file-classification")
def file_classification(file: UploadFile):
    if file.filename == "":
        raise HTTPException(status_code=400, detail="No selected file")

    if not allowed_file(file.filename):
        raise HTTPException(status_code=400, detail="File extension unsupported")

    classifier = FilenameClassifier(file)
    file_class = classify_service.classify(classifier)
    
    return {"file_class": file_class}
