from werkzeug.datastructures import FileStorage


class FilenameClassifier:
    def __init__(self, file: FileStorage):
        """Classify a file based on its name."""
        self.file = file

    async def classify(self):
        """Classify the file based on its name."""

        filename = self.file.filename.lower()

        if "drivers_license" in filename:
            return "drivers_licence"

        if "bank_statement" in filename:
            return "bank_statement"

        if "invoice" in filename:
            return "invoice"

        return "unknown file"
