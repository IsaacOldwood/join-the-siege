from werkzeug.datastructures import FileStorage


class FileContentsClassifier:
    def __init__(self, file: FileStorage):
        """Classify a file based on its name."""
        self.file = file

    async def classify(self):
        """Classify the file based on its name."""

        filename = self.file.filename.lower()

        if not filename.endswith(".csv"):
            return None

        file_contents = await self.file.read()

        file_contents = file_contents.decode("utf-8")

        if "invoice" in file_contents:
            return "invoice"

        return None
