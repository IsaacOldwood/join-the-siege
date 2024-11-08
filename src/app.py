from fastapi import FastAPI, UploadFile, HTTPException

from src.utils import allowed_file
from src.services import classify as classify_service

app = FastAPI()


@app.post("/file-classification")
async def file_classification(file: UploadFile):
    """Classify a file based on its contents, filename and other attributes using our state of the art AI model."""
    if file.filename == "":
        raise HTTPException(status_code=400, detail="No selected file")

    if not allowed_file(file.filename):
        raise HTTPException(status_code=400, detail="File extension unsupported")

    file_class = await classify_service.classify_file(file)

    return {"file_class": file_class}
