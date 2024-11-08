from decouple import config, Csv


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in config("ALLOWED_EXTENSIONS", cast=Csv())