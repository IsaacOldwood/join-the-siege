from fastapi import FastAPI, UploadFile, HTTPException

from src.classifier import classify_file


app = FastAPI()

ALLOWED_EXTENSIONS = {"pdf", "png", "jpg"}


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


@app.post("/classify_file")
def classify_file_route(file: UploadFile):
    if file.filename == "":
        raise HTTPException(status_code=400, detail="No selected file")

    if not allowed_file(file.filename):
        raise HTTPException(status_code=400, detail="File extension not allowed")

    file_class = classify_file(file)
    return {"file_class": file_class}
